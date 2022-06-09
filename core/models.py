from django.db import models

# Create your models here.


class TimeStampModel(models.Model):
    """TimeStamp Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        # https://docs.djangoproject.com/en/4.0/topics/db/models/#abstract-base-classes
