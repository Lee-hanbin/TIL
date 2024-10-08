from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField, ImageSpecField
from django.db import models
from django.conf import settings



def articles_image_path(instance, filename):
    return f'image/{instance.user.username}/{filename}'


# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True)
    # 스키마에 생성되지 않는 걸보니 물리적인 colunm은 아니네!!
    image_thumnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(200,300)],
        format='JPEG',
        options={'quality': 80},
    )
    # image = models.ImageField(blank=True, upload_to = 'images/')
    # image = models.ImageField(blank=True, upload_to = '%Y/%m/%d/')
    # image = models.ImageField(blank=True, upload_to =articles_image_path)
    # image = ProcessedImageField(
    #     blank=True,
    #     upload_to='thumbnails/',
    #     processors=[Thumbnail(200,300)],
    #     format='JPEG',
    #     options={'quality': 80},
    # )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content