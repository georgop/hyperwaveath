from django.contrib import admin
from .models import Product

class QuestionAdmin(admin.ModelAdmin):
    search_fields = [
        'product_name',
        'product_id',
        'product_size',
    ]
admin.site.register(Product,QuestionAdmin)





