from django.shortcuts import render  # type:ignore
# importando os contatos para exibir na tela
from contact.forms import RegisterForm  # type:ignore


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )
