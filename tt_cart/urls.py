from django.conf.urls import url

import views

urlpatterns=[
    url('^add/$', views.add),
    url('^$', views.cart),
]