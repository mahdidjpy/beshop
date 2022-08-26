from django.contrib import admin
from .models import Category, Product, Gender, Condition


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Gender)
admin.site.register(Condition)

