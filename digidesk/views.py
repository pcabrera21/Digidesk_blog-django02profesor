from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Digimon

# Create your views here.
def index(request):
  digimons = Digimon.objects.all()

  context = {
    'digis': digimons
  }
  
  return render(request, 'index.html', context)

@csrf_exempt
def create(request):
  # peticiones/verbo tipo mas usuales: GET, POST, PUT, DELETE
  #GET: conectar
  #POST: Crear registro
  #PUT: actualizar datos
  #DELETE: eliminar datos
  # tabien existen: HEAD (verificacion) OPTION PATHS
  params = request.POST #aun no guarda en BD
  digi = Digimon()
  digi.name = params["name"]
  digi.level = params["level"]
  digi.img = params["img"]
  digi.save() #guarda en la BD
  return HttpResponse(status = 200)