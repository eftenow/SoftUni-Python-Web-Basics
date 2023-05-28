from django.urls import path, include

from petstagram.pets.views import add_pet, details_pet, delete_pet, edit_pet

urlpatterns = [
    path('add/', add_pet, name='pet add'),
    path('<str:username>/pet/<slug:petname>/', include([
        path('', details_pet, name='pet details'),
        path('delete/', delete_pet, name='pet delete'),
        path('edit/', edit_pet, name='pet edit')
    ]))

]