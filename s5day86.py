s5day86

本周回顾：
	1. 权限
		- 6表
		
	2. 缓存和中间件
	
	3. GitHub
	
	4. 信号
	
	5. 序列化
	
	6. 性能相关
	
	7. 分页
	
	8. Http请求本质
	
	9. FBV CBV
	
	10. Django请求生命周期


今日内容：
	- 中间件
	- 自动生成菜单
		- 默认展开
		- 默认选中
		
	- CURD
		- 基于ModelForm进行增删改查
		
	---> 独立app，用于做权限验证 <---
	

内容详细：
	- 中间件
	
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
	
	- 自动生成菜单
	
		session中存储菜单相关：
			- 所有菜单
			- 可以在菜单上显示的URL
	
		
	- 基于ModelForm进行增删改查： 
		- UserInfo
		- 3张
		
作业：
	1. 权限相关菜单/中间件
	2. 3张表
	
	结果：
		独立app，用于做权限。
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	