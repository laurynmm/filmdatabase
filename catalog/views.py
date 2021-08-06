from json.encoder import JSONEncoder
from catalog.forms import FilmTitleForm, PersonNameForm, ReviewRatingForm
import datetime
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse

from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, FormMixin, UpdateView, DeleteView, ModelFormMixin
from django.urls import reverse_lazy, reverse

from .models import Credit, Film, Person, Review
from .forms import FilmSearchForm

from django.core import serializers

# Home page of site
def index(request):
    """View function for home page of site"""

    all_films = Film.objects.all()
    form = FilmSearchForm()

    context = {
        'form': form,
        'all_films': all_films,
    }

    return render(request, 'index.html', context=context)


def rest_films(request):
    """View function for home page of site"""

    all_films = Film.objects.all()
    films_output = []
    for film in all_films:
        films_output.append({
            'title': film.title,
            'year': film.year,
        })
    return JsonResponse(films_output, safe=False)

# Generic List & Detail views
class FilmListView(FormMixin, generic.ListView):
    model = Film
    form_class = FilmTitleForm

    def get_queryset(self):
        if ('title' in self.request.GET):
            title = self.request.GET['title']
            return Film.objects.filter(title__icontains=title)
        else:
            return Film.objects.all()
    
class FilmDetailView(generic.DetailView):
    model = Film

class PersonListView(FormMixin, generic.ListView):
    model = Person
    form_class = PersonNameForm

    def get_queryset(self):
        if ('first_name' in self.request.GET):
            return Person.objects.filter(first_name__icontains=self.request.GET['first_name'])
        else:
            return Person.objects.all()

class PersonDetailView(generic.DetailView):
    model = Person

class ReviewListView(FormMixin, generic.ListView):
    model = Review
    form_class = ReviewRatingForm

    def get_queryset(self):
        if ('rating' in self.request.GET):
            return Review.objects.filter(rating__exact=self.request.GET['rating'])
        else:
            return Review.objects.all()

# Generic List views with some filtering
class ReviewRatingListView(FormMixin, generic.ListView):
    model = Review
    form_class = ReviewRatingForm

    def get_queryset(self):
        if ('rating' in self.request.GET):
            return Review.objects.filter(rating__exact=self.request.GET['rating'])
        else:
            return Review.objects.all()

class ReviewsUserListView(LoginRequiredMixin, FormMixin, generic.ListView):
    model = Review
    template_name = 'catalog/review_list_for_user.html'
    ordering = ['-date_watched']
    form_class = FilmSearchForm

    def get_queryset(self):
        user_films = Review.objects.filter(user=self.request.user)

        if ('title' in self.request.GET):
            return user_films.filter(film__title__icontains=self.request.GET['title'])
        else:
            return user_films

# Generic editing views
class FilmCreate(LoginRequiredMixin, CreateView):
    model = Film
    fields = ['title', 'plot', 'year', 'imdb_id']
    initial = { 'year': 2020 }

class FilmUpdate(LoginRequiredMixin, UpdateView):
    model = Film
    fields = ['title', 'plot', 'year', 'imdb_id', 'genre', 'language']

class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'date_of_birth']

class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

class CreditCreate(LoginRequiredMixin, CreateView):
    model = Credit
    fields = ['film', 'person', 'job_title', 'if_actor_character_role']
    success_url = reverse_lazy('films')

class CreditUpdate(LoginRequiredMixin, UpdateView):
    model = Credit
    fields = ['film', 'person', 'job_title', 'if_actor_character_role']

class ReviewCreate(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['film', 'private', 'date_watched', 'rating']
    initial = {'date_watched': datetime.date.today()}
    success_url = reverse_lazy('my-reviews')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewUpdate(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['film', 'private', 'date_watched', 'rating']
    success_url = reverse_lazy('my-reviews')

class ReviewDelete(LoginRequiredMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('my-reviews')

class MartinsMovieSearch(generic.ListView, FormMixin):
    model = Film
    template_name = "martin.html"
    form_class = FilmSearchForm

    def get_queryset(self):
        return Film.objects.all()
    
    def post(self, request):
        form = self.get_form()

        filter = {}
        if form.is_valid():
            if ('title' in form.cleaned_data):
                filter['title__contains'] = form.cleaned_data["title"]
            if ('before' in form.cleaned_data):
                filter['year__lte'] = form.cleaned_data["before"]

        films = Film.objects.filter(**filter)

        context = {
         'film_list': films,
         'form': form,
        }
        return render(request, 'martin.html', context=context)

# from django.views.decorators.csrf import csrf_protect
# @csrf_protect
# def martin(request):
#     films = Film.objects.filter(title__contains=request.POST['title'])
#     context = {
#         'films': films,
#         'get_params': request.GET,
#         'post_params': request.POST,
#     }

#     return render(request, 'martin.html', context=context)
