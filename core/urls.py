# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('candidates/', views.candidates, name='candidates'),
    path('testimony/', views.testimony, name='testimony'),
    path('contact/', views.contact, name='contact'),
    path('candidates/add/', views.add_candidate, name='add_candidate'),
]
