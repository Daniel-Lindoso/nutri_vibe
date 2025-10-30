from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NutricionistaForm, PacienteForm
from django.contrib.auth.decorators import login_required # Temporário


# Create your views here.
# View para cadastrar nutricionistas
def cadastrar_nutricionista(request):
    if request.method == 'POST':
        form = NutricionistaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Nutricionista cadastrado com sucesso!")
            return redirect('cadastrar_nutricionista')  # redireciona pra mesma página
    else:
        form = NutricionistaForm()
    return render(request, 'sistema/cadastrar_nutricionista.html', {'form': form})


# View para cadastrar pacientes
def cadastrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Paciente cadastrado com sucesso!")
            return redirect('cadastrar_paciente')
    else:
        form = PacienteForm()
    return render(request, 'sistema/cadastrar_paciente.html', {'form': form})

# Temporário
@login_required
def home(request):
    return render(request, 'sistema/home.html')