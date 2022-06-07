from email import message
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.


def index(request):

    return render(request, 'flores/index.html')


def productos(request):

    return render(request, 'flores/productos.html')


def quienes(request):

    return render(request, 'flores/quienessomos.html')


def registro(request):

    return render(request, 'flores/registro.html')


def fundacion(request):

    return render(request, 'flores/fundacion.html')


def registro(request):

    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registrado correctamente")
            return redirect(to="index")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)
