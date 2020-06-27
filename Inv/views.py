from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Categoria, Subcategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubcategoriaForm, MarcaForm, UnidadMedidaForm, ProductoForm

#Views de categoria
class CategoriaView (LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class CategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    login_url= "bases:login"

#se sobreescribe el metodo para obtener el usuario que esta creando el registro
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    login_url= "bases:login"

#se sobreescribe el metodo para obtener el usuario que esta editando el registro
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name ='inv/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inv:categoria_list")


#Views de subcategoria
class SubcategoriaView (LoginRequiredMixin, generic.ListView):
    model = Subcategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class SubcategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = Subcategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubcategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url= "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SubcategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Subcategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubcategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url= "bases:login"

#se sobreescribe el metodo para obtener el usuario que esta editando el registro
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class SubcategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = Subcategoria
    template_name ='inv/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inv:subcategoria_list")

#Views de marca
class MarcaView (LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class MarcaNew(LoginRequiredMixin, generic.CreateView):
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    login_url= "bases:login"

#se sobreescribe el metodo para obtener el usuario que esta creando el registro
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    login_url= "bases:login"

#se sobreescribe el metodo para obtener el usuario que esta editando el registro
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
        
def marca_inactivar (request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not marca:
        return redirect("inv:marca_list")

    if request.method == 'GET':
        contexto = {'obj':marca}
    
    if request.method == 'POST':
        marca.estado=False
        marca.save()
        return redirect("inv:marca_list")

    return render(request, template_name, contexto)
        
#Views de unidad de medida
class UnidadMedidaView (LoginRequiredMixin, generic.ListView):
    model = UnidadMedida
    template_name = "inv/unidadMedida_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class UnidadMedidaNew(LoginRequiredMixin, generic.CreateView):
    model = UnidadMedida
    template_name = "inv/unidadMedida_form.html"
    context_object_name = "obj"
    form_class = UnidadMedidaForm
    success_url = reverse_lazy("inv:unidadMedida_list")
    login_url= "bases:login"

#se sobreescribe el metodo para obtener el usuario que esta creando el registro
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class UnidadMedidaEdit(LoginRequiredMixin, generic.UpdateView):
    model = UnidadMedida
    template_name = "inv/unidadMedida_form.html"
    context_object_name = "obj"
    form_class = UnidadMedidaForm
    success_url = reverse_lazy("inv:unidadMedida_list")
    login_url= "bases:login"

#se sobreescribe el metodo para obtener el usuario que esta editando el registro
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
        
def unidadMedida_inactivar (request, id):
    um = UnidadMedida.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not um:
        return redirect("inv:unidadMedida_list")

    if request.method == 'GET':
        contexto = {'obj':um}
    
    if request.method == 'POST':
        um.estado=False
        um.save()
        return redirect("inv:unidadMedida_list")

    return render(request, template_name, contexto)

#Views de producto
class ProductoView (LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class ProductoNew(LoginRequiredMixin, generic.CreateView):
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    login_url= "bases:login"

#se sobreescribe el metodo para obtener el usuario que esta creando el registro
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class ProductoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    login_url= "bases:login"

#se sobreescribe el metodo para obtener el usuario que esta editando el registro
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
        
def producto_inactivar (request, id):
    prod = Producto.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not prod:
        return redirect("inv:producto_list")

    if request.method == 'GET':
        contexto = {'obj':prod}
    
    if request.method == 'POST':
        prod.estado=False
        prod.save()
        return redirect("inv:producto_list")

    return render(request, template_name, contexto)