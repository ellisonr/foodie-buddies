from django.contrib import admin
from .models import Restaurant, MenuItem, Comment

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Comment)
