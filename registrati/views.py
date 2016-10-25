from django.shortcuts import render
from django.contrib.auth.models import User

def registrazione(request):
    return render(request, 'registrazione.html', {})

def registrati(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    try:
        user = User.objects.create_user(username=username, email=email, password=password)
    except:
        return render(request, 'login_error.html')
    if user is not None:
        user.save()
        return render(request, 'sei_registrato.html')
    else:
        return render(request, 'login_error.html')
