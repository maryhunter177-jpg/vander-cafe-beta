from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Cafe

# Registra o usuário no painel
admin.site.register(Usuario, UserAdmin)

# Configura a tabela de Cafés
@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'produtor', 'preco', 'status')
    list_filter = ('status',)
    list_editable = ('status',) # Permite aprovar direto na lista!