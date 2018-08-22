from django.urls import path,re_path
from .views import NewOrderView,MyOrderView,MyAllListView,GetEmployeeInfo,\
    AllListView,OrderDetailView,UnsignedView,ProcessingView,UrgentView,PendingView,\
    MyWorkView,AllUnsignedView,AllUrgentView,TeamWorkView,ClosedOrderView

app_name='order'

urlpatterns=[
    path('new_order/', NewOrderView.as_view(),name='new_order'),
    path('get_employee/', GetEmployeeInfo.as_view(), name='get_employee'),
    path('my_order/',MyOrderView.as_view(),name='my_order'),
    path('my_order/all_list',MyAllListView.as_view(),name='my_order_list'),
    path('all_list/',AllListView.as_view(),name='all_list'),
    path('all_closed/', ClosedOrderView.as_view(), name='all_closed'),

    path('unsigned/',UnsignedView.as_view(),name='unsigned'),
    path('processing/',ProcessingView.as_view(),name='processing'),
    path('urgent/',UrgentView.as_view(),name='urgent'),
    path('pending/',PendingView.as_view(),name='pending'),

    path('my_work/', MyWorkView.as_view(), name='my_work'),
    path('all_unsigned/', AllUnsignedView.as_view(), name='all_unsigned'),
    path('all_urgent/', AllUrgentView.as_view(), name='all_urgent'),
    path('team_work/', TeamWorkView.as_view(), name='team_work'),

    re_path('order_detail/(?P<ord_id>\d+)/',OrderDetailView.as_view(),name='order_detail'),
]
