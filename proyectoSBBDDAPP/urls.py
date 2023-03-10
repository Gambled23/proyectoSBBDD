from django.contrib import admin
from django.urls import path

from proyectoSBBDDAPP import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate_report/', views.generate_report, name='generate_report'),
    path('report_status/', views.report_status, name='report_status'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('test/', views.test, name='test'),
    path('register_user/', views.register_user, name='register_user'),
]