from django.urls import path
import uuid
from . views import signup,profile,send_email
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('signup/',signup,name='signup-page'),
    path('',
         auth_views.LoginView.as_view(template_name='users/login.html'),
         name='users-login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='users/logout.html'),
                                       name='users-logout'),
    path('profile/',profile,name='users-profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('send_email/',send_email,name='send_email')
]