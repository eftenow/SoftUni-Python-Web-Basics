from django.shortcuts import render


def add_pet(request):
    return render(request, template_name='pet-add-page.html')


def delete_pet(request, username, pet_slug):
    return render(request, template_name='pet-delete-page.html')


def details_pet(request, username, pet_slug):
    return render(request, template_name='pet-details-page.html')


def edit_pet(request, username, pet_slug):
    return render(request, template_name='pet-edit-page.html')
