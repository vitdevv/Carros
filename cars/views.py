from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm

def cars_view(request):
    cars = Car.objects.all() #.order_by('-model') # Access the Car model to ensure it's loaded, from ORM Django
    search = request.GET.get('search')
    if search:
        cars = cars.filter(model__icontains=search)
    # cars = Car.objects.filter(model__contains='Hyundai')
    # print(cars)
    
    return render(
        request,
        'cars.html',
        {'cars': cars }
    )
    
def car_details(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, "details.html", {"car": car})

def new_car_view(request):
    if request.method == "POST":
        new_car_form = CarForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarForm()
    return render(request, "new_car.html", {"new_car_form": new_car_form})