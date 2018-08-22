import xadmin
from xadmin import views


# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 修改title
    site_title = 'ITIL后台管理界面'
    # 修改footer
    site_footer = '佳佳的公司'
    # 收起菜单
    menu_style = 'accordion'


# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView,GlobalSettings)
# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView,BaseSetting)