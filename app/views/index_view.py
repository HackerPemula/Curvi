from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Index(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "index.html")