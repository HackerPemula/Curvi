from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import make_middleware_decorator

# Create your views here.
class HRPortal(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "hrportal.html")