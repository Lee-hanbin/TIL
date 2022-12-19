from turtle import update
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10) #필드이름 = 타입(최대 길이 = 10)
    content = models.TextField()            # CharField는 길이가 제한적이지만 TextField는 길이제한이 유함
    # PK는 자동 생성되기에 따로 지정 x
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.title