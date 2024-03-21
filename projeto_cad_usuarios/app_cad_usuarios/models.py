from django.db import models

class Usuarios(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    