from django.shortcuts import render
#from django.utils import timezone
from .models import Tornei
from .models import Iscrivi

def lista_tornei_iscritti(request):
    if request.user.is_authenticated:
        iscritti = Iscrivi.objects.all()
        return render(request, 'agenda.html', {'iscritti': iscritti})
    else:
         return render(request, 'errore_generico.html', {})

def lista_tornei(request):
    if request.user.is_authenticated:
        tornei = Tornei.objects.all()
        return render(request, 'lista_tornei.html', {'tornei': tornei})
    else:
         return render(request, 'login_error.html', {})

def iscrivi_tornei(request):
    username = request.POST['username']
    nome_torneo = request.POST['nome_torneo']
    campo_torneo = request.POST['campo_torneo']
    try:
        iscritti=Iscrivi.objects.all()
        for iscritto in iscritti:
            if iscritto.username==username and iscritto.nome_torneo==nome_torneo and iscritto.campo_torneo==campo_torneo:
                return render(request, 'errore_iscrizione.html', {})
            else:
                Iscrivi.objects.create(username=username, nome_torneo=nome_torneo, campo_torneo= campo_torneo)
                return render(request, 'complimenti_iscrizione.html', {})
    except:
        return render(request, 'errore_generico.html', {})

