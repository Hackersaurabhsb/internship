from django.contrib import admin
from .models import Client,Artist,Work
# Register your models here.
admin.site.register(Client)
admin.site.register(Artist)
admin.site.register(Work)