from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

# def consultas(request):
#     # Verifica se o usuário está logado
#     if not request.user.is_authenticated:
#         return render(request, 'website/login.html')
#     return render(request, 'website/consultas.html')

def login_view(request):
    # Lógica de login (exemplo simplificado)
    if request.method == 'POST':
        # Autenticação aqui
        pass
    return render(request, 'website/login.html')

def register_view(request):
    if request.method == 'POST':
        # Lógica de cadastro do usuário
        pass
    return render(request, 'website/register.html')
    