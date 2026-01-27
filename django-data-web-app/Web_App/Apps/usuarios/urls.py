# usuarios/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import registrar_usuario, login_usuario, logout_usuario
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.registrar_usuario, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='usuarios/password_reset.html'
    ), name='password_reset'),

    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='usuarios/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='usuarios/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='usuarios/password_reset_complete.html'
    ), name='password_reset_complete'),
]
