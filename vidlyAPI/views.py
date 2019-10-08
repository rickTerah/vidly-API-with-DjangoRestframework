from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import (
    GenreSerializer,
    MovieSerializer,
    CustomerSerializer,
    RentalSerializer,
    UserSerializer
)
from .models import (
    Genre,
    Movie,
    Customer,
    Rental,
)

# Create your views here.
class GenreListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(methods=['GET'], detail=False, url_path='inGenre/<int:genre_id>/')
    def get_movies_from_genre(self, request, genre_id, *args, **kwargs):
        movies = Movie.objects.filter(genre_id=genre_id)
        data = MovieSerializer(movies, many=True).data
        return Response(data)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    authentication_classes = ()
    permission_classes = ()
    serializer_class = CustomerSerializer

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": 'Wrong credentials'}, status=status.HTTP_400_BAD_REQUEST)
