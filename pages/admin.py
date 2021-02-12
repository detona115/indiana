from django.contrib import admin

# Register your models here.
from .models import Parent, Child

admin.site.register(Parent)
admin.site.register(Child)