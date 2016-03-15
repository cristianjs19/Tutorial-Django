from django.http import Http404,HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
import datetime

def hola(request):
  return HttpResponse("Hola Mundo!!!")

def fecha_actual(request):
	ahora = datetime.datetime.now()
	return render(request, 'fecha_actual2.html', {'fecha_actual': ahora})

def horas_adelante (request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt= datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render(request, 'horas_adelante.html', {'hora_siguiente': dt, 'horas': offset })


   
