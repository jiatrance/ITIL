import xadmin
from .models import Category,Resolution,WorkOrder,Priority,Statue


class CategoryAdmin(object):
    list_display = ['case_type', 'add_time']
    search_fields = ['case_type']
    list_filter = ['case_type', 'add_time']


class ResolutionAdmin(object):
    list_display = ['resolution_code',  'add_time']
    search_fields = ['resolution_code']
    list_filter = ['resolution_code', 'add_time']


class PriorityAdmin(object):
    list_display = ['priority', 'add_time']
    search_fields = ['priority']
    list_filter = ['priority', 'add_time']


class StatusAdmin(object):
    list_display = ['status',  'add_time']
    search_fields = ['status']
    list_filter = ['status', 'add_time']


class WorkOrderAdmin(object):
    list_display = [ 'company','statue','assigned_to','title', 'add_time']
    search_fields = ['company', 'company','statue','assigned_to','title' ]
    list_filter = ['company', 'company','statue','assigned_to','title', 'add_time']


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Resolution, ResolutionAdmin)
xadmin.site.register(Priority, PriorityAdmin)
xadmin.site.register(Statue, StatusAdmin)
xadmin.site.register(WorkOrder, WorkOrderAdmin)