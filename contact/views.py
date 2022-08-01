from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from contact.forms import ContactForm

# Create your views here.
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'name': form.cleaned_data['name'], 
			'subject': form.cleaned_data['subject'], 
			'email': form.cleaned_data['email'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'liveletrevo@gmail.com', ['liveletrevin6@gmail.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("contact")
      
	form = ContactForm()
	return render(request, "appmain/contact.html", {'form':form})