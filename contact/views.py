from django.shortcuts import render
from .forms import Send_email
# Create your views here.
from django.core.mail import send_mail

def contact(request):
    if request.POST:
        send_mail(
            f'{request.POST["Subject"]} -> {request.POST["name"]} : {request.POST["email"]}',
            f'{request.POST["name"]},{request.POST["email"]},{request.POST["Subject"]}\n {request.POST["message"]}',
            'obidzeromax@gmail.com',
            [f'{request.POST["email"]}'],
            fail_silently=False,
        )
    form = Send_email()
    ctx = {
        "form" : form
    }
    return render(request,"contact/contact.html",ctx)