from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True) #fecha de creacion solo se modifica una vez
    fm = models.DateTimeField(auto_now=True) #fecha que se modifica en cada transancion
    uc = models.ForeignKey(User, on_delete=models.CASCADE) #usuario que crea el registro
    um = models.IntegerField(blank=True, null= True) #usuario que modifica el registro, puede estar en blanco y ser nulo

    #Clase para que este modelo sea del tipo abstacto y no sea tomado en cuenta en la migracion
    class Meta:
        abstract=True