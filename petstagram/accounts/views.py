from django.shortcuts import render


def login_account(request):
    return render(request, template_name='login-page.html')


def delete_account(request, pk):
    return render(request, template_name='profile-delete-page.html')


def details_account(request, pk):
    return render(request, template_name='profile-details-page.html')


def edit_account(request, pk):
    return render(request, template_name='profile-edit-page.html')


def register_account(request):
    return render(request, template_name='register-page.html')

