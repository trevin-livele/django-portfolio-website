from django.shortcuts import render

# Create your views here.
def services(request):
    return render(request, 'appmain/services.html')

def portfolio(request):
    return render(request, 'appmain/portfolio.html')



def contact(request):
    return render(request, 'appmain/contact.html')