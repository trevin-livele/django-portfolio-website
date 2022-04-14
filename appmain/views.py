from django.shortcuts import render
from categories.models import Category
from appmain.models import Project

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