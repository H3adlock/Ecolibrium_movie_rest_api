from django.http import HttpResponse
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes

from .models import Movie
from .serializers import MovieSerializer
from .permissions import IsAdminOrReadOnly


# Create your views here.
class MovieListView(APIView):
    """
    API view for searching Movies
    """
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        queryset = Movie.objects.all()
        allowed_methods = ['GET']
        name = request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        director = request.query_params.get('director', None)
        if director is not None:
            queryset = queryset.filter(director__icontains=director)

        # filter if movie has genre with queried genre name
        # genre = request.query_params.get('genre', None)
        # if genre is not None:
        #     queryset = queryset.filter(genre__name__icontains=genre)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # @permission_classes([IsAdminOrReadOnly])
    # def post(self, request, format=None):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieCreateView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAdminOrReadOnly,)
