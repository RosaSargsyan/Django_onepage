from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def index(request):
    home_list = Home.objects.all()[0]
    about_list = About.objects.all()[0]
    proj_list = Proj.objects.all()
    logo = Logo.objects.all()[0]
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        return redirect('index')
    return render(request, 'main/index.html', context={
        'home_list': home_list,
        'about_list' : about_list,
        'proj_list' : proj_list,
        'logo': logo
    })

