from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_Form = ContactForm()
    if request.method == "POST":
        contact_Form = ContactForm(data=request.POST)
        if contact_Form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
        #Envaimos el correo y rediriccionamos
        email = EmailMessage(
            "La Caffetiera: nuevo mensaje de contacto",
            "De {} <{}>\n\nEscribio\n\n{}".format(name,email,content),
            'no-contestar@inbox.mailtrap.io',
            ["saul_mendozaespinosa@hotmail.com"],
            reply_to=[email]
        )
        try:
            email.send()
            return redirect(reverse('contact')+"?ok")
        except:
            import traceback
            traceback.print_exc()
 

        
    return render(request,'contact/contact.html',{'form': contact_Form})
