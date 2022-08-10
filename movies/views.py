from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User , Collection , Movie
from .serializers import UserSerializer , CreateUserSerializer , CollectionSerializer , MovieSerializer
from .services import  get_Movies
from django.contrib.auth import get_user_model  
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from django.views import View
import json

# class CollectionViewSet(viewsets.ModelViewSet):
#     queryset = Collection.objects.all()
#     serializer_class = CollectionSerializer

# class MovieViewSet(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

@api_view(['POST','GET'])
@permission_classes([AllowAny])
def user_create(request):
    if request.method == 'POST':
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data)
            tok  = {"access_token":serializer.data['token']}
            return JsonResponse(tok, safe=False)

    else:
        users = get_user_model().objects.all()
        serializer = CreateUserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

# @api_view(['POST','GET'])
# @permission_classes([AllowAny])
# def get_collections(request):
#     if request.method == 'POST':
#         print(request.data)
#         serializer = CollectionSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return JsonResponse(serializer.data, safe=False)


def get_movies(request):
    
    movies = get_Movies()
    return JsonResponse(movies, safe=False)



class MovieCollections(View):

    def post(self, request):

        data = json.loads(request.body.decode("utf-8"))
        title = data.get('title')
        description = data.get('description')

        collectionData = {
            'title':title,
            'description':description
        }

        collection_item = Collection.objects.create(**collectionData)

        movies = data.get('movies')
        response_data ={'collection_id': collection_item.id} 
        for x in movies :

            m_title = x.get('title')
            
            m_description =  x.get('description') ,
            genres = x.get('genres'),
            uuid = x.get('uuid')

            movieData = {
                'title':m_title,
                'description':m_description,
                'genres': genres,
                'uuid':uuid
            }

            movie_item = Movie.objects.create(**movieData)

            movie_item.collection.add(collection_item)

        return JsonResponse(response_data, status=201)

    def get(self, request):
        items_count = Collection.objects.count()
        items = Collection.objects.all()

        Collection_data = []
        for item in items:
            Collection_data.append({
                'title': item.title,
                'description': item.description,
                'id': item.id,
            })

        data = {"is_success":True,
                "data":{
                    "collections":Collection_data

                    
                }
            
        }

        return JsonResponse(data)

   
   
class MovieCollectionsUpdate(View):

    def put(self, request, item_id):
        data = json.loads(request.body.decode("utf-8"))
        collection_item = Collection.objects.get(id=item_id)
        if data['title']:
            collection_item.title = data['title']

        if data['description']:
            collection_item.description = data['description']

        collection_item.save()

        
        movies_list = []
        movies = data.get('movies')
             
        for x in movies :

                m_title = x.get('title')
                
                m_description =  x.get('description') ,
                genres = x.get('genres'),
                uuid = x.get('uuid')

                movieData = {
                    'title':m_title,
                    'description':m_description,
                    'genres': genres,
                    'uuid':uuid
                }

                movie_item = Movie.objects.create(**movieData)

                movie_item.collection.add(collection_item)
                movies_list.append(movie_item)

        response_data = {
        'title':collection_item.title,
        'description':collection_item.description,
        'movies':movies
            }
         
        
        

        return JsonResponse(response_data)
    