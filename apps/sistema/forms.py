from django import forms
from .models import Nutricionista, Paciente

# Formulário para cadastrar e editar Nutricionistas
class NutricionistaForm(forms.ModelForm):
    class Meta:
        model = Nutricionista  # modelo que o formulário representa
        fields = ['nome', 'email', 'telefone', 'crn', 'especialidade']
        labels = {
            'nome': 'Nome completo',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'crn': 'Registro CRN',
            'especialidade': 'Especialidade',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'crn': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidade': forms.TextInput(attrs={'class': 'form-control'}),
        }


# Formulário para cadastrar e editar Pacientes
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nome', 'idade', 'responsavel',
            'contato_responsavel', 'diagnostico_tea',
            'tipos_alimento', 'observacoes', 'nutricionista'
        ]
        labels = {
            'nome': 'Nome do paciente',
            'idade': 'Idade',
            'responsavel': 'Responsável',
            'contato_responsavel': 'Contato',
            'diagnostico_tea': 'Diagnóstico (TEA)',
            'tipos_alimento': 'Tipos de alimentos que consome',
            'observacoes': 'Observações',
            'nutricionista': 'Nutricionista responsável',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'contato_responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'diagnostico_tea': forms.TextInput(attrs={'class': 'form-control'}),
            'tipos_alimento': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'nutricionista': forms.Select(attrs={'class': 'form-select'}),
        }