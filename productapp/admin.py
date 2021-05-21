from django.contrib import admin
from .models import Product, Question, Choice

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Product)