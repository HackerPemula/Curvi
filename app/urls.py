from django.urls import path
from app.views import index_view, auth_view, hrportal_view

urlpatterns = [
    path('', index_view.Index.as_view(), name='home'),
    path('login/', auth_view.Login.as_view(), name='login'),
    path('logout/', auth_view.Logout.as_view(), name='logout'),
    path('hrportal/', hrportal_view.HRPortal.as_view(), name='hrportal'),
]
