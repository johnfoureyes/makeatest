from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

def pagina_login(request):
    return render(request, 'loggati.html', {})

def loggati(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'buonfine.html')
    else:
        return render(request, 'login_error.html')

def do_logout(request):
    logout(request)
    return render(request, 'index.html')

def area_riservata(request):
#    username = request.POST['username']
#    password = request.POST['password']
#    user = authenticate(username=username, password=password)
    if request.user.is_authenticated:
        return render(request, 'area_riservata.html')
    else:
        return render(request, 'login_error.html')
