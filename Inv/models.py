from django.db import models

from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la categoria',
        unique=True
    )

    def __str__(self):
        #cuando se cargue la categoria haga referencia a su descripcion
        return '{}'.format(self.descripcion)

    def save(self):
        #guardar en mayusculas la descripcion
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save() #invoca al metodo para poder guardar el dato en mayusculas

    class Meta:
        verbose_name_plural = "Categorias"

class Subcategoria (ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    descripcion = models.CharField(
        max_length= 100,
        help_text= 'Descripcion de la Categoría'
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.description,self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Subcategoria, self).save()

    class Meta:
        verbose_name_plural="Subcategorias"
        #evita que existan dos subcategorias identicas por cada categoria
        unique_together = ('categoria','descripcion')
