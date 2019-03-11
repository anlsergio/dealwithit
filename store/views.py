import decimal
from itertools import chain
from operator import attrgetter

from django import forms
from django.contrib.auth.mixins import \
    LoginRequiredMixin  # inherit this class in order to require authentication for class based views
from django.contrib.auth.mixins import \
    UserPassesTestMixin  # inherit this class in order to check if the user should access the view even if authenticated
from django.forms.utils import ErrorList
from django.http import Http404
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views.generic import \
    CreateView  # Class based views to solve common problems and don't reinvent the wheel
from django.views.generic import DeleteView, DetailView, ListView, UpdateView

from .models import Category, Product, User

# Create your views here.
# def home(request):
#     context = {
#         'products': Product.objects.all()
#     }
#     return render(request, 'store/home.html', context)

class ProductListView(ListView):
    # model = Product
    template_name = 'store/home.html' # default: <app>/<model>_<viewtype>.html
    # paginate_by = 2
    # context_object_name = 'products' # default: object_list
    # ordering = ['-date_posted'] # It Changes the ordering to show the latest added products first

    # Override the get_queryset method since it's need to get more than just a product list from the database
    # The template should also render Category list information
    def get_queryset(self):
        product_list = Product.objects.order_by('-date_posted')[:9] # Order by newest added and get only the first 9 ones
        category_list = Category.objects.all()

        result_list = list( # Convert it to a list
            # chain() helps concatenate all the elements into a list of objects [product1, product2, category1,...]. 
            # It works like a list generator
            chain(product_list, category_list) 
        )

        return result_list

# Class based view designed to handle Category filtering options for products' listing
class CategoryProductListView(ListView):
    model = Product
    template_name = 'store/product_category.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        # name: the 'name' attribute of the Category model
        # self.kwargs.get: gets the keyword arguments passed through the URL
        category_object = get_object_or_404(Category, name=self.kwargs.get('category'))
        return Product.objects.filter(category=category_object).order_by('-date_posted') # This returns the set of Product objects filtered by the category object stored in category_object

class UserProductListView(ListView):
    model = Product
    template_name = 'store/product_user.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        username = get_object_or_404(User, username=self.kwargs.get('username'))
        return Product.objects.filter(seller=username).order_by('-date_posted')

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = [
        'name',
        'description',
        'price',
        'category',
        'image'
    ]

    # You need to override the default form_valid method in order to add
    # Some special attributes like the current user who's submiting the form
    # As the seller of the product
    def form_valid(self, form):
        # It basically says:
        # Before saving the content, get the current user and put it
        # Into the seller attribute of the current instance of the form

        current_user = self.request.user

        form.instance.seller = current_user

        charge = decimal.Decimal(5 * form.instance.category.credit_weigth)

        if current_user.profile.credit - charge >= 0:
            current_user.profile.credit -= charge
            current_user.save()

            # After that the form can be validated
            return super().form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList([
                f"You need at least US${ charge } credits worth in order to proceed"
            ])
            return self.form_invalid(form)



class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = [
        'name',
        'description',
        'price',
        'image'
    ]

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    # Test function to prevent an user to mess with someone else's products
    def test_func(self):
        product = self.get_object() # get from the session the method which the user is trying to update
        if self.request.user == product.seller:
            return True
        return False


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/' # You need to define where to go after the deletion succeed

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.seller:
            return True
        return False


def about(request):
    return render(request, 'store/about.html', {'title': 'About'})
