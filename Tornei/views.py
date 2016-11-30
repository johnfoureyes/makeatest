from django.shortcuts import render
from django.utils import timezone
from .models import Tornei

def lista_tornei(request):
    if request.user.is_authenticated:
        tornei = Tornei.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'lista_tornei.html', {'tornei': tornei})
    else:
         return render(request, 'login_error.html', {})