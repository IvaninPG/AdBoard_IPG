from django.contrib import admin
from .models import Ad, Category, Response

admin.site.register(Category)
admin.site.register(Ad)
admin.site.register(Response)
