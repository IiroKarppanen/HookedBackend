from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieSerializer
from .models import Movies
import json

# POST/GET/DELETE Request functions

@api_view(['GET', 'POST'])
def movie(request):

    if request.method == 'GET':
        movie = Movies.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def movie_detail(request, pk):
    
    try:
        movie = Movies.objects.get(pk=pk)
    except Movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
