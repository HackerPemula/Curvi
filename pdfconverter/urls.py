from django.urls import path

from . import views

urlpatterns = [
    path('', views.file2PDF, name='topdf'),
    path('submit', views.submit, name='submit'),
]
