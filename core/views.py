from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieSerializer
from .models import Movies
import json, os

#Movies.objects.all().delete()

##path = os.getcwd()
#file = os.path.join(path, "movies.json")

#print('path')
#files = [f for f in os.listdir('.') if os.path.isfile(f)]
#for f in files:
 #   print(f)

#w#ith open(r"movies.json", encoding="utf8") as f:
 #   data = json.load(f)

#for movie in data:
#    serializer = MovieSerializer(data=movie)
#    if serializer.is_valid():
#        print("valid")
#        
#        serializer.save()

# MOVIE DATA FUNCTIONS

@api_view(['GET', 'POST'])
def movie(request):

    permission_classes = ()
    authentication_classes = ()

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
    permission_classes = ()
    authentication_classes = ()
    
    try:
        movie = Movies.objects.get(pk=pk)
    except Movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
