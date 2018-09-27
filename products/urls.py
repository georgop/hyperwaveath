from django.urls import path,re_path
from . import views
from .models import Product
urlpatterns = [
    path('',views.index),
    path('<int:product_id>/',views.detail)
    ]