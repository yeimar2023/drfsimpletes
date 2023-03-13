from django.db import models

# Create your models here.

#codigo  para añadir una tabla en la base de datos que este conecntada.
class Project(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField()
    technology = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True) #para cargar la hora y fecha de creacion automaticamente.
