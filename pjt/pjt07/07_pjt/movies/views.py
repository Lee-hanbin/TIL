from django.shortcuts import get_list_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from .serializers import ActorSerializer, ActorSerListializer, MoiveListSerializer, MoiveSerializer, ReviewListSerializer, ReviewSerializer
from .models import Actor, Movie, Review
from movies import serializers

# Create your views here.

@api_view()
def actor_list(request):
    actors = Actor.objects.all()
    serializers = ActorSerListializer(actors, many=True)
    return Response(serializers.data)

@api_view()
def artor_detail(request, actor_pk):
    actor = Actor.objects.get(pk=actor_pk)
    serializers = ActorSerializer(actor)
    return Response(serializers.data)

@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializers = MoiveListSerializer(movies, many=True)
    return Response(serializers.data)

@api_view()
def moive_detail(requst, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializers = MoiveSerializer(movie)
    return Response(serializers.data)

@api_view()
def review_list(request):
    reviews = Review.objects.all()
    serializers = ReviewListSerializer(reviews, many=True)
    return Response(serializers.data)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    if request.method == 'GET':
        serializers = ReviewSerializer(review)
        return Response(serializers.data)
    
    elif request.method == 'PUT':
        serializers = ReviewSerializer(review, data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)
    
    elif request.method == 'DELETE':
        review.delete()
        message_d = f'review {review_pk} is deleted'
        return Response(message_d, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_review(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializers = ReviewSerializer(data=request.data)
    if serializers.is_valid(raise_exception=True):
        # serializers.save()
        serializers.save(movie=movie)
        return Response(serializers.data, status=status.HTTP_201_CREATED)