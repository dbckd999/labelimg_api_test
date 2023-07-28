from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location="/Users/dbckd/Documents/img")


class MyModel(models.Model):
    photo = models.ImageField(storage=fs, null=False)
제