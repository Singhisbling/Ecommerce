from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.product, name='product'),
    url(r'^(?P<pk>\d+)/$', views.description, name='description'),
    url(r'^chakker/(?P<pk>\d+)/$', views.chakker, name='chakker'),
    url(r'^delete/(?P<productId>\d+)/$',views.delete,name="delete"),
    url(r'^ads/$', views.Ads, name="ads"),
    url(r'^order/(?P<pk>\d+)/$',views.order,name="order"),




]
