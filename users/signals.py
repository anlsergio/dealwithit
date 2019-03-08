from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# post_save is the signal itself (a trigger)
# User is the object who is firing the signal
# Explained: When a User is saved send the signal to the receiver (method decorated with @receiver)

# instance: the actual instance of the User who has been created
# created: if the User was infact created (Boolean)
# **kwargs: any additional key-word arguments is accepted

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # credit=5 means that every new user will start with US$ 5 worth of credit
        Profile.objects.create(user=instance, credit=5)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()