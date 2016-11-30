from django.conf.urls import url

from . import views

app_name = 'myapp'
urlpatterns = [
    url(r'^newshome/$', views.newshome, name = "newshome"),
    url(r'^newshome/Trumptab/$', views.Trumptab),
    url(r'^newshome/Trumptab/(?P<w>[A-Za-z0-9\- ]+)/$', views.picget),
    url(r'^newshome/Hillarytab/$', views.Hillarytab),
    url(r'^newshome/Hillarytab/(?P<w>[A-Za-z0-9\- ]+)/$', views.picget),
    url(r'^newshome/marihuanatab/$', views.marihuanatab),
    url(r'^newshome/marihuanatab/(?P<w>[A-Za-z0-9\- ]+)/$', views.picget),
    url(r'^newshome/Cubatab/$', views.Cubatab),
    url(r'^newshome/Cubatab/(?P<w>[A-Za-z0-9\- ]+)/$', views.picget),
]
