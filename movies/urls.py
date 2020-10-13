from django.urls import path
from .views import *

urlpatterns = [
    path('movies', MovieListView.as_view(), name='api')
]
