from django.urls import path, include

from petstagram.accounts.views import SignInView, ProfileDeleteView, UserDetailsView, \
    SignUpView, SignOutView, EditUserView

urlpatterns = [
    path('login/', SignInView.as_view(), name='login account'),
    path('register/', SignUpView.as_view(), name='register account'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='account details'),
        path('edit/', EditUserView.as_view(), name='account edit'),
        path('delete/', ProfileDeleteView.as_view(), name='delete account')
    ]))
]