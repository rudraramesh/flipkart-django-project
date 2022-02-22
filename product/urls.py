import django
from django.urls import path
from . import views


urlpatterns=[
    path('',views.index),
    path('addproduct/',views.product_post),
    path('addcategory/',views.category_post),
]