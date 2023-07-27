from django.db import models

# Create your models here.
from django.db import models


class MyModel(models.Model):
    # 다음과 같이 ImageField를 정의합니다.
    photo = models.ImageField(upload_to='photos/', null=False)


class TestModel(models.Model):
    txval = models.CharField(max_length=20)
