from django.shortcuts import render, get_object_or_404, redirect  # type:ignore
# importando os contatos para exibir na tela
from contact.models import Contact  # type:ignore
from django.db.models import Q  # type:ignore


def create(request):
    context = {

    }

    return render(
        request, 'contact/create.html',
        context
        )
