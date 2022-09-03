from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

def index(request):
    movies = Article.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)

def new(request):
    return render(request, 'movies/new.html') 


def create(request):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    movie = Article(title= title, audience = audience, release_date= release_date, genre= genre, score= score,poster_url= poster_url,description= description)
    movie.save()

    return redirect(request, 'movies:index') 

def detail(request, pk):
    movie = Article.objects.get(pk=pk)
    context = {
        'movie' : movie,
    }
    return render(request, 'movies/detail.html', context) 

def edit(request, pk):
    movie = Article.objects.get(pk=pk)
    context = {
        'movie' : movie,
    }
    return render(request, 'movies/edit.html', context) 

def delete(request, pk):
    if request.method == "POST":
        movie = Article.objects.get(pk=pk)
        movie.delete()
    return render(request, 'movies:index') 

def update(request, pk):
    return render(request, 'movies/update.html') 

