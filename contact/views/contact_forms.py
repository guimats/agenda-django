from django.shortcuts import get_object_or_404, render, redirect  # type:ignore
from django.urls import reverse  # type:ignore

from contact.forms import ContactForm
from contact.models import Contact


def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'form': form,
            'form_action': form_action,
        }

        # confirma se o formulário não tem erros para salvar
        if form.is_valid():
            # form.save() -> para salvar no banco de dados
            # commit=False para não salvar direto
            # contact = form.save(commit=False)
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
    )


def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        context = {
            'form': form,
            'form_action': form_action,
        }

        # confirma se o formulário não tem erros para salvar
        if form.is_valid():
            # form.save() -> para salvar no banco de dados
            # commit=False para não salvar direto
            # contact = form.save(commit=False)
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
    )
