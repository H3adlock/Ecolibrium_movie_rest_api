from django.urls import path
from .views import *

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='api'),
    path('movies/create', MovieCreateView.as_view(), name='api_create')
]
