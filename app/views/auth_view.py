from django.shortcuts import render
from django.views.generic import TemplateView
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from auth_v2.auth_backend import AuthBackend
import json

# Create your views here.
class Login(TemplateView):
    def post(self, request, **kwargs):
        try:
            staff = AuthBackend.authenticate(request.POST['username'], request.POST['password'])

            response = {
                "message": "failed"
            }

            if staff:
                request.session['ActiveUser'] = staff
                
                response = {
                    "message": "success",
                    "url": "/hrportal"
                }
                return HttpResponse(json.dumps(response), content_type="application/json")
            
            return HttpResponse(json.dumps(response), content_type="application/json", status=401)
        except:
            return HttpResponse(status=400)

class Logout(TemplateView):
    def post(self, request, **kwargs):
        try:
            response = {
                "message": "failed"
            }

            if 'ActiveUser' in request.session:
                del request.session['ActiveUser']

                response = {
                    "message": "success",
                    "url": "/login"
                }

                return HttpResponse(json.dumps(response), content_type="application/json")

            return HttpResponse(json.dumps(response), content_type="application/json", status=401)
        except:
            return HttpResponse(status=400)