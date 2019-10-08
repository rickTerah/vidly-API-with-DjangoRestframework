from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    GenreListView,
    MovieViewSet,
    CustomerViewSet,
    RentalViewSet,
    UserCreateView,
    LoginView
)

app_name = 'vidly'

router = DefaultRouter()
router.register('movies', MovieViewSet, base_name="movies")
router.register('customers', CustomerViewSet, base_name="customers")
router.register('rentals', RentalViewSet, base_name="rentals")

urlpatterns = [
    path('genres/', GenreListView.as_view(), name="genre_list"),
    path('users/', UserCreateView.as_view(), name="user_create"),
    path('login/', LoginView.as_view(), name="login"),
    path('movies/inGenre/<int:genre_id>', MovieViewSet.as_view({"get":'get_movies_from_genre'})),
]
urlpatterns += router.urls