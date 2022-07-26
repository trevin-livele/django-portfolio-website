from django.shortcuts import render
from categories.models import Category
from appmain.models import Project  
from appmain.forms import  MailingListForm
from .models import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail


# Create your views here.
def services(request):
    return render(request, 'appmain/services.html')

def portfolio(request):
    category = Category.objects.all()
    projects = Project.objects.all()

    context = {
        'category': category,
        'projects': projects,
    }
    return render(request, 'appmain/portfolio.html', context)



def contact(request):
    return render(request, 'appmain/contact.html')



def sendMails(request):
    mails = MailingList.objects.all()
    send_mail("subject", "message", "erdeminsurance22@gmail.com", mails)
    return redirect("/")