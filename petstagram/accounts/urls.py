from django.urls import path, include

from petstagram.accounts.views import login_account, delete_account, details_account, edit_account, register_account

urlpatterns = [
    path('login/', login_account, name='account register'),
    path('register/', register_account, name='register account'),
    path('profile/<int:pk>/', include([
        path('', details_account, name='account details'),
        path('edit/', edit_account, name='account edit'),
        path('delete/', delete_account, name='delete register')
    ]))
]