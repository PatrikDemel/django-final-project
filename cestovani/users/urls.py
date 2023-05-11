from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='index'),
    path('login/', views.login_view, namae='login'),
    path('logout/', views.logout_view, namae='logout'),
]
