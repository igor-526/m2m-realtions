from django.shortcuts import render, HttpResponse

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles = Article.objects.all()
    context = {'object_list': articles}

    return render(request, template, context)