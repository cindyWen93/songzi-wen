from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()
from . import views


urlpatterns = [

    url(r'^$', views.index, name = 'index'),
    url(r'^music/', include('music.urls')),
    url(r'^friends/$', views.friends, name = 'friends'),
    url(r'^photo/', include('photo.urls')),
    url(r'^myselfEnglish/$', views.myselfEnglish, name='myselfEnglish'),
    url(r'^watersun/$', views.watersun, name='watersun'),
    url(r'^chen/$', views.chen, name='chen'),
    url(r'^blog/', include('blog.urls')),
    url(r'^faye/$', views.fayeSong, name='faye'),

]
