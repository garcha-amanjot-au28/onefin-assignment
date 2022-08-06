from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User
from .serializers import UserSerializer , CreateUserSerializer
from .services import  get_Movies
from django.contrib.auth import get_user_model  
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


@api_view(['POST'])
@permission_classes([AllowAny])
def user_create(request):
    if request.method == 'POST':
        print(request.data)
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, safe=False)



def get_movies(request):
    
    movies = get_Movies()
    return JsonResponse(movies, safe=False)

def get_collections(request):
    return HttpResponse('Collections List')


def register_user(request):
    users = get_user_model().objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)
    # get all the users 
    # serialize them
    # return json
    