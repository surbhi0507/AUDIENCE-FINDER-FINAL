from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.http import HttpResponse
from mysite.core.models import form
from django.contrib import messages





def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        print(name,email,phone,address)
        #form=form(name=name,email=email,phone=phone,address=address)
        #form.save()
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


@login_required
def secret_page(request):

    
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'

def desmail(request):
    if request.method == 'POST':
        message = request.POST['message']

        send_mail('Contact Form',
         message, 
         settings.EMAIL_HOST_USER,
         settings.EMAIL_RECEIVING_USER,
         fail_silently=False)
         
    return render(request,'desmail.html')


      
def devmail(request):
    if request.method == 'POST':
        message = request.POST['message']

        send_mail('Contact Form',
         message, 
         settings.EMAIL_HOST_USER,
         settings.EMAIL_RECEIVING_USER1, 
         fail_silently=False)
         
    return render(request,'devmail.html')  


def dmail(request):
    if request.method == 'POST':
        message = request.POST['message']

        send_mail('Contact Form',
         message, 
         settings.EMAIL_HOST_USER,
         settings.EMAIL_RECEIVING_USER2, 
         fail_silently=False)
        
    return render(request,'dmail.html')  
    



def thanks(request):
    return render(request,'thanks.html')  
