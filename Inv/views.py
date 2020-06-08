from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Categoria, Subcategoria
from .forms import CategoriaForm, SubcategoriaForm


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
