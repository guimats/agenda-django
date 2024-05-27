from django.shortcuts import render  # type: ignore
# importando os contatos para exibir na tela
from contact.models import Contact


def index(request):
    # puxando todos os contatos registrados no Contact
    contacts = Contact.objects.all()

    # criando variavel com as informações dos contatos
    context = {
        'contacts': contacts,
    }

    return render(
        request, 'contact/index.html',
        # adicionando os contatos no return da view
        context
        )
