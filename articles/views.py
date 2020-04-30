from django.shortcuts import render
from articles.models import Article
from .forms import ContactForm
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.http import HttpResponse

def index(request):
    context = {
        'articles': Article.objects.all(),
    }
    return render(request, 'articles/articles_list.html', context)


def email(request, id):
    article = Article.objects.get(id=id)
    initial = {'subject': article.title, 'message': article.description}
    form = ContactForm(initial=initial)
    context = {'form': form}
    return render(request, 'articles/email.html', context)



def send_email(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            print("hello")
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            recipient = form.cleaned_data['recipient'] 
            send_mail(subject, message, sender, [recipient], fail_silently=False)
            return render(request, 'articles/success_email.html')
    
    return render(request, 'articles/fail_email.html')
