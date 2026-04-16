from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.contact_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_success_view, name='contact_success'),
]
