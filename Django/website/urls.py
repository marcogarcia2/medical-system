from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    #path('login/', views.login_view, name='login'),  # Página de login
    path('register/', views.register_view, name='register'),  # Página de cadastro
    path('consultas/', views.consultas_view, name='consultas'),  # Página de consultas

]