from django.db import models

class User(models.Model):
    iUsers = models.IntegerField(primary_key=True)  # Usa la clave primaria existente
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name