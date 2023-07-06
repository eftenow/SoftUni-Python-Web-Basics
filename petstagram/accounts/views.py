from django import forms
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from petstagram.accounts.forms import CreateProfileForm, LoginProfileForm, EditUserForm

UserModel = get_user_model()


class ProfileDeleteView(DeleteView):
    template_name = 'profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('display home')

    def post(self, request, *args, **kwargs):
        self.request.user.delete()
        return HttpResponseRedirect(self.success_url)


class UserDetailsView(DetailView):
    template_name = 'profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        photos = self.object.photo_set.all()
        paginator = Paginator(photos, 2)
        page_number = self.request.GET.get('page') or 1
        page_obj = paginator.get_page(page_number)
        context = super().get_context_data()
        total_likes_count = sum([p.likes.count() for p in self.object.photo_set.all()])

        context.update({
            'total_likes_count': total_likes_count,
            'paginator': paginator,
            'page_number': page_number,
            'page_obj': page_obj
        })

        return context


class SignOutView(LogoutView):
    next_page = reverse_lazy('display home')


class EditUserView(UpdateView):
    template_name = 'profile-edit-page.html'
    form_class = EditUserForm
    model = UserModel

    def form_valid(self, form):
        response = super().form_valid(form)

        profile = self.object.profile  # Works because there is a OneToOneField relationship  UserModel and Profile
        profile.first_name = form.cleaned_data['first_name']
        profile.last_name = form.cleaned_data['last_name']
        profile.profile_picture = form.cleaned_data['profile_picture']
        profile.gender = form.cleaned_data['gender']
        profile.save()

        return response

    def get_success_url(self):
        return reverse_lazy('account details', kwargs={'pk': self.object.pk})


class SignUpView(CreateView):
    template_name = 'register-page.html'
    form_class = CreateProfileForm

    def get_success_url(self):
        # Provide a valid URL to redirect to
        return reverse_lazy('display home')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = authenticate(
            self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        login(self.request, user)
        return response


class SignInView(LoginView):
    template_name = 'login-page.html'
    form_class = LoginProfileForm
    success_url = reverse_lazy('display home')
