from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.common.views import photo_likes_count, user_already_liked_photo
from petstagram.pets.forms import CreatePetForm, EditPetForm, DeletePetForm
from petstagram.pets.models import Pet


class AddPetView(CreateView):
    template_name = 'pet-add-page.html'
    form_class = CreatePetForm

    def get_success_url(self):
        return reverse_lazy('display home')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()
    if request.method == 'POST':
        pet.delete()
        return redirect('account details', pk=1)
    form = DeletePetForm(initial=pet.__dict__)
    context = {'form': form}
    return render(request, template_name='pet-delete-page.html', context=context)


class DetailsPetView(DetailView):
    model = Pet
    template_name = 'pet-details-page.html'
    slug_url_kwarg = 'pet_slug'
    comment_form = CommentForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet_photos'] = self.object.photo_set.all()
        context['is_owner'] = self.object.user == self.request.user

        return context


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()

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
