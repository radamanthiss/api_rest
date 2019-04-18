from rest_framework import serializers
from django.contrib.auth.models import User
from movies.models import Movie


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id','username','password','is_staff')
	
class MovieSerializer(serializers.ModelSerializer):

	class Meta:
		model = Movie
		fields = ('id','titulo','genero','calificacion','fecha_lanzamiento')
		



