#se le conoce como el wiutsed.desde aqui nos permite establcer quien puede consultar en nuestro modelo o base de datos
#es decir, para establecer que peticiones se pueden hacer. saber si tenemos que enviar una serie de autenticacion de usuario.
from .models import Project #importamos desde model.py la clase que se creo llamda Project
from rest_framework import viewsets, permissions #se importa los permisos 
from .serializers import ProjectSerializer 

#para poder decir que consultas se van  a poder realizar
class ProjectViewSet(viewsets.ModelViewSet): 
    queryset = Project.objects.all() #conjunto de datos...consulta todos los datos de una tabla.
    permission_classes=[permissions.AllowAny] #establece los permisos, AllowAny quiere decir que cualquier aplicacion o cliente puede solictar datos a el servidor... IsAuthenticated para comprobar si esta autenticado. 
    serializer_class = ProjectSerializer # para indicarle de que serializer va a estar utilizando los datos.

 