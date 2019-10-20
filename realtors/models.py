from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length = 200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(datetime.now(), blank=True)

    # This method sets the default name that appears in the Django Admin backend
    def __str__(self):
        return self.name