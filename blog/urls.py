

from django.urls import path
from .views import blog, detallesPost, registro, crearPost, mostrarinicio, editarAutor, eliminarPost, salir

urlpatterns = [
     path('blog', blog, name='blog'),
     path('detpost/<int:id>/', detallesPost, name='detpost'),
     path('registration/registro', registro, name='registro'),
     path('crearpost', crearPost, name='crearpost'),
     path('', mostrarinicio, name='inicio'),
     path('editarPost/<int:id>', editarAutor, name='editarPost'),
     path('eliminarPost/<int:id>', eliminarPost, name='eliminarPost'),
     path('logout/', salir, name='salir')

]
