from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView, 
    ProductCreateView, 
    ProductUpdateView,
    ProductDeleteView,
    CategoryProductListView,
    UserProductListView
    )
# import current app views to define its routes
from . import views


# define routes for this particular app
urlpatterns = [
    # 'name' argument helps to refer to this route on other sections of the project, like the template for example
    # This class based view will look for a template with the pattern <app>/<model>_<viewtype>.html by default
    path('', ProductListView.as_view(), name='store_home'),

    path('category/<str:category>/', CategoryProductListView.as_view(), name='category_products'),
    path('user_products/<str:username>/', UserProductListView.as_view(), name='user_products'),

    # Explicity grabs the Primary Key from the ListView and passes it through the URL in order to show the details of a particular object
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/new/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'), 
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'), 

    # Route to a regular function based view
    path('about/', views.about, name='store_about'),
]