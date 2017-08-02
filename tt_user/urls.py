from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_handle/$', views.register_handler),
    url(r'^register_valid/$', views.register_valid),

    url(r'^login/$', views.login),
    url(r'^login_handle/$', views.login_handler),
    url(r'^logout/$', views.logout),

    url(r'^$', views.user_info),
    url(r'^site/$', views.user_site),
    url(r'^order/$', views.user_order),
    url(r'^islogin/$', views.islogin),

]
