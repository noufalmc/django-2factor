from django.db import signals
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import CustomUser
from .models import CodesFactor

@receiver(post_save, sender=CustomUser)
def post_save_generate_code(sender, instance, created, *args, **kwargs):
    if created:
        CodesFactor.objects.create(user=instance)