from django.shortcuts import render
from django.http import HttpResponse

def formulario_buscar(request):
	return render(request, 'formulario_buscar.html')

def buscar(request):
	if 'q' in request.GET and request.GET['q']:
		mensaje = 'Estas buscando: %r' % request.GET['q']
	else:
		mensaje = 'Haz subido un formulario vacio.'
	return HttpResponse(mensaje)