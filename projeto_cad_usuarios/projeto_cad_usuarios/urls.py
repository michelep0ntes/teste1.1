
from django.urls import path
from app_cad_usuarios.views import home
urlpatterns = [
    # rota, viewnresponsável, nome de referência
    #usuarios.com
    path('', home , name='home'),
    #usuarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
