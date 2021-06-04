from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Criando sua views aqui.

def hello(resquest, nome, idade):
    return HttpResponse('<h1>Seja bem vindo {}, sua idade é {}</h1>'.format(nome, idade))

# Calcular.

def soma(resquest, numero1, numero2, resultado):
    resultado = numero1 + numero2
    return HttpResponse('<h1>Vamos somar {} + {} = {}</h1>'.format(numero1,numero2,resultado))


# def mu(request, n1, n2, res):
#     res = n1 * n2
#     return HttpResponse('<h1>Vamos multiplicar {} x {} = {}</h1>'.format(n1,n2,res))


# criando uma função para chamar o hello.

# def hello(resquest):
#     return HttpResponse('<h1>Seja bem vindo.</h1>')    