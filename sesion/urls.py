from django.urls import path
from .views import index, crear_usuario, inicio_sesion, cerrar_sesion

urlpatterns = [

  # Página principal
  path('', index, name='index'),

  # Inicio de sesión & creación de usuario.
  path('login/',inicio_sesion, name="login"),

  # Creación de usuario.
  path('crear_usuario/',crear_usuario, name="crear_usuario"),

  # Cierre de sesión
  path('logout/',cerrar_sesion, name="logout")

]
