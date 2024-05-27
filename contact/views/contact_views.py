from django.shortcuts import render, get_object_or_404  # type: ignore
# importando os contatos para exibir na tela
from contact.models import Contact
# from django.http import Http404  # type: ignore


def index(request):
    # puxando todos os contatos registrados no Contact (filtrando pelo show)
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]

    # criando variavel com as informações dos contatos
    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
    }

    return render(
        request, 'contact/index.html',
        # adicionando os contatos no return da view
        context
        )


def contact(request, contact_id):
    # puxando todos os contatos registrados no Contact (filtrando pelo show)
    # single_contact = Contact.objects.filter(pk=contact_id).first()

    # puxando um id do contato para o link
    # (função get_object_or_404 retorna um erro caso o ID não exista)
    single_contact = get_object_or_404(
        Contact.objects, pk=contact_id, show=True
        )
    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    # criando variavel com as informações dos contatos
    context = {
        'contact': single_contact,
        'site_title': site_title,
    }

    return render(
        request, 'contact/contact.html',
        # adicionando os contatos no return da view
        context
        )
