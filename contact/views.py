from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm


# Create your views here.

def contact(request):
    #print('Tipo de peticion:', format(request.method))
    contact_form = ContactForm()

    # Procesar el formulario si la petition es POST
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            # Si los campos son validos, procesar los datos
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviar el correo o guardar en la base de datos (https://mailtrap.io/es/)
            # Asunto, cuerpo, email_origen, email_destino, email_respuesta
            email = EmailMessage(
                "La Ceffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ['comprafacil91@gmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
                # Si se envía correctamente, redirigir a la misma pagina con un mensaje de éxito
                return redirect(reverse('contact')+'?ok')
            except:
                # Si no se puede enviar el correo, redirigir a la misma pagina con un error
                return redirect(reverse('contact')+'?fail')
            
    return render(request, 'contact/contact.html',{'form': contact_form})
