from django.contrib.auth.mixins import \
    LoginRequiredMixin  # inherit this class in order to require authentication for class based views
from django.contrib.auth.mixins import \
    UserPassesTestMixin  # inherit this class in order to check if the user should access the view even if authenticated
from django.shortcuts import render
from django.views.generic import \
    CreateView  # Class based views to solve common problems and don't reinvent the wheel
from django.views.generic import DeleteView, DetailView, ListView, UpdateView

from .models import Product


# Create your views here.
def home(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'store/home.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'store/home.html' # default: <app>/<model>_<viewtype>.html
    context_object_name = 'products' # default: object_list
    ordering = ['-date_posted'] # It Changes the ordering to show the latest added products first

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = [
        'name',
        'description',
        'price',
        'image'
    ]

    # You need to override the default form_valid method in order to add
    # Some special attributes like the current user who's submiting the form
    # As the seller of the product
    def form_valid(self, form):
        # It basically says:
        # Before saving the content, get the current user and put it
        # Into the seller attribute of the current instance of the form
        form.instance.seller = self.request.user

        # After that the form can be validated
        return super().form_valid(form)


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