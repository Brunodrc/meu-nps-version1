from django.contrib import admin
from .models import Usuario

admin.site.register(Usuario)

"""
#permite que as informações do usuario sejam apenas vizualizadas e nao alteradas pelo admin 
@admin.register(Usuario)
class Usuario_admin(admin.ModelAdmin):
    readonly_fields = ('nome','emal','senha','telefone')
 """
