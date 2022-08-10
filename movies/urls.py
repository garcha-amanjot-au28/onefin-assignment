from django.urls import path , include
from . import views
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import include

#URLconf
urlpatterns = [
    # path('movies/', views.get_movies),
    # path('collections/', views.MovieCollections.as_view()),
    # path('register/', views.register_user),
    # url(r'^api-token-auth/', obtain_jwt_token)
    path('',views.MovieCollections.as_view()),
    path('<int:item_id>', views.MovieCollectionsUpdate.as_view())
]