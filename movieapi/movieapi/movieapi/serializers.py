from rest_framework import serializers
from django.contrib.auth.models import User
from movies.models import Movie


class UserSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = User
		fields = ('username','password')
	
class MovieSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Movie
		fields = ('id','titulo','genero','calificacion','fecha_lanzamiento')
		



