from django.shortcuts import render, get_object_or_404, redirect  # type:ignore
# importando os contatos para exibir na tela
from contact.models import Contact
from django.db.models import Q  # type:ignore


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


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects \
        .filter(show=True) \
        .filter(
            # Q com o pipe '|' servem nesse caso como 'or'
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
            ) \
        .order_by('-id')

    context = {
        'contacts': contacts,
        'site_title': 'Search - '
    }

    return render(
        request, 'contact/index.html',
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
