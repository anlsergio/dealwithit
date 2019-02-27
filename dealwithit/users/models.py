from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

# Create your models here.
class Profile(models.Model, PhoneNumberField):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_profile.jpg', upload_to='profile_imgs')
    city = models.CharField(null=False, blank=False, max_length=50)
    state = models.CharField(null=False, blank=False, max_length=50)
    credit = models.DecimalField(default=0.00 , max_digits=10 , decimal_places=2)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False, null=True) # validators should be a list

    phone_number_is_public = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s profile"


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)