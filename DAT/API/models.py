from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.urls import reverse
#from django.contrib.auth.models import User

# Create your models here.
class RegistroDeOcorrencia(models.Model):
    id = ShortUUIDField(
        'Senha',
        length=5,
        max_length=7,
        prefix='01',
        alphabet="abcdefghijklmnopqrstuvwxyz0123456789",
        primary_key=True,
        editable=False,
    )
    LOAN_STATUS = (
        ('s', 'Assédio Sexual'),
        ('m', 'Assédio Moral'),
    )
    tipoDeOcorrencia = models.CharField(
        'Tipo de Ocorrência',
        max_length=1,
        choices = LOAN_STATUS,
        blank=True,
        default='m',
        help_text="Tipo de ocorrência!",
    )
    registroDeCaso=models.TextField("Registro de ocorrência", max_length=1000, help_text="Registre a ocorrência, que direcionaremos para um advogado!")
    dataDaDenuncia = models.DateField("Data da ocorrência", null = True, blank=True)

    LOAN_STATUS = (
        ('Concluido', 'Concluido'),
        ('Em aberto', 'Em aberto'),
        ("Em progresso", "Em progresso"),
    )
    status = models.CharField(
        max_length=50,
        choices = LOAN_STATUS,
        blank=True,
        default='Em aberto',
        help_text="Status da ocorrência!",
    )

    #o advogado consegue registrar uma ocorrência
    advogado = models.ForeignKey('API.Advogado', on_delete=models.SET_NULL, null=True,  related_name='registros_de_ocorrencias')

    class Meta:
        ordering = ['id', 'tipoDeOcorrencia', 'registroDeCaso', 'dataDaDenuncia', 'status']

    def __str__(self):
        return f'senha: {self.id}, status da ocorrencia: {self.status}'
    
    def get_absolute_url(self):
        return reverse('Detalhes da ocorrência', args=[str(self.id)])
    
class Advogado(models.Model):
    OAB = models.CharField("OAB", max_length=10)
    nome = models.CharField('Nome', max_length=10, help_text="Primeiro nome")
    sobrenome = models.CharField('Sobrenome', max_length=10, help_text="Ultimo nome")
    email = models.EmailField("E-mail", max_length=200, default='default@example.com', unique=True, help_text="Email para contato e acesso ao sistema")
    #user = models.OneToOneField(User, on_delete=models.CASCADE, default=1) #advogado com permissões de superusuário
    #registros de ocorrências vinculads com advogados
    registros_de_ocorrencia = models.ManyToManyField(RegistroDeOcorrencia, related_name='advogados', blank=True)

    #listando todas as ocorrências para o advogado pelo id delas
    def display_registros_de_ocorrencia(self):
        return ', '.join(registros_de_ocorrencia.id for registros_de_ocorrencia in self.registros_de_ocorrencia.all())
    display_registros_de_ocorrencia.short_description = 'Ocorrências'

    class Meta:
        ordering = ['OAB', 'nome', 'sobrenome', 'email']

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
    def get_absolute_url(self):
        return reverse('Detalhes do cadastro', args=[str(self.id)])


    

    
    
