from django.shortcuts import render,redirect
import requests
from W_app.models import Student


# Create your views here.

# def home(request):
#     if request.method == 'POST':
#         city = request.POST['city']
#         url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e1b0c38d394d992c06d331ce329389fa'

#         response = requests.get(url)
#         weather_data = response.json()
#         city_update = {
#             'City': city,
#             'temperature' : int((weather_data['main']['temp'])-273.15),
#             'wind': weather_data['wind']['speed']
#         }
#         return render(request,'index.html',{'city_update':city_update})
#     else:
#         city_update=''
#         return render(request,'index.html',{'city_update':city_update})
    
def static(request):
    if request.method == 'POST':
        name = request.POST['name']
        roll = request.POST['roll']
        email = request.POST['email']
        phone = request.POST['phone']
        pwd = request.POST['pass']

        stud = Student(name=name,roll=roll,email=email,mob=phone,pwd=pwd)
        stud.save()

    return render(request,'static.html')
def display(request):
    ob = Student.objects.all()
    return render(request,'display.html',{'ob':ob})

def discard(request,roll):
    ob = Student.objects.get(roll = roll)
    ob.delete()
    return redirect('/display')

def edit(request,roll):
    task = Student.objects.get(roll=roll)
    return render(request,'edit.html',{'task':task})

def update(request,roll):
    task = Student.objects.get(roll = roll)
    task.name = request.POST['name']
    task.roll = request.POST['roll']
    task.email = request.POST['email']
    task.mob = request.POST['phone']
    task.save()
    return redirect('/display')


