import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Film, Review
from .forms import CreateReviewForm, NewFilmForm, UpdateReviewForm

# Home page of site
def index(request):
    """View function for home page of site"""

    if request.user.is_authenticated:
        user_films = Film.objects.filter(review__user=request.user).distinct()
        other_films = Film.objects.exclude(review__user=request.user)
        user_reviews = Review.objects.filter(user=request.user)
        context = {
            'film_form': NewFilmForm(),
            'review_form': CreateReviewForm(initial={'date_watched':datetime.date.today()}),
            'update_review_form': UpdateReviewForm(initial={'new_date':datetime.date.today()}),
            'user_films': user_films,
            'other_films': other_films,
            'user_reviews': user_reviews,
        }
    else:
        all_films = Film.objects.all()
        context = {
            'all_films': all_films,
        }

    return render(request, 'index.html', context=context)

@login_required
# Adding new films
def add_film(request):
    form = NewFilmForm(request.POST)

    if form.is_valid():
        data = form.cleaned_data['title']
            
        if Film.objects.filter(title__icontains=data).count() == 0:
            film = Film(title=data)
            film.save()
    
    return HttpResponseRedirect(reverse('index'))

@login_required
# Adding new reviews
def add_review(request):
    form = CreateReviewForm(request.POST)

    if form.is_valid():
        Review(film=form.cleaned_data['film'],
               date_watched=form.cleaned_data['date_watched'],
               user=request.user).save()
    
    return HttpResponseRedirect(reverse('index'))

@login_required
# Delete review
def delete_review(request):
    form = UpdateReviewForm(request.POST)

    if form.is_valid():
        review_id = form.cleaned_data['review']
        review = Review.objects.get(pk=review_id)

        if review.user == request.user:
            review.delete()

    return HttpResponseRedirect(reverse('index'))

@login_required
# Modify review date
def update_review(request):
    form = UpdateReviewForm(request.POST)

    if form.is_valid():
        review_id = form.cleaned_data['review']
        review = Review.objects.get(pk=review_id)

        if review.user == request.user:
            review.date_watched = form.cleaned_data['new_date']
            review.save()

    return HttpResponseRedirect(reverse('index'))