"""ITIL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.urls import path,include,re_path
from users.views import IndexView
from django.views.static import serve
from ITIL.settings import MEDIA_ROOT,STATICFILES_DIRS

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('user/',include('users.urls')),
    path('order/',include('order.urls')),
    path('operation/',include('operation.urls')),
    re_path('static/(?P<path>.*)', serve, {'document_root': STATICFILES_DIRS}),
    re_path('media/(?P<path>.*)', serve, {'document_root':MEDIA_ROOT}),
    path('',IndexView.as_view(),name='index'),
    path('ueditor/',include('DjangoUeditor.urls')),
]
