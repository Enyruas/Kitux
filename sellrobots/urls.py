from django.conf.urls import patterns, url

from sellrobots import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^search$', views.search),
    url(r'^search/$', views.search),
    url(r'^signup$', views.signup),
    url(r'^signout$', views.signout),
    url(r'^tests$', views.tests),
    url(r'^search/(?P<keyword>\w+)/(?P<page>\d+)$', views.search),
#    url(r'^search_result$', views.search_result),
)
