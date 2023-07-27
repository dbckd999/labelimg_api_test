from django.contrib import admin
from .models import MyModel, TestModel

# Register your models here.

admin.site.register(MyModel)
admin.site.register(TestModel)
