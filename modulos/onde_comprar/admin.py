from django.contrib import admin
from models import OndeComprar, Estado, Cidade, Franquia

class FranquiaAdmin(admin.ModelAdmin):
    list_display = ['ondecomprar', 'cidade', 'endereco', 'telefone', 'email']

admin.site.register(OndeComprar)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Franquia)
