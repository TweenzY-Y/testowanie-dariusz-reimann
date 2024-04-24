from django.shortcuts import render
from django.views.generic.detail import DetailView
from salonsamochodowyapp.models import ListCars
# Create your views here.

def home(request):
    return render(request, 'home.html')

class CarDetailView(DetailView):
    model = ListCars
    template_name = 'salonsamochodowyapp/templates/car_detail.html'
    context_object_name = 'car'