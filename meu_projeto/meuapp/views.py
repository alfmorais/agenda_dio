from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse('Hello World')


def soma(request, n1, n2):
    soma = n1 + n2
    frase = f'A soma dos números ', n1, ' + ', n2, ' = ', soma
    return HttpResponse(frase)


def sub(request, n1, n2):
    sub = n1 - n2
    frase = f'A subtração dos números ', n1, ' - ', n2, ' = ', sub
    return HttpResponse(frase)


def mult(request, n1, n2):
    mult = n1 * n2
    frase = f'A multiplicação dos números ', n1, ' * ', n2, ' = ', mult
    return HttpResponse(frase)


def divi(request, n1, n2):
    try:
        divi = n1 / n2
        frase = f'A divisão dos números ', n1, ' / ', n2, ' = ', divi
        return HttpResponse(frase)
    except ZeroDivisionError:
        frase = 'Divisão por zero não é possivel'
        return HttpResponse(frase)
