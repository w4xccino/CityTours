from django.shortcuts import render
from .models import Lugar

# Create your views here.
def index(request):
  print("index gaaa")
  return render(request, "Turismo/index.html")

def base (request):
  return render(request, "Turismo/base.html" )

def lugares(request):

  cards = Lugar.objects.all()
  context = {'cards':cards}
  return render(request, "Turismo/lugares.html", context)
