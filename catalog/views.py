
from django.shortcuts import render

from .models import Film, Review

# Home page of site
def index(request):
    """View function for home page of site"""

    if request.user.is_authenticated:
        user_films = Film.objects.filter(review__user=request.user)
        other_films = Film.objects.exclude(review__user=request.user)
        context = {
            'user_films': user_films,
            'other_films': other_films,
        }
    else:
        all_films = Film.objects.all()
        context = {
            'all_films': all_films,
        }

    return render(request, 'index.html', context=context)
