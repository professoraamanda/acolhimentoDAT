from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.urls import reverse

# Create your models here.
class Denuncia(models.Model):
    id_denuncia = ShortUUIDField(
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
    denuncia=models.TextField("Compartilhe a ocorrência", max_length=1000, help_text="Deixe um comentário sobre o ocorrido!")
    dataDaDenuncia = models.DateField("Data da ocorrência", null = True, blank=True)

    LOAN_STATUS = (
        ('c', 'Concluido'),
        ('a', 'Em aberto'),
        ('p', "Em progresso"),
    )
    status = models.CharField(
        max_length=1,
        choices = LOAN_STATUS,
        blank=True,
        default='a',
        help_text="Status da ocorrência!",
    )

    class Meta:
        ordering = ['id_denuncia', 'tipoDeOcorrencia', 'denuncia', 'dataDaDenuncia', 'status']

    def __str__(self):
        return f'{self.id_denuncia}: {self.tipoDeOcorrencia} ({self.denuncia})'
    
    def get_absolute_url(self):
        return reverse('Detalhes da ocorrência', args=[str(self.id)])
    
class Advogado(models.Model):
    OAB = models.CharField("OAB", max_length=10)
    nome = models.CharField('Nome', max_length=10, help_text="Primeiro nome")
    sobrenome = models.CharField('Sobrenome', max_length=10, help_text="Ultimo nome")
    contato = models.CharField("Telefone", max_length=11, help_text="Telefone para contato")
    #id_denuncia = models.ManyToManyField('Denuncia', on_delete=models.SET_NULL, null=True, help_text='senha de acesso a denuncia')

    class Meta:
        ordering = ['OAB', 'nome', 'sobrenome']

    def __str__(self):
        return f'{self.nome} {self.sobrenome} - {self.contato}'
    
    def get_absolute_url(self):
        return reverse('Detalhes do cadastro', args=[str(self.id)])


    

    
    
