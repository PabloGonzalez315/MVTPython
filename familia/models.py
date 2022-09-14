from django.db import models

# Create your models here.
class Integrante(models.Model):
    nombre= models.CharField(max_length=15)
    apellido= models.CharField(max_length=15)
    edad= models.IntegerField()
    fecha_nacimiento= models.DateField()
    
    def __str__(self):
        return self.nombre, self.edad