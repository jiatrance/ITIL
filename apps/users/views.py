from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from .models import UserProfile
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.views.generic.base import View
from order.models import Statue,Priority
from order.views import WorkOrder
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .form import LoginForm


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user=UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class IndexView(View):
    def get(self,request):
        if request.user.is_authenticated:
            my_work = WorkOrder.objects.filter(assigned_to=request.user).order_by('-add_time')
            my_work=my_work.exclude(statue=Statue.objects.get(status='已完成'))
            team_work = WorkOrder.objects.exclude(assigned_to=UserProfile.objects.get(name='')) \
                .exclude(statue=Statue.objects.get(status='已完成')).order_by('-add_time')
            unsigned = WorkOrder.objects.filter(assigned_to=UserProfile.objects.get(name='')) \
                .exclude(statue=Statue.objects.get(status='已完成')).order_by('-add_time')
            all_urgent = WorkOrder.objects.filter(priority=Priority.objects.get(priority='紧急')) \
                .exclude(statue=Statue.objects.get(status='已完成')).order_by('-add_time')
            return render(request,'index.html',{
                'my_work': my_work,
                'unsigned': unsigned,
                'team_work': team_work,
                'all_urgent': all_urgent
            })
        else:
            return render(request,'page-login.html')


class LoginView(View):
    def get(self,request):
        return render(request,'page-login.html')

    def post(self,request):
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            username=request.POST.get('username',None)
            password=request.POST.get('password',None)

            user=authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request,'page-login.html',{'login_form':login_form })

        else:
            return render(request,'page-login.html',{ 'login_form':login_form })


class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))
