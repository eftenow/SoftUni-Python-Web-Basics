from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.db import models

from petstagram.accounts.models import Profile

UserModel = get_user_model()


class CreateProfileForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("email", "username", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            user=user
        )
        if commit:
            return profile.save()
        return profile


class LoginProfileForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'autofocus': True,
            'placeholder': 'Username'
        })
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class EditUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        profile_fields = ['first_name', 'last_name', 'profile_picture', 'gender']
        for field in profile_fields:
            verbose_name = Profile._meta.get_field(field).verbose_name
            placeholder = verbose_name.capitalize()
            self.fields[field] = forms.CharField(
                label=verbose_name,
                widget=forms.TextInput(attrs={'placeholder': placeholder})
            )

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
