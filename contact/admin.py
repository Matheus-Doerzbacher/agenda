from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'phone',
        'email',
    )
    ordering = ('-id',)
    # list_filter = ('first_name',)
    search_fields = (
        'id',
        'first_name',
        'last_name',
    )
    list_per_page = 20  # numero de resultados por pagina
    list_editable = (
        'last_name',
    )  # Permite editar os campos selecionados direto na lista
    list_display_links = (
        'first_name',
    )  # Permite clicar nos campos da lista para editar
