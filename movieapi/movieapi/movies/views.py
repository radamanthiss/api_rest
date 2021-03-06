from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from movies.serializers import UserSerializer, MovieSerializer
from django.contrib.auth.models import User
from movies.models import Movie



# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer


