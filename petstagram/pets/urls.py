from django.urls import path, include

from petstagram.pets.views import AddPetView, DetailsPetView, delete_pet, edit_pet

urlpatterns = [
    path('add/', AddPetView.as_view(), name='pet add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', DetailsPetView.as_view(), name='pet details'),
        path('delete/', delete_pet, name='pet delete'),
        path('edit/', edit_pet, name='pet edit')
    ]))

]