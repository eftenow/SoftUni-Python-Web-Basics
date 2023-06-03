from django.shortcuts import render

from petstagram.pets.models import Pet


def add_pet(request):
    return render(request, template_name='pet-add-page.html')


def delete_pet(request, username, pet_slug):
    return render(request, template_name='pet-delete-page.html')


def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'pet_photos': photos
    }

    return render(request, template_name='pet-details-page.html', context=context)


def edit_pet(request, username, pet_slug):
    return render(request, template_name='pet-edit-page.html')
