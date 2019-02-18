from django.urls import path
# import current app views to define its routes
from . import views


# define routes for this particular app
urlpatterns = [
    path('', views.home, name='store_home'), # 'name' argument helps to refer to this route on other sections of the project, like the template for example
    path('about/', views.about, name='store_about'),
]
