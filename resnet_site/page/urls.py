import django.urls
from django.urls import path, re_path
from . import views
app_name = 'page'

urlpatterns = [
    path('', views.upload_file, name='upload'),
]