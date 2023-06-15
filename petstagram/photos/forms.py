from django import forms

from petstagram.photos.models import Photo


class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'


class EditPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['photo']
