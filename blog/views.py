from django.shortcuts import render, redirect
from .forms import blogForm
from blog.models import Blog
from django.core.exceptions import ObjectDoesNotExist
from .forms import loginForm
from .forms import registroForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q



# Create your views here.




def blog(request):
    queryset = request.GET.get("buscar")
    post = Blog.objects.all()
    print(post)
    if queryset:
        post = Blog.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(subtitulo__icontains = queryset)
        ).distinct()
    return render(request, 'blog.html', {'post': post})



@login_required
def detallesPost(request,id):
    detpost = Blog.objects.get(id=id)
    return render(request, 'post-details.html', {'detpost': detpost})


@login_required
def crearPost(request):
    if request.method == 'POST':
        publicacion = blogForm(request.POST, request.FILES)
        print(Blog.objects.all())
        if publicacion.is_valid():
            publicacion.save()
            messages.success(request, 'Publicacion exitosa')
            return redirect('inicio')
    else:
        publicacion = blogForm()
    return render(request, 'crearPost.html', {'post': publicacion})
    



def mostrarinicio(request):
    post = Blog.objects.all()
    print(post)
    return render(request, 'index.html', {'post': post})


@login_required
def editarAutor(request, id):
    error = None
    editar = None
    try:
        id = Blog.objects.get(id = id)
        print(id)
        if request.method == 'POST':
            editar= blogForm(request.POST,request.FILES, instance= id)
            if editar.is_valid():
                editar.save()
            return redirect('blog')
        else:
            editar= blogForm(instance= id)
    except ObjectDoesNotExist as e:
        error = e
        
    return render(request, 'editarPost.html', {'editar': editar, 'error': error})


@login_required
def eliminarPost(request, id):
    eliminar = Blog.objects.get(id = id)
    datos = Blog.objects.all()
    if request.method == 'GET':
        eliminar.delete()
        messages.success(request, 'Post Eliminado')
        return render(request, 'blog.html', {'post':datos})



def iniciarSesion(request):
    login = loginForm(request, request.POST)
    return render(request, 'login.html', {'form':login})




def registro(request):
    if request.method == 'POST':
        registros = registroForm(data = request.POST)
        if registros.is_valid():
            usuarios = registros.save()
            usuario = authenticate(request, username=registros.cleaned_data['username'], password=registros.cleaned_data['password1'])
            login(request, usuario)
            messages.success(request, 'Usuario Registrado')
            return redirect('blog')
    else:
        registros = registroForm()
    return render(request, 'registration/registro.html', {'datos': registros})



def salir(request):
    logout(request)
    return redirect('inicio')