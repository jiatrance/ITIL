import xadmin
from .models import UserComments


class UserCommentsAdmin(object):
    list_display = ['user', 'work_order', 'comments', 'add_time']
    search_fields = ['user', 'work_order', 'comments']
    list_filter = ['user', 'work_order', 'comments', 'add_time']