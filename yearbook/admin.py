from django.contrib import admin
from yearbook.models import Funcao, Lotacao, Unidade_Organizacional, Sala, Cargo, Pessoa

# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,					{'fields'	:	['nome','foto','cargo']}),
		('Data de Nascimento',	{'fields'	:	['nascimento', 'ferias_inicio', 'ferias_fim']}),
	]

admin.site.register(Funcao)
admin.site.register(Lotacao)
admin.site.register(Unidade_Organizacional)
admin.site.register(Sala)
admin.site.register(Cargo)
admin.site.register(Pessoa, PessoaAdmin)