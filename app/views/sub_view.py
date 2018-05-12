from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Filter(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "subview/filter.html")

class View(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "subview/view.html")

class Upload(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "subview/upload.html")

class Logout(TemplateView):
    def get(self, request, **kwargs):
        if 'ActiveUser' in request.session:
            del request.session['ActiveUser']