from django.shortcuts import render, redirect
from ..forms import ContactForm


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        context = {
            'form': form,
        }

        if form.is_valid():
            # Para salvar direto no banco
            # form.save()

            # Quando se deseja alterar algum dado antes de salvar no banco
            contact = form.save(commit=False)
            contact.first_name = contact.first_name.strip()
            contact.last_name = contact.last_name.strip()
            contact.save()
            return redirect('contact:create')

        return render(request, 'contact/create.html', context)

    context = {
        'form': ContactForm(),
    }

    return render(request, 'contact/create.html', context)
