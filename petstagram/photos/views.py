from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from petstagram.common.forms import CommentForm
from petstagram.common.views import photo_likes_count, user_already_liked_photo
from petstagram.photos.forms import CreatePhotoForm, EditPhotoForm
from petstagram.photos.models import Photo

UserModel = get_user_model()


class CreatePhotoView(CreateView):
    model = Photo
    template_name = 'photo-add-page.html'
    form_class = CreatePhotoForm

    def get_success_url(self):
        return reverse_lazy('display home')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class DetailsPhotoView(DetailView):
    template_name = 'photo-details-page.html'
    model = Photo
    form = CommentForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['photo_likes'] = self.object.likes.count()
        context['photo_comments'] = self.object.photocomment_set.all()
        context['is_owner'] = self.object.user == self.request.user
        return context


def edit_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    form = EditPhotoForm(request.POST or None, instance=photo)
    if form.is_valid():
        form.save()
        return redirect('photo details', pk=pk)

    context = {'form': form}
    return render(request, template_name='photo-edit-page.html', context=context)


def delete_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    photo.delete()
    return redirect('display home')
