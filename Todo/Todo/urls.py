from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('delete/<int:pk>/', delete),
    path('edit/<int:pk>/', edit),
]