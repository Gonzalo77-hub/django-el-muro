from django.urls import path
from . import views, auth
urlpatterns = [
    path('', views.index),
    path('Wall', views.muro),
    path('mensajes', views.mensaje),
    path('registro/', auth.registro),
    path('login/', auth.login),
    path('logout/', auth.logout),
    path('comentarios', views.comentario),
    path('borrar/<int:id>', views.borrar),
]
