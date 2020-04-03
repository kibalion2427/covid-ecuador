from django.contrib import admin
from .models import Pais,Provincia,CasoCovid


class PaisesInline(admin.TabularInline):
    pass
    # model = Pais.provincias.through
    # verbose_name = 'pais'
    # model = Pais
    # extra = 1

class ProvinciaAdmin(admin.ModelAdmin):
    # list_display = ('codigo',)
    # search_fields = ('codigo', )
    # list_filter = ('codigo', )
    inlines = (PaisesInline,)

admin.site.register({Pais,Provincia,CasoCovid})
# admin.site.register(Provincia,ProvinciaAdmin)

# Register your models here.
