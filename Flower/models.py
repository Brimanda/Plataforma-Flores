from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombreCategoria = models.CharField(
        primary_key=True, max_length=50, verbose_name='Nombre Categoria')

    def __str__(self):
        return self.nombreCategoria


class Flor(models.Model):
    idFlor = models.IntegerField(primary_key=True, verbose_name='Id Flor')
    nombreFlor = models.CharField(max_length=20, verbose_name='Nombre Flor')
    descFlor = models.CharField(max_length=50, verbose_name='Descripción')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.idFlor
