from django.shortcuts import render
from django.utils import timezone
from .models import Campi

def lista_campi(request):
    if request.user.is_authenticated:
        campi = Campi.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'lista_campi.html', {'campi': campi})
    else:
         return render(request, 'login_error.html', {})