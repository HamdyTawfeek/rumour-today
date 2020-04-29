from django.shortcuts import render
from articles.models import Article

def index(request):
    context = {
        'articles': Article.objects.all(),
    }
    return render(request, 'articles/articles_list.html', context)