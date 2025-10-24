from django.contrib import admin
from .models import Nutricionista, Paciente

# Register your models here.
# Configuração simples para exibir campos úteis na listagem do admin
@admin.register(Nutricionista)
class NutricionistaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crn', 'email', 'telefone', 'created_at')
    search_fields = ('nome', 'crn', 'email')
    list_filter = ('especialidade',)
    ordering = ('nome',)
    # fields/readonly_fields podem ser adicionados se quiser controlar edição

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'responsavel', 'idade', 'nutricionista', 'created_at')
    search_fields = ('nome', 'responsavel', 'diagnostico_tea')
    list_filter = ('diagnostico_tea',)
    ordering = ('-created_at',)