from django.db import models
from django.utils import timezone


class Tornei(models.Model):
    author = models.ForeignKey('auth.User')
    nome = models.CharField(max_length=100)
    campo = models.CharField(max_length=100)
    num_squad = models.IntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome

class Iscrivi(models.Model):
    username = models.CharField(max_length=100)
    nome_torneo = models.CharField(max_length=100)
    campo_torneo = models.CharField(max_length=100)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.username