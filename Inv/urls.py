from django.urls import path
from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDel, \
        SubcategoriaView, SubcategoriaNew, SubcategoriaEdit, SubcategoriaDel, \
        MarcaView,MarcaNew, MarcaEdit, marca_inactivar,\
        UnidadMedidaView, UnidadMedidaNew, UnidadMedidaEdit, unidadMedida_inactivar,\
        ProductoView, ProductoNew, ProductoEdit, producto_inactivar


urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new', CategoriaNew.as_view(), name = 'categoria_new'),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name = 'categoria_edit'),
    path('categorias/delete/<int:pk>', CategoriaDel.as_view(), name = 'categoria_del'),
    
    path('subcategorias/', SubcategoriaView.as_view(), name='subcategoria_list'),
    path('subcategorias/new', SubcategoriaNew.as_view(), name = 'subcategoria_new'),
    path('subcategorias/edit/<int:pk>', SubcategoriaEdit.as_view(), name = 'subcategoria_edit'),
    path('subcategorias/delete/<int:pk>', SubcategoriaDel.as_view(), name = 'subcategoria_del'),

    path('marca/', MarcaView.as_view(), name='marca_list'),
    path('marca/new', MarcaNew.as_view(), name = 'marca_new'),
    path('marca/edit/<int:pk>', MarcaEdit.as_view(), name = 'marca_edit'),
    path('marca/inactivar/<int:id>', marca_inactivar, name = 'marca_inactivar'),

    path('unidad/', UnidadMedidaView.as_view(), name='unidadMedida_list'),
    path('unidad/new', UnidadMedidaNew.as_view(), name = 'unidadMedida_new'),
    path('unidad/edit/<int:pk>', UnidadMedidaEdit.as_view(), name = 'unidadMedida_edit'),
    path('unidad/inactivar/<int:id>', unidadMedida_inactivar, name = 'unidadMedida_inactivar'),

    path('producto/', ProductoView.as_view(), name='producto_list'),
    path('producto/new', ProductoNew.as_view(), name = 'producto_new'),
    path('producto/edit/<int:pk>', ProductoEdit.as_view(), name = 'producto_edit'),
    path('producto/inactivar/<int:id>', producto_inactivar, name = 'producto_inactivar'),
]