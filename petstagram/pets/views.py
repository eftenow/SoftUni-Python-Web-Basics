from django.shortcuts import render, redirect

from petstagram.pets.forms import CreatePetForm, EditPetForm, DeletePetForm
from petstagram.pets.models import Pet


def add_pet(request):
    form = None

    if request.method == 'GET':
        form = CreatePetForm()
    elif request.method == 'POST':
        form = CreatePetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account details', pk=1)

    context = {
        'form': form
    }
    return render(request, template_name='pet-add-page.html', context=context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()
    if request.method == 'POST':
        pet.delete()
        return redirect('account details', pk=1)
    form = DeletePetForm(initial=pet.__dict__)
    context = {'form': form}
    return render(request, template_name='pet-delete-page.html', context=context)


def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'pet_photos': photos
    }

    return render(request, template_name='pet-details-page.html', context=context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()
    print(pet)

    if request.method == 'GET':
        form = EditPetForm(instance=pet)
    else:
        form = EditPetForm(request.POST, instance=pet)
        if form.is_valid():
            print('its valid')
            form.save()
            return redirect('pet details', username, pet_slug)
    context = {'form': form}

    return render(request, template_name='pet-edit-page.html', context=context)
