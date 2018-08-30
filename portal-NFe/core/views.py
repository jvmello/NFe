from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render

def index(request):
    if request.user.is_anonymous:
        return render(request, 'index.html')
    return  render(request, 'base.html')

def login(request):
    context = {}
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return render(request, 'index.html')
        else:
            context = {'erro':{
                                'text':'Usuario ou senha invalidos!',
                                'type':'danger'
                                }
                       }

    return  render(request, 'login.html', context )

def logout(request):
    auth_logout(request)
    return render(request, 'login.html')

