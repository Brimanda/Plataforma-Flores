from django.urls import path 
from .views import index, productos, quienes, fundacion, registro

urlpatterns = [
    path('', index, name='index'),
    path('productos', productos, name='productos'),
    path('quienessomos', quienes, name='quienessomos'),
    path('fundacion', fundacion, name='fundacion'),
    path('registro/', registro, name='registro'),


]