from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # auto_now_add adds the current time to the property whenever the object
    # is created but it can't be updated anymore once added
    # use default=timezone.now instead if you want the ability to
    # update the date and time further more
    # another option is simply use auto_now, if you want the date and
    # time to update everytime the object itself is updated (surely not useful in this scenario)
    date_posted = models.DateTimeField(auto_now_add=True)

    # seller is a reference to the User object through a ForeignKey 
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    price = models.DecimalField(default=0.00 , max_digits=10 , decimal_places=2)
    image = models.ImageField(default='default.jpg', upload_to='product_imgs')
    # category -> needs to be added after the creation of the category model

    def __str__(self):
        return self.name

    
    # overrides the default save() method
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # get the image path and checks the image
        # for size optimization, in order to prevent
        # too many large files to be uploaded to the server
        # and resizes it if necessary
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)