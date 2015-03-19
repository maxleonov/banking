from django.conf.urls import patterns, url, include
from cashmachine import views


urlpatterns = patterns(
    '',
    url(r'^/?$', views.card, name='card'),
    url(r'^logout/?$', views.logout, name='logout'),
    url(r'^error/?$', views.error, name='error'),
    url(r'^pin/$', views.pin, name='pin'),
    url(r'^operations/?$', views.operations, name='operations'),
    url(r'^operations/balance/?$', views.balance, name='balance'),
    url(r'^operations/getcash/?$', views.getcash, name='getcash'),
    url(r'^operations/report/(?P<operation>\d{1,20})/?$', views.report,
        name='report'),
)
