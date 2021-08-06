from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('films/', views.FilmListView.as_view(), name='films'),
    path('film/<int:pk>', views.FilmDetailView.as_view(), name='film-detail'),
    path('persons/', views.PersonListView.as_view(), name='people'),
    path('person/<int:pk>', views.PersonDetailView.as_view(), name='person-detail'),
    path('reviews/', views.ReviewListView.as_view(), name='reviews'),
    path('reviews/<rating>/', views.ReviewRatingListView.as_view(), name='reviews-rating'),
    path('myreviews/', views.ReviewsUserListView.as_view(), name='my-reviews'),
    path('film/create/', views.FilmCreate.as_view(), name='film-create'),
    path('film/<int:pk>/update/', views.FilmUpdate.as_view(), name='film-update'),
    path('person/create/', views.PersonCreate.as_view(), name='person-create'),
    path('person/<int:pk>/update/', views.PersonUpdate.as_view(), name='person-update'),
    path('credit/create/', views.CreditCreate.as_view(), name='credit-create'),
    path('credit/<int:pk>/update/', views.CreditUpdate.as_view(), name='credit-update'),
    path('review/create/', views.ReviewCreate.as_view(), name='review-create'),
    path('review/<uuid:pk>/update/', views.ReviewUpdate.as_view(), name='review-update'),
    path('review/<uuid:pk>/delete/', views.ReviewDelete.as_view(), name='review-delete'),
    path('films/api/', views.rest_films, name="films-api"),

]