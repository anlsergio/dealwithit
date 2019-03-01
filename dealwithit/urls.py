"""dealwithit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')), # store.urls would be responsible for creating particular rules for this particular app

    # This url is defined directly here because we want to refer to the root url while using users routes
    # Instead of doing somethin like users/register users/login, we'll can simply use /login
    path('register/', user_views.register, name='register'), 

    path('profile/', user_views.profile, name='profile'), 

    # It's a little bit different because it's a class based view
    # It's optional to specify a template_name to choose the location where Django will search for the template
    # By default, it looks for the "registration/login.html" template
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),

    # Here you need to define uidb64 and a token, since it's required for the underlying django template (the one which creates the email)
    # uidb64: The user's pk, who requested the password reset enconded in base 64
    # token: Used to check that the reset link is valid.
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete')
]


# If we're currently in DEBUG mode, we should set the URL pattern for MEDIA directory like
# The documentation says to do.
# Refer to: https://docs.djangoproject.com/en/2.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)