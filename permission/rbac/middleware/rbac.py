import re
from django.shortcuts import redirect,HttpResponse
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class RbacMiddleware(MiddlewareMixin):

    def process_request(self,request):

        for url in settings.PASS_URL_LIST:
            if re.match(url,request.path_info):
                return None
        permission_url_list = request.session.get(settings.SESSION_PERMISSION_URL_KEY)
        if not permission_url_list:
            return redirect(settings.LOGIN_URL)
        # 用户请求： /user/add/
        # 有权限
        # ^/user/$
        flag = False

        for db_url in permission_url_list:
            pattern = settings.URL_REGEX.format(db_url)
            if re.match(pattern,request.path_info):
                flag = True
                break



        # - request.path_info / index /
        #     - request.session["SESSION_PERMISSION_URL_KEY"]
        #     [
        #     / test /
        #     / login /
        #     / index /
        #     ]
        #     - 匹配
        #     - 成功：
        #     无
        #
        #         失败：
        #         return HttpResponse('xxx')
        #
        #
        #     - 登录页面无序任何权限


        if not flag:
            if settings.DEBUG:
                url_html = "<br/>".join(permission_url_list)
                return HttpResponse('无权访问: %s' %url_html)
            else:
                return HttpResponse('无权访问')