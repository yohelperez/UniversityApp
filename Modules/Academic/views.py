from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def contactForm(request):
    return render(request, "contactForm.html")

def contact(request):
    
    
    
    if request.method == "POST":
        """
        Code for when having access to a real email
        
        subject = request.POST["txtSubject"]
        message = request.POST["txtMessage"] + " / Email: " + request.POST["txtEmail"] 
        email_from = settings.EMAIL_HOST_USER
        email_to = ["kristan.virtualassistant@gmail.com"]
        send_mail(subject, message, email_from, email_to, fail_silently = False)
        return render(request, "successfulContact.html")
        """
        return render(request, "successfulContact.html")
    return render(request, "contactForm.html")