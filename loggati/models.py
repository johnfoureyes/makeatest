from django.db import models

class persona (models.Model):
    name = models.CharField(max_length = 50)
