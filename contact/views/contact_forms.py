from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from ..forms import ContactForm
from ..models import Contact


def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':
        form = ContactForm(request.POST)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            # Para salvar direto no banco
            # form.save()

            # Quando se deseja alterar algum dado antes de salvar no banco
            contact = form.save(commit=False)
            contact.first_name = contact.first_name.strip()
            contact.last_name = contact.last_name.strip()
            contact.save()
            return redirect('contact:update', contact_id=contact.id)

        return render(request, 'contact/create.html', context)

    context = {
        'form': ContactForm(),
        'form_action': form_action,
    }

    return render(request, 'contact/create.html', context)


def update(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            # Para salvar direto no banco
            # form.save()

            # Quando se deseja alterar algum dado antes de salvar no banco
            contact = form.save(commit=False)
            contact.first_name = contact.first_name.strip()
            contact.last_name = contact.last_name.strip()
            contact.save()
            return redirect('contact:update', contact_id=contact.id)

        return render(request, 'contact/create.html', context)

    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }

    return render(request, 'contact/create.html', context)
