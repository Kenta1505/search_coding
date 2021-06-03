from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='file_eraser'

urlpatterns=[
    path('', views.main, name='file_eraser'),
]