from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile,Project

@receiver(post_save,sender=User)
def create_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance,full_name = instance.first_name,phone = instance.last_name)

@receiver(post_save,sender=User)
def save_profile(sender,instance, **kwargs):
    instance.profile.save()

