from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from PIL import Image

# Create your models here.

class Category(models.Model):
    # Since the home template is served with a context_list with more than one object,
    # It's convenient to "tag" this class in order to indentify the object in the template
    model_name = 'Category'
    
    name = models.CharField(max_length=200)
    credit_weigth = models.IntegerField()

    def __str__(self):
        return self.name


class Product(models.Model):
    model_name = 'Product'
    name = models.CharField(max_length=100)
    description = models.TextField()

    # auto_now_add adds the current time to the property whenever the object
    # Is created but it can't be updated anymore once added
    # Use default=timezone.now instead if you want the ability to
    # Update the date and time further more.
    # Another option is simply use auto_now, if you want the date and
    # Time to update everytime the object itself is updated (surely not useful in this scenario)
    date_posted = models.DateTimeField(auto_now_add=True)

    expiration_date = models.DateTimeField(null=True)

    is_expired = models.BooleanField(default=False)

    # seller is a reference to the User object through a ForeignKey 
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    price = models.DecimalField(default=0.00 , max_digits=10 , decimal_places=2)
    image = models.ImageField(default='default_product.jpg', upload_to='product_imgs')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
    # This method overrides the default save() method
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Get the saved image path and checks the image
        # For size optimization, in order to prevent
        # Too many large files to be uploaded to the server
        # And resizes it if necessary
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    
    # Redirect vs Reverse:
    # Redirect would redirect you to a specific route
    # Reverse will return the URL/full path as a string
    # Since here we just want to get the URL and let the view handle the route for us, we just simply use reverse
    # The point here is that we need to reference the correct object detail by its Primary Key
    # So let the already created url route to manage this
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})