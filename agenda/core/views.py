from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.


def eventos(request, titulo_evento):
    titulo = Evento.objects.get(titulo=titulo_evento)
    frase = f'Esse é o titulo do evento ', titulo
    return HttpResponse(frase)


def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
