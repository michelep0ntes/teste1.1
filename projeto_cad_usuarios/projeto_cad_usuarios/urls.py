
from django.urls import path
from django.contrib import admin
from app_cad_usuarios.views import home
urlpatterns = [
    path("admin/", admin.site.urls),
    # rota, viewnresponsável, nome de referência
    #usuarios.com
    path('', home , name='home'),
    #usuarios.com/usuarios
   
]
