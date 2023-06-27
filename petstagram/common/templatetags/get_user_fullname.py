from django.contrib.auth import get_user_model
from django import template

from petstagram.accounts.models import Profile

register = template.Library()
UserModel = get_user_model()


@register.filter
def get_username_or_full_name(user_id):
    profile = Profile.objects.filter(user_id=user_id).get()
    return profile.get_full_name()
