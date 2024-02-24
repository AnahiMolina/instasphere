from django.contrib import admin
from .models import Usuario, Publicacion, Comentarios, Conversacion
# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
    'id',
    'usuario',
    'nombre',
    'apellidos',
    'correo',
    'contrasenia',
    )

    list_display_links = ('usuario',)
    search_fields = ('usuario','nombre')
    sortable_by = ('id')


class PublicacionAdmin (admin.ModelAdmin):
    list_display = (
        'descripcion',
        'fecha',
        'id_usuario',
        'tipo',
    )

class ComentariosAdmin (admin.ModelAdmin):
    list_display = (
        'fecha',
        'contenido',
        'id_publicacion',
        'id_usuario_comentario',
    )
    list_display_links = ('fecha',)
    search_fields = ('contenido ', 'fecha')


class ConversacionAdmin (admin.ModelAdmin):
    list_display = (
        'fecha',
        'contenido',
        'estatus',
        'id_usuario_orig',
        'id_usuario_dest',
    )
    list_display_links = ('fecha',)
    search_fields = ('estatus' , 'contenido')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Comentarios, ComentariosAdmin)
admin.site.register(Conversacion, ConversacionAdmin)

