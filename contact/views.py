from django.shortcuts import render, redirect
from app.forms import ContactForm

# Create your views here.


def contact(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'home.html', context)