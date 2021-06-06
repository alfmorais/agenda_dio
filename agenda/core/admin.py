from django.contrib import admin
from core.models import Evento

# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao', 'data_evento')
    list_filter = ('usuario', 'data_evento')


admin.site.register(Evento, EventoAdmin)
