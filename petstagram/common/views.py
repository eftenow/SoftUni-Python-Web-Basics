from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse
from pyperclip import copy

from petstagram.common.forms import CommentForm
from petstagram.common.models import PhotoLike, PhotoComment
from petstagram.photos.models import Photo


def photo_likes_count(photo):
    photo.likes_count = photo.photolike_set.all().count()
    return photo


def user_already_liked_photo(photo):
    photo.user_liked = photo.likes_count > 0
    return photo


def display_home(request):
    photos = [photo_likes_count(photo) for photo in Photo.objects.all()]
    photos = [user_already_liked_photo(photo) for photo in photos]
    comment_form = CommentForm()

    context = {
        'photos': photos,
        'comment_form': comment_form
    }

    return render(request, template_name='home-page.html', context=context)


def like_photo_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    like_object = PhotoLike.objects.filter(to_photo_id=photo_id).first()

    if like_object:
        like_object.delete()
    else:
        like = PhotoLike(to_photo=photo)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def share_photo_functionality(request, photo_id):
    photo_url = request.META['HTTP_HOST'] + reverse('photo details', args=[photo_id])
    copy(photo_url)

    return redirect(request.META['HTTP_REFERER'] + f'photos/{photo_id}')


def add_comment_functionality(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.filter(id=photo_id).get()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


