from django.shortcuts import render, redirect
from .forms import FilmForm
from .models import Film

def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('film_list')
    else:
        form = FilmForm()
    return render(request, 'films/add.html', {'form': form})

def film_list(request):
    films = Film.objects.all().order_by('-created_at')
    return render(request, 'films/list.html', {'films': films})