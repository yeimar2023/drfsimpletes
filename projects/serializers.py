from rest_framework import serializers  #importamos los serializadores Los serializadores permiten convertir datos complejos , como conjuntos de consultas e instancias de modelos, en tipos de datos nativos de Python que luego se pueden representar fácilmente en correo electrónico XMLu otros tipos de contenido.

from .models import Project # para que django sepa que va a responder cuando se haga una peticion post,get putch o delete.

class ProjectSerializer(serializers.ModelSerializer): # permite convertir el modelo en datos que pueden ser consultados.
    class Meta:
        model = Project #este es el nombre de mi modelo que se creo en el archivo model.py
        fields = ('id','title','description','technology','fecha') #esto es para los campos que van a ser consultados de mi modelo. el id se crea por defecto 
        read_only_fields = ('fecha', ) # para decirle que este campo de mi modelo es solo lectura. no se puede eliminar ni modificar. 