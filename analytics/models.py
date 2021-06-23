from django.db import models

# Create your models here.
from shortner.models import KirrURL


class CLickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, KirrURL):
            obj, created = self.get_or_create(kirr_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    kirr_url = models.OneToOneField(KirrURL, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CLickEventManager()

    def __str__(self):
         return f"{self.count}"
