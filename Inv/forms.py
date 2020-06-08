from django import forms

from .models import Categoria, Subcategoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripción de la Categoría",
                  'estado': "Estado"}
        
        widget={'descripcion':forms.TextInput}

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class SubcategoriaForm(forms.ModelForm):
    #sobreescribimos para mostrar solo las categorias activas y ordenadas
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter (estado=True)
        .order_by('descripcion')
    )
    class Meta:
        model = Subcategoria
        fields = ['categoria','descripcion', 'estado']
        labels = {'descripcion': "SubcCategoría",
                  'estado': "Estado"}
        
        widget={'descripcion':forms.TextInput}

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['categoria'].empty_label = "Seleccione Categoría" 