from django.shortcuts import render
from django.views.decorators.http import require_safe, require_http_methods
from .models import Movie, Genre



# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    genres = Genre.objects.filter(movie=movie_pk)
    context = {
        'movie': movie,
        'genres': genres,
    }
    return render(request, 'movies/detail.html', context)


@require_http_methods(['GET', 'POST'])
def recommended(request):
    if request.method == "POST":
        genre = Genre.objects.get(name=request.POST.get('name'))
        movies = Movie.objects.filter(genres=genre.pk)
    else: 
        movies = None
    genres = Genre.objects.all()
    context = {
        'movies': movies,
        'genres': genres,
    }
    return render(request, 'movies/recommended.html', context)
    