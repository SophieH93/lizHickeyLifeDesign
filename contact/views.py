from django.shortcuts import render, reverse, redirect
from .forms import ContactForm
from django.contrib import messages


def contact(request):

    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid:
            contact_form.save()
            messages.success(request, 'Thank you for contacting us!\
                 We will get back at you in the next 24 hours.')
            return redirect('contact')
    
    template = 'contact/contact.html'

    context = {
        'contact_form': contact_form,
    }


    return render(request, template, context)
