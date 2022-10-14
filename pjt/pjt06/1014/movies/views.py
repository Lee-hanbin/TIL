from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from movies.forms import MovieForm
# Create your views here.

def index(request):
    return render(request, 'movies/index.html')

@login_required
# @require_http_methods(['GET','POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form':form,
    }
    return render(request, 'movies/create.html')

# def detail(request,pk):

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=pk)
        movie.delete()
    return redirect('movies:index')

@login_required
# @require_http_methods(['GET','POST'])
def update(request,pk):
    return render(request, 'movies/update.html')