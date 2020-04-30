from django.shortcuts import render
from articles.models import Article
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseBadRequest

def index(request):
    '''
    Shows a list of articles with their title and image 
    '''
    context = {
        'articles': Article.objects.all(),
    }
    return render(request, 'articles/articles_list.html', context)


def email(request, id):
    '''
    Loads email form with intial data article title and article description
    '''
    try:
        article = Article.objects.get(id=id)
        initial = {'subject': article.title, 'message': article.description}
        form = ContactForm(initial=initial)
        context = {'form': form}
        return render(request, 'articles/email.html', context)
    except:
        return HttpResponseBadRequest("Article is missing", status=400)


def send_email(request):
    '''
    Sending email using Amazon Simple Email Service (Amazon SES)  
    '''
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            try:
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                sender = form.cleaned_data['sender']
                recipient = form.cleaned_data['recipient'] 
                send_mail(subject, message, sender, [recipient], fail_silently=False)
                return render(request, 'articles/success_email.html')
            except:
                return render(request, 'articles/fail_email.html')
        return HttpResponseBadRequest("Form is not valid", status=400)
    return HttpResponseBadRequest("POST method is only allowed", status=400)


def error_404(request, exception):
    data = {}
    return render(request,'articles/404.html', data)
    
    
