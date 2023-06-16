from django.urls import path

from petstagram.common import views

urlpatterns = [
    path('', views.display_home, name='display home'),
    path('like/<int:photo_id>/', views.like_photo_functionality, name='like photo'),
    path('share/<int:photo_id>/', views.share_photo_functionality, name='share photo'),
    path('comment/<int:photo_id>/', views.add_comment_functionality, name='add comment')
]
