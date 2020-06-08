from django.urls import path
from .views import CategoriaView, CategoriaNew, CategoriaEdit, \
    CategoriaDel, \
        SubcategoriaView, SubcategoriaNew, SubcategoriaEdit, SubcategoriaDel

urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new', CategoriaNew.as_view(), name = 'categoria_new'),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name = 'categoria_edit'),
    path('categorias/delete/<int:pk>', CategoriaDel.as_view(), name = 'categoria_del'),
    
    path('subcategorias/', SubcategoriaView.as_view(), name='subcategoria_list'),
    path('subcategorias/new', SubcategoriaNew.as_view(), name = 'subcategoria_new'),
    path('subcategorias/edit/<int:pk>', SubcategoriaEdit.as_view(), name = 'subcategoria_edit'),
    path('subcategorias/delete/<int:pk>', SubcategoriaDel.as_view(), name = 'subcategoria_del'),
]