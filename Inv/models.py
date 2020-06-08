from django.db import models

from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la categoria',
        unique=True
    )

    def __str__(self):
        #cuando se cargue la categoria hag referencia a su descripcion
        return '{}'.format(self.descripcion)

    def save(self):
        #guardar en mayusculas la descripcion
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save() #invoca al metodo para poder guardar el dato en mayusculas

    class Meta:
        verbose_name_plural = "Categorias"
