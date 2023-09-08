from django.http import HttpResponse
from django.shortcuts import redirect
import os

def saludo(request):
    mensaje = "Hola Fulano"
    return HttpResponse(mensaje)

def get_google(request):
    return redirect("https://www.google.com.py")

def get_fibonacci(request):
    a, b = 0, 1
    r = []
    n = 100
    while(b<n):
        r.append(b)
        a,b=b, a+b

    return HttpResponse(r)

def apagar(request):
    os.system("shutdown -s -t 60")
