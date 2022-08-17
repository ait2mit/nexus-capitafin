from django.shortcuts import render, redirect

# Create your views here.
from django import forms
from django.utils import timezone
from .forms import MyCommentForm
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def contact(request):
    if request.method == "POST":
        form = MyCommentForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()




            mail_subject = 'Support Message from an User '
            msg = render_to_string('support_msg_notifi_to_admin.html', {

                'name': model_instance.name,
                'subject': model_instance.subject,
                'email': model_instance.email,
                'message': model_instance.message,

            })
            #to_email = form.cleaned_data.get('email')
            to_email = 'dwaterbd@gmail.com'
            email = EmailMessage(
                        mail_subject, msg, to=[to_email]
            )
            email.send()

















            return render(request, "contact_email_thank_you.html")
    else:
        form = MyCommentForm()
        return render(request, "contact_form.html", {'form': form})
