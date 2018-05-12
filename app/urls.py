from django.urls import path
from app.views import index_view, auth_view, hrportal_view, sub_view

urlpatterns = [
    path('', index_view.Index.as_view(), name='home'),
    path('login/', auth_view.Login.as_view(), name='login'),
    path('logout/', auth_view.Logout.as_view(), name='logout'),
    path('hrportal/', hrportal_view.HRPortal.as_view(), name='hrportal'),
    path('hrportal/subview/filter', sub_view.Filter.as_view(), name='sv_filter'),
    path('hrportal/subview/view', sub_view.View.as_view(), name='sv_view'),
    path('hrportal/subview/logout', sub_view.Logout.as_view(), name='sv_logout'),
]
