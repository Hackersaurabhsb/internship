from django.db import models
# Create your models here.
from django.conf import settings
class Client(models.Model):
    name=models.CharField(max_length=50)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
class Artist(models.Model):
    name=models.CharField(max_length=50)
    works=models.ManyToManyField('Work')
class Work(models.Model):
    work_choices=(
        ('Youtube','Youtube'),
        ('Instagram','Instagram'),
        ('Other','Other'),
    )
    link=models.URLField()
    work_type=models.CharField(max_length=30,choices=work_choices)
    