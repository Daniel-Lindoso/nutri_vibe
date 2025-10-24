from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Modelo que representa um nutricionista (ou médico de nutrição)
class Nutricionista(models.Model):
    # opcional: vincular a uma conta de usuário do Django (se quiser permitir login por nutricionista)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    nome = models.CharField("Nome completo", max_length=150)
    email = models.EmailField("Email", unique=True)
    telefone = models.CharField("Telefone", max_length=30, blank=True)
    crn = models.CharField("CRN/Registro", max_length=50, unique=True)
    especialidade = models.CharField("Especialidade", max_length=150, blank=True)
    created_at = models.DateTimeField("Data de cadastro", auto_now_add=True)

    class Meta:
        verbose_name = "Nutricionista"
        verbose_name_plural = "Nutricionistas"
        ordering = ['nome']  # ordena por nome por padrão

    def __str__(self):
        # como o objeto será exibido, por exemplo no admin
        return f"{self.nome} ({self.crn})"


# Modelo que representa um paciente
class Paciente(models.Model):
    nome = models.CharField("Nome do paciente", max_length=150)
    data_nascimento = models.DateField("Data de nascimento", null=True, blank=True)
    idade = models.PositiveIntegerField("Idade", null=True, blank=True)
    responsavel = models.CharField("Responsável", max_length=150, blank=True)
    contato_responsavel = models.CharField("Contato do responsável", max_length=50, blank=True)
    diagnostico_tea = models.CharField("Diagnóstico (TEA)", max_length=150, blank=True)
    tipos_alimento = models.TextField("Tipos de alimento que já come", blank=True)
    observacoes = models.TextField("Observações clínicas", blank=True)
    # relação com nutricionista (opcional): se o nutricionista for apagado, paciente fica com null
    nutricionista = models.ForeignKey(Nutricionista, on_delete=models.SET_NULL, null=True, blank=True, related_name='pacientes')
    created_at = models.DateTimeField("Criado em", auto_now_add=True)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ['-created_at']  # mais recentes primeiro

    def __str__(self):
        return f"{self.nome} — {self.responsavel or 'sem responsável'}"