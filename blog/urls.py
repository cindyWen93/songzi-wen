from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name = 'post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/blog.views.post_detail$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^post/(?P<pk>\d+)/addgifts/$', views.post_add_gifts, name='post_add_gifts'),
    url(r'^post/(?P<pk>\d+)/addgifts/addlikes/$', views.post_add_likes, name='post_add_likes'),
    url(r'^post/(?P<pk>\d+)/addgifts/addeggs/$', views.post_add_eggs, name='post_add_eggs'),
    url(r'^post/(?P<pk>\d+)/addgifts/addflowers/$', views.post_add_flowers, name='post_add_flowers'),
    url(r'^post/(?P<pk>\d+)/addgifts/addknees/$', views.post_add_knees, name='post_add_knees'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^alert/$', views.alert, name='alert'),

]