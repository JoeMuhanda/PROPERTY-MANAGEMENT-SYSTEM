# property_management_system/models.py

from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=50)

class Unit(models.Model):
    number = models.CharField(max_length=10)
    size = models.IntegerField()
    rent = models.FloatField()
    deposit = models.FloatField()
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='units')
    tenant = models.ForeignKey('Tenant', on_delete=models.SET_NULL, null=True, blank=True)

class Tenant(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    emergency_contact = models.CharField(max_length=50)
    lease_start = models.DateField()
    lease_end = models.DateField()
    unit = models.OneToOneField(Unit, on_delete=models.SET_NULL, null=True, blank=True)

# property_management_system/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Property, Unit, Tenant

def home(request):
    properties = Property.objects.all()
    return render(request, 'home.html', {'properties': properties})

def add_property(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        owner_name = request.POST.get('owner_name')
        property = Property(name=name, address=address, owner_name=owner_name)
        property.save()
        return redirect('home')
    else:
        return render(request, 'add_property.html')

def view_property(request, id):
    property = get_object_or_404(Property, id=id)
    return render(request, 'view_property.html', {'property': property})

def add_unit(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        size = request.POST.get('size')
        rent = request.POST.get('rent')
        deposit = request.POST.get('deposit')
        property_id = request.POST.get('property')
        unit = Unit(number=number, size=size, rent=rent, deposit=deposit, property_id=property_id)
        unit.save()
        return redirect('home')
    else:
        properties = Property.objects.all()
        return render(request, 'add_unit.html', {'properties': properties})

def view_unit(request, id):
    unit = get_object_or_404(Unit, id=id)
    return render(request, 'view_unit.html', {'unit': unit})

# property_management_system/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_property/', views.add_property, name='add_property'),
    path('view_property/<int:id>/', views.view_property, name='view_property'),
    path('add_unit/', views.add_unit, name='add_unit'),
    path('view_unit/<int:id>/', views.view_unit, name='view_unit'),
]

# property_management_system/settings.py

# Add the following lines to the bottom of the file

INSTALLED_APPS = [
    # ... other apps ...
    'property_management_system',
]

# property_management_system/templates/*.html

<!-- home.html -->
{% for property in properties %}
  <h2>{{ property.name }}</h2>
  <p>{{ property.address }}</p>
  <p>{{ property.owner_name }}</p>
  <a href="{% url 'view_property' property.id %}">View Property</a>
{% endfor %}

<!-- add
