from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse
from pyperclip import copy

from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import PhotoLike, PhotoComment
from petstagram.photos.models import Photo

UserModel = get_user_model()


def photo_likes_count(photo):
    photo.likes_count = photo.likes.all().count()
    return photo


def user_already_liked_photo(photo):
    photo.user_liked = photo.likes.count() > 0
    return photo


def display_home(request):
    photos = Photo.objects.all()
    search_form = SearchForm()
    user = UserModel.objects.filter(pk=request.user.pk).first()
    liked_photos_by_user = []

    if user is not None:
        liked_photos_by_user = [like.to_photo for like in user.likes.all()]

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            photos = photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])

    photos = [photo_likes_count(photo) for photo in photos]
    comment_form = CommentForm()

    context = {
        'photos': photos,
        'comment_form': comment_form,
        'search_form': search_form,
        'liked_photos_by_user': liked_photos_by_user
    }

    return render(request, template_name='home-page.html', context=context)


def like_photo_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    like_object = PhotoLike.objects.filter(to_photo_id=photo_id, user=request.user).first()

    if like_object:
        like_object.delete()
    else:
        like = PhotoLike(to_photo=photo, user=request.user)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def share_photo_functionality(request, photo_id):
    photo_url = request.META['HTTP_HOST'] + reverse('photo details', args=[photo_id])
    copy(photo_url)

    return redirect(request.META['HTTP_REFERER'] + f'photos/{photo_id}')


def add_comment_functionality(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.filter(id=photo_id, user=request.user).get()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.user = request.user
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
