from django.shortcuts import render

from petstagram.common.views import photo_likes_count, user_already_liked_photo
from petstagram.photos.models import Photo


def add_photo(request):
    return render(request, template_name='photo-add-page.html')


def details_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo_likes = photo_likes_count(photo)
    photo_liked = user_already_liked_photo(photo)

    photo_likes = photo.photolike_set.all()
    photo_comments = photo.photocomment_set.all()

    context = {
        'photo' : photo,
        'photo_likes': photo_likes,
        'photo_comments': photo_comments
    }
    return render(request, template_name='photo-details-page.html', context=context)


def edit_photo(request, pk):
    return render(request, template_name='photo-edit-page.html')


