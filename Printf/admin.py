from django.contrib import admin

# Register your models here.
from .models import data,Snippet
admin.site.register(data)
admin.site.register(Snippet)