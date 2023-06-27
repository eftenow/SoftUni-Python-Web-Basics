from django.urls import path, include

from petstagram.photos.views import CreatePhotoView, DetailsPhotoView, edit_photo, delete_photo

urlpatterns = [
    path('add/', CreatePhotoView.as_view(), name='photo add'),
    path('<int:pk>/', include([
        path('', DetailsPhotoView.as_view(), name='photo details'),
        path('edit/', edit_photo, name='photo edit'),
        path('delete/', delete_photo, name='photo delete'),
    ]))
]