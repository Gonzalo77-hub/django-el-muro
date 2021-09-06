from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required
from .models import *
from datetime import datetime, date
from django.utils.timezone import localtime



@login_required
def index(request):

    context = {
        'saludo': 'Hola'
    }
    return render(request, 'index.html', context)

def muro(request):

    context = {'mensajes': Message.objects.all(),
                'comentarios': Comment.objects.all(),
                'usuarios':User.objects.all(),
                }
    return render(request, 'muro.html', context)

def mensaje(request):
    
    mensaje = Message.objects.create(message=request.POST['messag'],
                                    user=User.objects.get(id=request.session['usuario']['id'])
            )
    return redirect("/Wall")

def comentario(request):
    print(request.session['usuario']['id'])
    comentarios = Comment.objects.create(comment=request.POST['commen'],
                                        user_c=User.objects.get(id=request.session['usuario']['id'] ),
                                        message=Message.objects.get(id=request.POST['mensaje_id']))
    return redirect('/Wall')

def borrar(request, id):

    a = Comment.objects.get(id=id)
    hora_actual =datetime.now()
    hora_1 = localtime(a.created_at)
    print(hora_actual)
    print(hora_1)
    resultado = (hora_actual.minute - hora_1.minute)
    print(resultado)
    minutos = (resultado *60)
    print(minutos)
    if minutos <= 30:
        a.delete()
        messages.success(request,"Comentario borrado correctamente")
        return redirect("/Wall")
    else:
        messages.error(request,"El comentario no se puede borrar ya que han pasado mas de 30 min desde que se creo")
        return redirect("/Wall") 