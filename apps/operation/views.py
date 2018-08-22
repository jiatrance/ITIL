from django.shortcuts import render
from django.views.generic import View
from order.models import WorkOrder
from .models import UserComments
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from ITIL.settings import MEDIA_URL
from order.models import Category,Priority,Statue,Resolution
from users.models import UserProfile
from pure_pagination import Paginator,PageNotAnInteger
from django.db.models import Q
import json
import xlwt

from django.urls import reverse


class AddCommentsView(View):
    def post(self,request):
        order_id = request.POST.get('order_id', 0)
        if not request.user.is_authenticated:
            return HttpResponse("{'status':'fail','msg':'用户未登录'}",content_type='application/json')
        comment=request.POST.get('comment', '')

        if int(order_id) > 0 and comment:
            user_comment = UserComments()
            work_order = WorkOrder.objects.get(id=int(order_id))
            user_comment.work_order = work_order
            user_comment.comments=comment
            user_comment.user=request.user
            user_comment.add_time=datetime.now()
            user_comment.save()

            data={
                "status": "success",
                'img':MEDIA_URL+user_comment.user.image.path,
                'name':user_comment.user.name,
                'comments':user_comment.comments,
                'add_time':user_comment.add_time.strftime('%Y-%m-%d %H:%M:%S')
            }

            return HttpResponse(json.dumps(data), content_type='application/json')

        else:
            return HttpResponse('{"status":"fail"}', content_type='application/json')


class ExportExcelView(View):
    def get(self,request):
        all_order=WorkOrder.objects.all()
        all_category=Category.objects.all()
        all_resolution=Resolution.objects.all()
        all_receiver=UserProfile.objects.all()
        priorities=Priority.objects.all()
        statues=Statue.objects.all()
        return render(request,'export-excel.html',{
            'all_order':all_order,
            'all_category':all_category,
            'all_resolution':all_resolution,
            'all_receiver':all_receiver,
            'priorities':priorities,
            'statues':statues
        })


def get_excel(request,a,b,c,d,f):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Order' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '.xls'
    workbook = xlwt.Workbook(encoding='utf-8')  # 创建工作簿
    sheet = workbook.add_sheet("sheet1")  # 创建工作页
    row0 = [u'工号', u'部门', u'姓名', u'联系方式', u'故障类型',
            u'优先级', u'状态', u'指派给', u'标题', u'解决类型'
            ]
    for i in range(0, len(row0)):
        sheet.write(0, i, row0[i])

    work_order=WorkOrder.objects.all()
    if a != "all":
        work_order=work_order.filter(category=Category.objects.get(id=int(a)))
    if b != "all":
        work_order= work_order.filter(priority=Priority.objects.get(id=int(b)))
    if c != "all":
        work_order=work_order.filter(statue=Statue.objects.get(id=int(c)))
    if d != "all":
        work_order= work_order.filter(assigned_to=UserProfile.objects.get(id=int(d)))
    if f != "all":
        work_order=work_order.filter(resolution_code=Resolution.objects.get(id=int(f)))
    num = 1
    for d in work_order:
        sheet.write(num, 0, d.employee_id)
        sheet.write(num, 1, d.company.name)
        sheet.write(num, 2, d.customer.name)
        sheet.write(num, 3, d.phone)
        sheet.write(num, 4, d.category.case_type)
        sheet.write(num, 5, d.priority.priority)
        sheet.write(num, 6, d.statue.status)
        sheet.write(num, 7, d.assigned_to.name)
        sheet.write(num, 8, d.title)
        sheet.write(num, 9, solution_code(d))
        num = num + 1
    workbook.save(response)
    return response


def solution_code(work_order):
    if work_order.resolution_code:
        return work_order.resolution_code.resolution_code


class CloseOrderView(View):
    def get(self,request,ord_id):
        all_list = WorkOrder.objects.filter(assigned_to=request.user).order_by('-add_time')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_list, 10, request=request)
        all_list = p.page(page)

        return render(request, 'my-order-list.html', {
            'all_list': all_list
        })

    def post(self,request,ord_id):
        category = request.POST.get('category')
        priority = request.POST.get('priority')
        statue = request.POST.get('statue')
        receiver = request.POST.get('receiver')
        resolution_code=request.POST.get('solution_code')
        solution=request.POST.get('solution')

        work_order = WorkOrder.objects.get(id=int(ord_id))
        work_order.category = Category.objects.get(id=int(category))
        work_order.priority = Priority.objects.get(id=int(priority))
        work_order.statue = Statue.objects.get(id=int(statue))
        work_order.assigned_to = UserProfile.objects.get(id=int(receiver))
        work_order.close_time=datetime.now()
        work_order.resolution_code=Resolution.objects.get(id=int(resolution_code))
        work_order.resolution_notes=solution

        if work_order.assigned_to==UserProfile.objects.get(name=''):
            return HttpResponseRedirect(reverse('index'))

        if work_order.resolution_code == Resolution.objects.get(resolution_code='已解决'):
            work_order.done=True
            work_order.statue=Statue.objects.get(status='已完成')
            work_order.save()
            all_list = WorkOrder.objects.filter(Q(assigned_to=request.user)& Q(statue=Statue.objects.get(status='已完成'))).order_by('-add_time')
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(all_list, 10, request=request)
            all_list = p.page(page)
            return render(request, 'my-order-list.html', {
                'all_list': all_list
            })
        work_order.save()
        return HttpResponseRedirect(reverse('index'))


class ReopenView(View):
    def post(self,request):
        order_id = request.POST.get('ord_id',0)
        work_order = WorkOrder.objects.get(id=int(order_id))
        work_order.done=False
        work_order.statue=Statue.objects.get(status='重开')
        work_order.save()
        return HttpResponse('success')


class NewOpenView(View):
    def post(self,request):
        work_order = WorkOrder()
        work_order.done=False
        work_order.statue=Statue.objects.get(status='重开')
        work_order.save()
        return HttpResponse('success')


class ChartView(View):
    def get(self,request):
        return render(request,'charts.html')