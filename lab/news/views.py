from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import News
from .forms import NewsForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def index(request):
    news = News.objects.order_by('-create_time')
    context = {'news': news}
    return render(request, 'news/index.html', context)

@login_required(login_url='/login/')
def add(request):
    if request.method == 'POST':
        news = NewsForm(request.POST)
        if news.is_valid():
            news = news.save(commit=False)
            news.create_time = timezone.now()
            news.last_edit_time = timezone.now()
            news.save()
            return redirect('view_news')
        else:
            context = {'form': news}
            return render(request, 'news/add.html', context)
    else:
        news = NewsForm()
        context = {'form': news}
        return render(request, 'news/add.html', context)

def get(request, id):
    news = get_object_or_404(News, id=id)
    context = {'news': news}
    return render(request, 'news/view.html', context)

@login_required(login_url='/login/')
def delete(request, id):
    News.objects.filter(id=id).delete()
    return index(request)

@login_required(login_url='/login/')
def update(request, id):
    news = get_object_or_404(News, id=id)
    context = {'news': news}
    return render(request, 'news/update.html', context)

@login_required(login_url='/login/')
def updaterecord(request, id):
    topic = request.POST['topic']
    author = request.POST['author']
    text = request.POST['text']
    news = News.objects.get(id=id)
    news.topic = topic
    news.author = author
    news.text = text
    news.last_edit_time = timezone.now()
    news.save()
    return index(request)