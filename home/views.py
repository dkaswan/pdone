from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    context = {
        'username': 'John Doe',
    }
    return render(request, 'index.html', context);

def about(request):
    context = {}
    return render(request, 'about.html', context);

def services(request):
    context = {}
    return render(request, 'services.html', context);

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name = name, email = email, phone = phone, message = message, date = datetime.today())
        contact.save()
    context = {}
    return render(request, 'contact.html', context);