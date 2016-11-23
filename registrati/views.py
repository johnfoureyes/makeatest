from django.shortcuts import render
from django.contrib.auth.models import User

def registrazione(request):
    return render(request, 'registrazione.html', {})

def registrati(request):
    nome = request.POST['nome']
    cognome = request.POST['cognome']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    try:
        user = User.objects.create_user(first_name= nome, last_name=cognome, username=username, email=email, password=password)
        if user is not None:
            user.is_active=False
            user.save()
            return render(request, 'sei_registrato.html')
        else:
            return render(request, 'login_error.html')
    except:
        return render(request, 'login_error.html')
