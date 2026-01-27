from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView
from django.conf import settings
from django.conf.urls.static import static
from .views import home
from Apps.Legal.views import politicas_privacidad
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin-Alex&Ann/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # Página principal
    path('registro/', include('Apps.Formulario.urls')),
    path('eventos/', include('Apps.Eventos.urls')),
    path('legal/', include('Apps.Legal.urls')),
    path('marketing/', include('Apps.Marketing.urls')),
    path('usuarios/', include('Apps.usuarios.urls')),
    path('usuarios/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('usuarios/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('usuarios/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('usuarios/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('politicas/', politicas_privacidad, name='politicas'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)