from django.db import models
from django.utils import timezone


class Campi(models.Model):
    author = models.ForeignKey('auth.User')
    nome = models.CharField(max_length=100)
    indirizzo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=500)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome