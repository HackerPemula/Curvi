from django.urls import path
from . import views

urlpatterns = [
    path('submit', views.PDFConverter.as_view(), name='submit'),
]
