
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Film, Review
from .forms import NewFilmForm

# Home page of site
def index(request):
    """View function for home page of site"""

    if request.user.is_authenticated:
        user_films = Film.objects.filter(review__user=request.user)
        other_films = Film.objects.exclude(review__user=request.user)
        form = NewFilmForm()
        context = {
            'form': form,
            'user_films': user_films,
            'other_films': other_films,
        }
    else:
        all_films = Film.objects.all()
        form = NewFilmForm
        context = {
            'form': form,
            'all_films': all_films,
        }

    return render(request, 'index.html', context=context)

# Adding new films
def add_film(request):
    form = NewFilmForm(request.POST)

    if form.is_valid():
        data = form.cleaned_data['title']
            
        if Film.objects.filter(title__icontains=data).count() == 0:
            film = Film(title=data)
            film.save()
    
    return HttpResponseRedirect(reverse('index'))