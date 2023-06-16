from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.common.views import photo_likes_count, user_already_liked_photo
from petstagram.photos.forms import CreatePhotoForm, EditPhotoForm
from petstagram.photos.models import Photo


def add_photo(request):
    form = CreatePhotoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('display home')

    context = {'form': form}
    return render(request, template_name='photo-add-page.html', context=context)


def details_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo_likes = photo_likes_count(photo)
    photo_liked = user_already_liked_photo(photo)

    photo_likes = photo.photolike_set.all()
    photo_comments = photo.photocomment_set.all()
    comment_form = CommentForm()

    context = {
        'photo': photo,
        'photo_likes': photo_likes,
        'photo_comments': photo_comments,
        'comment_form': comment_form
    }
    return render(request, template_name='photo-details-page.html', context=context)


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
