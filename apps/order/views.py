from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.base import View
from django.urls import reverse
from .models import WorkOrder,Category,Resolution,Priority,Statue
from  organization.models import Company,CityDistrict,Employee
from users.models import UserProfile
from datetime import datetime
from pure_pagination import Paginator,PageNotAnInteger
from django.db.models import Q
from .form import NewOrderForm
from operation.models import UserComments
import json


class NewOrderView(View):
    def get(self,request):
        all_company=Company.objects.all()
        all_city_district=CityDistrict.objects.all()
        all_category=Category.objects.all()
        all_receiver=UserProfile.objects.all()
        priorities=Priority.objects.all()
        statues=Statue.objects.all()
        return render(request,'new-order.html',{
            'all_company':all_company,
            'all_city_district':all_city_district,
            'all_category':all_category,
            'all_receiver':all_receiver,
            'priorities':priorities,
            'statues':statues,
        })

    def post(self,request):
        em_id=request.POST.get('ID')
        company=request.POST.get('company')
        employee_name=request.POST.get('employee_name')
        phone = request.POST.get('phone')
        category = request.POST.get('category')
        priority = request.POST.get('priority')
        statue = request.POST.get('statue')
        receiver = request.POST.get('receiver')
        title = request.POST.get('title')
        description = request.POST.get('description')
        remark = request.POST.get('remark')

        if em_id == '':
            return HttpResponseRedirect(reverse('order:new_order'))
        emp=Employee()
        try:
            emp=Employee.objects.get(employee_id=em_id)
        except:
            new_order=NewOrderForm(request.POST)
            if new_order:
                emp.employee_id=em_id
                emp.company=Company.objects.get(id=int(company))
                emp.name=employee_name
                emp.phone=phone
                emp.add_time=datetime.now()
                emp.save()

        if emp:
            work_order = WorkOrder()
            work_order.employee_id = emp.employee_id
            work_order.company = emp.company
            work_order.customer = emp
            work_order.phone=emp.phone
            work_order.category = Category.objects.get(id=int(category))
            work_order.priority = Priority.objects.get(id=int(priority))
            work_order.statue = Statue.objects.get(id=int(statue))
            work_order.assigned_to = UserProfile.objects.get(id=int(receiver))
            work_order.title = title
            work_order.description = description
            work_order.comment = remark
            work_order.add_time=datetime.now()
            work_order.save()
            if 'save' in request.POST:
                return HttpResponseRedirect(reverse('order:all_list'))
            else:
                return HttpResponseRedirect(reverse('order:new_order'))
        return render(request, 'new-order.html', { 'new_form': new_order})


class MyOrderView(View):
    def get(self,request):
        unsigned_orders=WorkOrder.objects.filter(Q(assigned_to=request.user)).order_by('-add_time').\
            exclude(statue=Statue.objects.get(status='已完成'))[:3]

        processing_order=WorkOrder.objects.filter(Q(assigned_to=request.user) & Q(statue=Statue.objects.get(status='处理中'))).order_by('-add_time').\
            exclude(statue=Statue.objects.get(status='已完成'))[:3]

        pending_order=WorkOrder.objects.filter(Q(assigned_to=request.user) &
                                              Q(statue=Statue.objects.get(status='挂起'))).order_by('-add_time').\
            exclude(statue=Statue.objects.get(status='已完成'))[:3]

        urgent_order = WorkOrder.objects.filter(Q(assigned_to=request.user) &
                                                Q(priority=Priority.objects.get(priority='紧急'))).order_by('-add_time').\
            exclude(statue=Statue.objects.get(status='已完成'))[:3]

        all_my_order = WorkOrder.objects.filter(Q(assigned_to=request.user)).order_by('add_time').\
            exclude(statue=Statue.objects.get(status='已完成'))[:3]

        return render(request,'my-order.html',{
            'unsigned_orders':unsigned_orders,
            'processing_order':processing_order,
            'pending_order':pending_order,
            'urgent_order':urgent_order,
            'all_my_order':all_my_order
        })


class OrderDetailView(View):
    def get(self,request,ord_id):
        current_order=WorkOrder.objects.get(id=int(ord_id))
        all_category=Category.objects.all()
        all_resolution=Resolution.objects.all()
        all_receiver=UserProfile.objects.all()
        priorities=Priority.objects.all()
        statues=Statue.objects.all()
        all_current_comment=UserComments.objects.filter(work_order=current_order).order_by('-add_time')
        return render(request,'order-detail.html',{
            'current_order':current_order,
            'all_category':all_category,
            'all_resolution':all_resolution,
            'all_receiver':all_receiver,
            'priorities':priorities,
            'statues':statues,
            'all_current_comment':all_current_comment
        })


class UnsignedView(View):
    def get(self,request):
        all_list = WorkOrder.objects.filter(Q(assigned_to=request.user) &
                                           Q(statue=Statue.objects.get(status='新建'))). \
                       exclude(statue=Statue.objects.get(status='已完成')).order_by('-add_time')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_list, 10, request=request)
        all_list = p.page(page)

        return render(request,'my-order-list.html',{
            'all_list':all_list
        })


class MyWorkView(View):
    def get(self,request):
        all_list = WorkOrder.objects.filter(assigned_to=request.user)
        all_list = all_list.exclude(statue=Statue.objects.get(status='已完成')).order_by('-add_time')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_list,10 , request=request)
        all_list = p.page(page)

        return render(request,'my-order-list.html',{
            'all_list':all_list
        })


class TeamWorkView(View):
    def get(self,request):
        all_list = WorkOrder.objects.exclude(assigned_to=UserProfile.objects.get(name=''))\
            .exclude(statue=Statue.objects.get(status='已完成')).order_by('-add_time')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_list,10 , request=request)
        all_list = p.page(page)

        return render(request,'my-order-list.html',{
            'all_list':all_list
        })


class AllUrgentView(View):
    def get(self,request):
        all_list = WorkOrder.objects.filter(priority=Priority.objects.get(priority='紧急'))\
            .exclude(statue=Statue.objects.get(status='已完成')).order_by('-add_time')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_list,10 , request=request)
        all_list = p.page(page)

        return render(request,'my-order-list.html',{
            'all_list':all_list
        })


class AllUnsignedView(View):
    def get(self,request):
        all_list = WorkOrder.objects.filter(assigned_to=UserProfile.objects.get(name='')).\
            exclude(statue=Statue.objects.get(status='已完成')).order_by('-add_time')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_list,10 , request=request)
        all_list = p.page(page)

        return render(request,'my-order-list.html',{
            'all_list':all_list
        })


class ClosedOrderView(View):
    def get(self,request):
        all_list = WorkOrder.objects.filter(statue=Statue.objects.get(status='已完成')).order_by('-add_time')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_list,10 , request=request)
        all_list = p.page(page)
        return render(request,'my-order-list.html',{
            'all_list':all_list
        })


class ProcessingView(View):
    def get(self, request):
        all_list = WorkOrder.objects.filter(Q(assigned_to=request.user) &
                                            Q(statue=Statue.objects.get(status='处理中'))).\
                       exclude(statue=Statue.objects.get(status='已完成')).order_by('-add_time')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_list,10 , request=request)
        all_list = p.page(page)
        return render(request, 'my-order-list.html', {
            'all_list': all_list
            })


class PendingView(View):
    def get(self, request):
        all_list = WorkOrder.objects.filter(Q(assigned_to=request.user) &
                                              Q(statue=Statue.objects.get(status='挂起'))). \
                       exclude(statue=Statue.objects.get(status='已完成')).order_by('-add_time')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_list,10 , request=request)
        all_list = p.page(page)
        return render(request, 'my-order-list.html', {
            'all_list': all_list
        })


class UrgentView(View):
    def get(self, request):
        all_list = WorkOrder.objects.filter(Q(assigned_to=request.user) &
                                           Q(priority=Priority.objects.get(priority='紧急'))). \
                       exclude(statue=Statue.objects.get(status='已完成')).order_by('-add_time')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_list,10 , request=request)
        all_list = p.page(page)

        return render(request, 'my-order-list.html', {
            'all_list': all_list
        })


class MyAllListView(View):
    def get(self,request):
        all_list = WorkOrder.objects.filter(assigned_to=request.user).order_by('-add_time').\
            exclude(statue=Statue.objects.get(status='已完成'))
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_list,10 , request=request)
        all_list = p.page(page)

        return render(request,'my-order-list.html',{
            'all_list':all_list
        })


class AllListView(View):
    def get(self,request):
        all_list=WorkOrder.objects.all().order_by('-add_time')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_list,10 , request=request)
        all_list = p.page(page)

        return render(request,'all-order-list.html',{
            'all_list':all_list,
        })


class GetEmployeeInfo(View):
    def post(self,request):
        em_id=request.POST.get('employeeID','')
        if em_id == '':
            return HttpResponse(json.dumps({'statue': '1'}), content_type='application/json')
        try:
            emp=Employee.objects.get(employee_id=em_id)

            if emp:
                args = {
                    'statue': 'success',
                    'company': emp.company.name,
                    'employee_name': emp.name,
                    'phone': emp.phone,
                }
                return HttpResponse(json.dumps(args), content_type='application/json')
        except:
            return HttpResponse(json.dumps({'statue': '2'}), content_type='application/json')