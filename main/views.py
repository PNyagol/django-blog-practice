from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send an email)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            print('Name:', name)
            print('Email:', email)
            print('Message:', message)
            return redirect('main:contact_success')  # Redirect to a success page
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})


def contact_success_view(request):
    return render(request, 'main/contact_success.html')


