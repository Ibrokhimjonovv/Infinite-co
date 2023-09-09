from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from .forms import ContactForm
import requests

# Create your views here.


def index(request):
    portfolios = Portfolio.objects.all()
    socialnetworks = SocialNetworks.objects.all()
    teams = Team.objects.all()
    partners = Partners.objects.all()
    navbars = Navbar.objects.all()
    getstarteds = Getstarted.objects.all()
    statics = Statics.objects.all()
    services = Services.objects.all()
    categories = Categories.objects.all()
    questions = Questions.objects.all()

    if request.method =='POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']

            send_mail(
                'Contact Form',
                f'Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}', 
                'settings.EMAIL_HOST_USER',
                ['megabytekekabyt@gmail.com'],
                fail_silently=False,
            )

            requests.post(f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage?chat_id={settings.CHAT_ID}&text=Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}")
            
            form.save()
            return redirect('/')
    else:
        form = ContactForm()

    context = {
        'config': Config.objects.order_by('-pk').first(),
        'form':form,
        'portfolios':portfolios,
        'teams':teams,
        'socialnetworks':socialnetworks,
        'partners':partners,
        'navbars':navbars,
        'getstarteds':getstarteds,
        'statics':statics,
        'services':services,
        'categories':categories,
        'questions':questions
    }
    context['list1'] = context['config'].texts1.split('\n')
    
    return render(request, 'index.html', context)

def portfolio_detail(request, portfolio_id):
    # portfolio_details = Portfolio.objects.all()
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    # portfolio_details = Portfolio.objects.get(id=1)
    navbars = Navbar.objects.all()
    getstarteds = Getstarted.objects.all()
    context = {
        'config': Config.objects.order_by('-pk').first(),
        'portfolio':portfolio,
        'navbars':navbars,
        'getstarteds':getstarteds
    }

    return render(request, 'portfolio_details.html', context)