from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

def index(request):
    #if request.user.is_autenticated:
    return render(request, 'index.html')
    #return  render(request, 'base.html')

def login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = autenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            error = 'Usuario ou Senha incorretos!'

    return  render(request, 'login.html')

def logout(request):
    logout(request)

    return render(request, 'login.html')

