import xadmin
from .models import CityDistrict,Company,Employee


class CityDistrictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CompanyAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'dist', 'address', 'add_time']


class EmployeeAdmin(object):
    list_display = ['employee_id', 'name', 'company', 'add_time']
    search_fields = ['employee_id','company', 'name', ]
    list_filter = ['employee_id','company', 'name', 'add_time']


xadmin.site.register(CityDistrict, CityDistrictAdmin)
xadmin.site.register(Company, CompanyAdmin)
xadmin.site.register(Employee, EmployeeAdmin)