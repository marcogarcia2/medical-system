from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    #path('consultas/', views.consultas, name='consultas'),  # Página de consultas
    path('login/', views.login_view, name='login'),  # Página de login
    path('register/', views.register_view, name='register'),  # Página de cadastro

]