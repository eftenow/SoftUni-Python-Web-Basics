from django.urls import path, include

from petstagram.photos.views import add_photo, details_photo, edit_photo

urlpatterns = [
    path('add/', add_photo, name='photo add'),
    path('<int:pk>/', include([
        path('', details_photo, name='photo details'),
        path('edit/', edit_photo, name='photo edit')
    ]))
]