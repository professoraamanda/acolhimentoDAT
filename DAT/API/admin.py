from django.contrib import admin
from .models import Denuncia, Advogado

# Register your models here.
#admin.site.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    readonly_fields = ('id_denuncia',)  # Define 'id' como campo de somente leitura
    list_display = ('id_denuncia', 'tipoDeOcorrencia', 'denuncia', 'dataDaDenuncia')  # Certifique-se de incluir 'id' aqui se quiser exibi-lo na lista

    # Define a ordem dos campos no formulário de administração
    list_filter = ('tipoDeOcorrencia',)
    fieldsets = ( (None, {
            'fields': ('id_denuncia','tipoDeOcorrencia','denuncia', 'dataDaDenuncia')}),
    )

admin.site.register(Denuncia, DenunciaAdmin)

admin.site.register(Advogado)
