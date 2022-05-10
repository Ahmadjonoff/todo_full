from django.shortcuts import render, redirect
from .models import *

def home(request):
    if request.method == 'POST':
        TODO.objects.create(
            title = request.POST['t'],
            time = request.POST['v'],
            description = request.POST['d'],
            status = request.POST['s'],
        )
        return redirect('/')

    p = TODO.objects.all()
    return render(request, 'todo.html', {'todos' : p})

def delete(request, pk):
    TODO.objects.get(id = pk).delete()
    return redirect('/')

def edit(request, pk):
    p = TODO.objects.get(id=pk)
    if request.method == 'POST':
        p.title = request.POST['t']
        p.time = request.POST['v']
        p.description = request.POST['d']
        p.status = request.POST['s']
        p.save()
        return redirect('/')

    return render(request, 'edit.html', {'plan' : p})