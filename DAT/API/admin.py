from django.contrib import admin
from .models import Advogado, RegistroDeOcorrencia

# Register your models here.
#admin.site.register(Denuncia)
@admin.register(RegistroDeOcorrencia)
class RegistroDeOcorrenciaAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)  # Define 'id' como campo de somente leitura
    list_display = ('id', 'tipoDeOcorrencia', 'registroDeCaso', 'dataDaDenuncia', 'status', )  # Certifique-se de incluir 'id' aqui se quiser exibi-lo na lista

    # Define a ordem dos campos no formulário de administração
    list_filter = ('tipoDeOcorrencia','status',)
    fieldsets = ( (None, {
            'fields': ('id','tipoDeOcorrencia','registroDeCaso', 'dataDaDenuncia', 'status')}),
    )

@admin.register(Advogado)
class AdvogadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'OAB', 'email', 'display_registros_de_ocorrencia')
