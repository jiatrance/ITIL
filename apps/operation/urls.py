from django.urls import path,re_path
from .views import AddCommentsView,ExportExcelView,get_excel,ReopenView,CloseOrderView,ChartView

app_name='operation'

urlpatterns=[
    path('add_comments/', AddCommentsView.as_view(),name='add_comments'),
    path('get_url/',ExportExcelView.as_view(),name='get_url'),
    path('reopen/',ReopenView.as_view(),name='reopen'),
    path('chart/',ChartView.as_view(),name='chart'),
    re_path('close_order/(?P<ord_id>\d+)',CloseOrderView.as_view(),name='close_order'),
    re_path('Excel-(?P<a>\w+)-(?P<b>\w+)-(?P<c>\w+)-(?P<d>\w+)-(?P<f>\w+)/',get_excel,name='export_excel'),
]