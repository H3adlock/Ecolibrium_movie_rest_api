from django.urls import path
from .views import *

urlpatterns = [
    path('movies', MovieListView.as_view(), name='api'),
    path('movies/create', MovieCreateView.as_view(), name='api_create'),
    path('movies/details/<pk>', MovieDetailView.as_view(), name='api_update_delete')
]
