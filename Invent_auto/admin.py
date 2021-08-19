from django.contrib import admin
from Invent_auto import models

# Register your models here.

admin.register(models.Products)
admin.register(models.Retailers)
admin.register(models.Orders)
