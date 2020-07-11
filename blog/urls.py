from django.urls import path, re_path
from . import views

urlpatterns = [
    path('' , views.PostListView.as_view() , name = 'post_list'),
    path('about/' , views.AboutView.as_view(), name='about'),
    path('post/new/' , views.CreatePostView.as_view() , name = 'post_new'),
    re_path(r'^post/(?P<pk>\d+)$' , views.PostDetailView.as_view() , name='post_detail'),
    re_path(r'^post/(?P<pk>\d+)/edit/$' , views.UpdatePostView.as_view() , name='post_edit'),
    re_path(r'^post/(?P<pk>\d+)/delete/$' , views.DeletePostView.as_view() , name='post_delete'),
    path('drafts/' , views.DraftListView.as_view() , name='post_drafts_list'),
]
