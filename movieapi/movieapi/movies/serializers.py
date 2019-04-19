from rest_framework import serializers
from django.contrib.auth.models import User
from movies.models import Movie
from django.contrib.auth import get_user_model



#class UserSerializer(serializers.ModelSerializer):

	#class Meta:
		#model = User
		#fields = ('id','username','password','is_staff')
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password','is_superuser', 'email', 'first_name', 'last_name', 'is_staff')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            is_superuser = validated_data['is_superuser'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_staff=validated_data['is_staff']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


	
class MovieSerializer(serializers.ModelSerializer):

	class Meta:
		model = Movie
		fields = ('id','titulo','genero','calificacion','fecha_lanzamiento')
		

