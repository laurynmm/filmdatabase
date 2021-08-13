from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_film/', views.add_film, name='add-film'),
    path('add_review/', views.add_review, name='add-review'),
    path('delete_review/', views.delete_review, name='delete-review'),
    path('update_review/', views.update_review, name='update-review'),
]
