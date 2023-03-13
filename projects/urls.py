#par crear las rutas que el cliente pueda consultar desde las herramientas que tiene rest_framework, crea las rutas basiscas o lo que se le conoce como el crud.
from rest_framework import routers
from .api import ProjectViewSet 

router = routers.DefaultRouter() #para ejcutar el modelo y crea el crud.
router.register('api/projects',ProjectViewSet, 'projects') #registras la ruta ,luego se le indica que estara basado en el conjunto de datos ProjectViewSet  y se guido el nombre de la ruta.

urlpatterns = router.urls #para que genere las url 