from django.contrib import admin  # type: ignore
from contact.models import Contact, Category


# Cadastrando o model 'Contact'
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # mostra as colunas informadas no display dos contacts
    list_display = 'id', 'first_name', 'last_name', 'phone', 'show'
    # ordena pelo valor informado - sinal de negativo '-' torna descrescente
    ordering = '-id',
    # cria um filtro para a tabela exibida
    # list_filter = 'created_date',
    # cria um campo de busca que procura nos campos informados
    search_fields = 'id', 'first_name', 'last_name',
    # quantos cadastros serão exibidos por página
    list_per_page = 10
    # máximo de cadastro que pode ser exibidio no 'mostrar tudo'
    list_max_show_all = 100
    # torna o dado editavel diretamente pelo display
    list_editable = 'first_name', 'last_name', 'show'
    # seleciona qual campo ficara com o link para acesso do cadastro
    list_display_links = 'phone', 'id',


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = '-id',
    list_display = 'name',
