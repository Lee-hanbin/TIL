from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id','title', 'content')      #all 해도 상관없음

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)     # 읽기 전용 필드로 바꿔줌

class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set =CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    # article.comment_set.count() => comment_set.count
    # ArticleSerializer 이므로 article 생략하고 문자열이니까 () 생략
    class Meta:
        model = Article
        fields = '__all__'
