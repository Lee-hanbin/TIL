from rest_framework import serializers

from .models import Movie, Actor, Review

##################################전체##############################################
class ActorSerListializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

class MoiveListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title','content',)

##################################참조###############################################
class Moivetitle(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)

class Actorname(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name',)

####################################단일#############################################
class ActorSerializer(serializers.ModelSerializer):
    # movie_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    movies = Moivetitle(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = '__all__'

class MoiveSerializer(serializers.ModelSerializer):
    actors = Actorname(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    # read_only를 하여 if문을 넘겨줌
    movie = Moivetitle(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'