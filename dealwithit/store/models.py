from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # auto_now_add adds the current time to the property whenever the object
    # Is created but it can't be updated anymore once added
    # Use default=timezone.now instead if you want the ability to
    # Update the date and time further more.
    # Another option is simply use auto_now, if you want the date and
    # Time to update everytime the object itself is updated (surely not useful in this scenario)
    date_posted = models.DateTimeField(auto_now_add=True)

    # seller is a reference to the User object through a ForeignKey 
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    price = models.DecimalField(default=0.00 , max_digits=10 , decimal_places=2)
    image = models.ImageField(default='default_product.jpg', upload_to='product_imgs')
    # category -> needs to be added after the creation of the category model

    def __str__(self):
        return self.name

    
    # This method overrides the default save() method
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Get the image path and checks the image
        # For size optimization, in order to prevent
        # Too many large files to be uploaded to the server
        # And resizes it if necessary
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)