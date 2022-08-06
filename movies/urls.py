from django.urls import path , include
from . import views
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import include, url

#URLconf
urlpatterns = [
    path('movies/', views.get_movies),
    path('collections/', views.get_collections),
    path('register/', views.register_user),
    url(r'^api-token-auth/', obtain_jwt_token)

    
]