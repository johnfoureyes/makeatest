from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

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
    except:
        return render(request, 'login_error.html')
    if user is not None:
        user.is_active=False
        user.save()
        subject = 'Ciao'
        message = 'Arrivederci'
        from_email = settings.EMAIL_HOST_USER
        to_list = [email]
        send_mail(subject, message,from_email,to_list,fail_silently=False,)
        return render(request, 'sei_registrato.html')
    else:
        return render(request, 'login_error.html')

