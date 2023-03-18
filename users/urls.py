from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('login/', views.user_login, name ='login'),
   # path('logout/', TemplateView.as_view(template_name="log_out.html"), name="logged_out"),
    path('register/', views.register, name='register'),
]