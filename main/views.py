from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Config, Portfolio, Team, SocialNetworks, Partners
from .forms import ContactForm
import requests

# Create your views here.


def index(request):
    portfolios = Portfolio.objects.all()
    socialnetworks = SocialNetworks.objects.all()
    teams = Team.objects.all()
    partners = Partners.objects.all()
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
        'partners':partners
    }
    context['list1'] = context['config'].texts1.split('\n')
    
    return render(request, 'index.html', context)
