from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

# Create your views here.

def home(request):
    todo_objs = Todo.objects.all() #data liyera aako database bata
    data = {'todos': todo_objs} #dict banako data lyauna lai cuz data aauda list ma aako huncha, frontend ma pathako data lai
    return render(request, 'index.html', context=data) #context le chai index.html ma data pathauxa


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')

        Todo.objects.create(name=name,description=description,status=status) #create is method for creating value in create file

        return redirect('home')


    return render(request, 'create.html')


def edit(request):
    return render(request, 'edit.html')


