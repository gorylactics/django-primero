from django.shortcuts import render , HttpResponse , redirect
from django.http import JsonResponse

def root(request):
    return redirect('/blogs')
    # return HttpResponse('holaMundo')
def index(request):
    return HttpResponse('<h1>placeholder para luego mostrar una lista de todos los blogs</h1>')

def new(request):
    return HttpResponse('placeholder para mostrar un nuevo formulario para crear un nuevo blog')

def create(request):
    # return redirect('/')
    return redirect(root)

def show(request, numero):
    return HttpResponse(f'placeholder para mostrar el blog numero {numero}')

def edit(request, numero):
    return HttpResponse(f'placeholder para editar el blog {numero}" con un método llamado')

def destroy(request, numero):
    return redirect('/blogs')

def json(request):
    response = JsonResponse({'Adrian': 'Cito'})
    return response