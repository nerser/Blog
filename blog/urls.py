from django.urls import path

from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<str:slug>/', views.PostDetail.as_view(), name='post_detail_url'),
    path('tags/', views.tags_list, name='tags_list_url'),
    path('tag/<str:slug>', views.TagDetail.as_view(), name='tag_detail_url'),
]
