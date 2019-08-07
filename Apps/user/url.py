from django.conf.urls import url
from .views import LogoutView, login_view, user_create, user_detail, user_update


urlpatterns =[
	
	url(r'^$', login_view.as_view() , name="login"),

	url(r'^logout/$', LogoutView.as_view() , name="logout"),
	url(r'^login/$', login_view.as_view() , name="login"),
	url(r'^user/create/$', user_create.as_view() , name="user_create"),
	url(r'^user/detail/(?P<pk>[^/]+)/$', user_detail.as_view() , name="user_detail"),
	url(r'^user/update/(?P<pk>[^/]+)/$', user_update.as_view() , name="user_update"),



	# url(r'^accounts/login/$', name='logoin')


]

