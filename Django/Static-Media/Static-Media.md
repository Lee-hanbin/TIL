# Static/Media

22/10/11  

# Managing static files

## Static files

### 개요

- 개발자가 서버에 미리 준비한 혹은 사용자가 업로드한 정적파일을 클라이언트에게 제공하는 방법

### 정적 파일

- 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
  - 사용자의 요청에 따라 내용이 바뀌는 것이 아니라 요청한 것을 그대로 보여주는 파일
- `파일 자체가 고정` 되어 있고, 서비스 중에도 추가되거나 `변경되지 않고 고정` 되어있음
- Django에서는 이러한 파일들을 `static file` 이라고 함
  - Django는 staticfiles 앱을 통해 정적 파일과 관련된 기능을 제공

### Media File

- 미디어 파일
- 사용자가 웹에서 업로드 하는 정적 파일
- 유저가 업로드 한 모든 정적 파일

⇒ static 파일의 부분집합

### 웹 서버와 정적 파일

- 웹 서버의 기본동작
  - 특정 위치(`URL`)에 있는 자원을 요청(`HTTP request`) 받아서 응답(`HTTP response`)을 처리하고 제공(`serving`) 하는 것
- 자원과 자원에 접근 가능한 주소가 있음을 의미
- 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원(`static resource`)을 제공

## static files 구성하기

### Django에서 정적파일을 구성하고 사용하기 위한 단계

1. ISTALLED_APP에 django.contrib.staticfiles가 포함되어 있는지 확인

2. settings.py에서 `STATIC_URL` 을 정의하기

3. 앱의 static 폴더에 정적 파일을 위치하기
   
    ex) `my_app/static/sample_img.jpg`

4. 템플릿에서 static 템플릿 태그를 사용하여 지정된 경로에 있는 정적 파일의 URL 만들기
   
   ```python
   {% load static %}
   
   <img src="{% 'sample_img.jpg %}" art="sample image">
   ```

### Django template tag

- `{% load %}`
  - load tag
  - 특정 라이브러리, 패키지에 등록된 모든 템플릿 태그와 필터를 로드
- `{% static '' %}`
  - static tag
  - STATIC_ROOT에 저장된 정적 파일에 연결

### Static files 관련 Core Settings

1. STATIC_ROOT 
   
   ```python
   static 파일들은 배포 시 사용자가 사용할 수 없음
   => STATIC_ROOT를 통해 접근 가능하게 한다
   
   # settings.py
   
   STATIC_ROOT = BASE_DIR / 'staticfiles'
   
   $ python manage.py collectstatic
   ```
   
   - Default : None
   - Django 프로젝트에서 사용하는 모든 정적 파일을 한곳에 모아 넣는 경로
   - `collectstatic`이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
   - `개발 과정에서 [setting.py](http://setting.py)의 DEBUG 값이 True로 설정되어 있으면 해당 값은 작용되지 않음`
   - 실 서비스 환경(`배포 환경`)에서 Django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위해 사용
   - 배포 환경에서는 Django에 내장되어 있는 정적 파일들을 인식하지 못함 (`내장되어 있는 정적 파일들을 밖으로 꺼내는 이유`)

2. STATICFILES_DIRS
   
   - Default : [] (empty list)
   
   - `app/static/` 디렉토리 경로를 사용하는 것(기본경로) 외에 추가적인 정적 파일 경로 목록을 정하는 리스트
   
   - 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성되어야 함
     
     ```python
     # settings.py
     
     STATICFIELS_DIRS = [
       BASE_DIR / 'static',
     ]
     ```

3. STATIC_URL (`이게 중요! 이건 작성되어 있음`)
- Default: None
- STATIC_ROOT에 있는 정적 파일을 참조 할 때 사용할 URL
- 개발 단계에서는 실제 정적 파일들이 저장되어 있는 app/static/ 경로 및 STATICFILES_DIRS에 정의된 추가 경로들을 탐색
- `실제 파일이나 디렉토리가 아니며, URL로만 존재`
- 비어 있지 않은 값으로 설정 한다면 반드시 slash(`/`)로 끝나야함

## Static files 실습

### static file 가져오기

- static file을 가져오는 방법
  
  1. 기본 경로에 있는 static file 가져오기
     
      ⇒ `app/static/,,,`
  
  2. 추가 경로에 있는 static file 가져오기
     
      ⇒ `STATICFILES_DIR에서 가져옴`

### 1. 기본 경로에 있는 static file 가져오기

1. articles/static/articles 경로에 이미지 파일 배치하기
   
    ![static.PNG](Static%20Media%20659f322185b148f490dd03dd577d600e/static.png)

2. startic tag를 사용해 이미지 파일 출력하기
   
   ```html
   {% extends 'base.html' %}
   <!-- 추가 -->
   {% load static %}    
   
   {% block content %}
       <!-- 추가 -->
     <img src="{% static 'articles/다운로드 (1).jpg' %}" alt="sample img">
     <h1>Articles</h1>
     <!-- 생략 -->
   {% endblock content %}
   ```

### 2. 추가 경로에 있는 static file 가져오기

1. 추가 경로 작성
   
   ```html
   # setting.py
   
   STATICFILES_DIRS = [
       BASE_DIR / 'static',
   ]
   ```

2. statc/경로에 이미지 파일 배치 
   
    ![static2.PNG](Static%20Media%20659f322185b148f490dd03dd577d600e/static2.png)

3. static tag를 사용해 이미지 파일 출력
   
   ```html
   {% extends 'base.html' %}
   {% load static %}
   
   {% block content %}
     <img width = 200 src="{% static 'articles/다운로드 (1).jpg' %}" alt="sample img">
     <img width = 325 src="{% static '다운로드.jpg' %}" alt="sample img2">
     <h1>Articles</h1>
       <!-- 생략 -->
   {% endblock content %}
   ```

## Image Upload

### 개념

- Django ImangeField를 사용해 사용자가 업로드한 정적 파일(`미디어 파일`) 관리하기

### ImageField()

- 이미지 업로드에 사용하는 모델 필드
- FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용 가능
- 더해서 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사
- ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성됨
  - max_length 인자를 사용하여 최대 길이를 변경 가능

### FileField()

`FileField(upload_to=’ ‘, storage=None, max_length=100, **options)`

- 파일 업로드에 사용하는 모델 필드
- 2개의 선택 인자를 가지고 있음
  1. upload_to
  2. storage

### FileField/ImageField를 사용

```python
1. setting.py MEDIA_ROOT, MEDIA_URL 설정
2. upload_to 속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT의 하위 경로 지정
    (선택사항)
```

- MEDIA_ROOT
  
  - Default: ‘’(empty string)
  
  - 사용자가 업로드 한 파일들을 보관할 디렉토리의 절대 경로
  
  - Django는 성능을 위해 업로드 파일은 데이터베이스에 저장 x
    
    - 데이터베이스에 저장되는 것은 `파일 경로`
      
      ⇒ 이미지를 넣는 게 아니라 경로를 넣어줌
  
  - MEDIA_ROOT는 STATIC_ROOT와 반드시 다른 경로로 지정
    
    ```python
    # settings.py
    
    MEDIA_ROOT = BASE_DIR / 'media'
    ```

- MEDIA_URL
  
  - Default: ‘’(empty string)
  
  - MEDIA_ROOT에서 제공되는 미디어 파일을 처리하는 URL
  
  - 업로드 된 파일의 주소(URL)를 만들어 주는 역할
    
    - 웹 서버 사용자가 사용하는 public URL
  
  - 비어 있지 않은 값으로 설정 한다면 반드시 slash(`/`) 로 끝
  
  - MEDIA_URL은 STATIC_URL과 반드시 다른 경로로 지정
    
    ```python
    # settings.py
    
    MEDIA_URL = '/media/'
    ```

### 개발 단계에서 사용자가 업로드한 미디어 파일 제공

- 사용자로부터 업로드 된 파일이 프로젝트에 업로드 되고나서, 실제로 사용자에게 제공하기 위해서는 업로드 된 파일의 URL이 필요함
  
  ```python
  #crud/urls.py
  
  from django.contrib import admin
  from django.urls import path, include
  from django.conf import settings
  from django.conf.urls.static import static
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls')),
      path('accounts/', include('accounts.urls')),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  
  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  # 잘보자 STATIC 아니고 MEDIA야 ㅠㅠㅠ
  ```
  
  - 업로드 된 파일의 URL == settings.MEDIA_URL
  - 위 URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT

## CREATE

### ImageField 작성

```python
# articles/models.py

from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
        ####################### 생략 ####################
    image = models.ImageField(blank=True)
        ####################### 생략 ####################
    def __str__(self):
        return self.title
```

### Model field option

- Model field option 중 아래 2가지 사항 알아보기
  
  1. blank
     
     - Default : False
     - True인 경우 필드를 비워 둘 수 있음
       - 이 경우, DB에는 ‘’ (빈 문자열) 저장
     - 유효성 검사에서 사용 됨(is_valid)
       - `Validation-related`
       - 필드에 blank=True가 있으면 form 유효성 검사에서 빈 값을 입력할 수 있음
  
  2. null
     
     - Default : False
     - True인 경우 Django는 빈 값을 DB에 NULL로 저장
       - ‘Database-related’
     
     ```python
     문자열 => '' 로 빈값 표시 (ImageField도 문자열기반)
     
     다른필드 => NULL로 빈값 표시
     ```

### Migrations

- ImageField를 사용하려면 반드시 Pillow 라이브러리 필요
  
  - Pillow 설치 없이는 makemigrations 실행 불가
    
    ```bash
    $ pip install Pillow
    
    $ python manage.py makemigrations
    $ python manage.py migrate
    
    $ pip freeze > requirements.txt
    ```

- form 변경
  
  ```python
  from django import forms
  from .models import Article, Comment
  
  class ArticleForm(forms.ModelForm):
  
      class Meta:
          model = Article
  ############image 추가하거나####################
          fields = ('title', 'content', 'image',)
          # exclude = ('title',)
  ############user만 빼준다 (외래키만)###############
                  # exclude = ('user',)
  ```

### ArticleForm에서 image 필드 출력 확인

- 확인 후 이미지를  첨부하여 게시글 작성 시도

- 이미지 업로드 불가
  
    ⇒ form 태그에 enctype 속성을 다음과 같이 변경
  
  ```html
  <!-- articles/create.html -->
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>CREATE</h1>
  <!-- enctype 추가 -->
    <form action="" method="POST" enctype="multipart/form-data">
  <!-- 생략 -->
  {% endblock content %}
  ```

`[참고]`

```python
# form 태그의 enctype(인코딩) 속성 값
1. aplication/x-www-form-urlencoded
 - 기본 값
 - 모든 문자 인코딩
2. multipart/form-data
 - 파일/이미지 업로드 시에 반드시 사용
 - 전송되는 데이터의 형식을 지정
 - <input type="file">을 사용할 경우 사용
3. text/plain
```

### request.FILES

- `파일 및 이미지`는 request의 POST 속성 값으로 넘어가지 않고 `FILES 속성 값`에 담겨 넘어감

```python
# articles/views.py

@login_requried
@require_http_method(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
```

⇒ media 폴더 생성되면 성공! (& db에 생성)

⇒ 같은 이름의 이미지 파일 업로드 ⇒ 장고가 알아서 난수 생성

![이미지.PNG](Static%20Media%20659f322185b148f490dd03dd577d600e/%25EC%259D%25B4%25EB%25AF%25B8%25EC%25A7%2580.png)

## READ

### 업로드 이미지 출력하기

- 업로드 된 파일의 상대 URL은 Django가 제공하는 url 속성을 통해 얻을 수 있음
  
  ```html
  {% extends 'base.html' %}
  
  {% block content %}
    <!-- image의 주소를 할당 -->
      <img src="{{ article.image.url }}" alt="{{ article.image }}">  
  
    <h2>DETAIL</h2>
    <h3>{{ article.pk }} 번째 글</h3>
  <!-- 생략 -->
  {% endblock content %}
  ```
  
  - article.image.url : 업로드 파일의 경로
  - article.image : 업로드 파일의 파일 이름

## Update

### 개요

- 이미지는 바이너리 데이터이기 때문에 텍스트처럼 일부만 수정 하는 것은 불가능
  
    ⇒ 새로운 사진으로 대체하는 방식을 사용

### 업로드 이미지 수정하기

- enctype 속성값 추가
  
  ```html
  <!-- update.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>UPDATE</h1>
      <!-- enctype 추가 -->
    <form action="{% url 'articles:update' article.pk %}" 
  method="POST" enctype="multipart/form-data">
   <!-- 생략 -->
  {% endblock content %}
  ```

- 이미#지 파일이 담겨있는 request.FILES 추가 작성
  
  ```python
  # aticles/view.py
  
  @login_required
  @require_http_methods(['GET', 'POST'])
  def update(request, pk):
      article = Article.objects.get(pk=pk)
      if request.user == article.user:
          if request.method == 'POST':
                          ###### request.FILES 추가######
              form = ArticleForm(request.POST, request.FILES, instance=article)
      ###############생략#####################
      return render(request, 'articles/update.html', context)
  ```
  
  - request.FILES가 없으면 사진이 저장되지 않는다

## upload_to argument

### 사용자 지정 업로드 경로와 파일 이름 정하기

- ImageField는 업로드 디렉토리와 파일 이름을 설정하는 2가지 방법 제공
  
  1. 문자열 값이나 경로 지정 방법
     
     1. upload_to 인자에 새로운 이미지 경로 추가
        
        ```python
        #articles/model.py
        
        # image = models.ImageField(blank=True)
        image = models.ImageField(blank=True, upload_to = 'images/')
        ```
        
        (makemigrations & migrate)
        
        ![이미지경로.PNG](Static%20Media%20659f322185b148f490dd03dd577d600e/%25EC%259D%25B4%25EB%25AF%25B8%25EC%25A7%2580%25EA%25B2%25BD%25EB%25A1%259C.png)
        
        ⇒ media 폴더 안에 image 폴더에 이미지 저장(경로 생성)
     
     2. 단순 문자열 뿐만 아니라 파이썬 time 모듈의 strtime()형식도 포함 될 수 있음. (`날짜/시간`으로 대체됨)
        
        ```python
        #articles/model.py
        
        image = models.ImageField(blank=True, upload_to = '%Y/%m/%d/')
        ```
        
        ![이미지 경로2.PNG](Static%20Media%20659f322185b148f490dd03dd577d600e/%25EC%259D%25B4%25EB%25AF%25B8%25EC%25A7%2580_%25EA%25B2%25BD%25EB%25A1%259C2.png)
        
        ⇒ media 폴더 안에 `년도폴더/월 폴더/ 일 폴더`에 저장
  
  2. 함수 호출 방법
     
     - upload_to는 독특하게 함수처럼 호출이 가능하며 해당 함수가 호출되면서 반드시 2개의 인지를 받음
       
       ```python
       #articles/model.py
       def articles_image_path(instance, filename):
         return f'image/{instance.user.username}/{filename}'
       
       image = models.ImageField(blank=True, upload_to =articles_image_path)
       ```
       
       ![이미지 경로3.PNG](Static%20Media%20659f322185b148f490dd03dd577d600e/%25EC%259D%25B4%25EB%25AF%25B8%25EC%25A7%2580_%25EA%25B2%25BD%25EB%25A1%259C3.png)
       
       ⇒  로그인된 `유저명 폴더 생성 후, 저장`

## Image Resizing

### 개요

- 실제 원본 이미지를 서버에 그대로 로드 하는 것은 여러 이유로 부담이 큼
- HTML <img> 태그에서 직접 사이즈를 조정할 수도 있지만, 업로드 될 때 이미지 자체를 resizing 하는 것을 사용해 볼 것

### 사전 준비

- 모듈 설치
  
  ```python
  $ pip install django-imagekit
  $ pip freeze > requirements.txt
  ```
  
  ```python
  #crud/settings.py
  INSTALLED_APPS = [
          # 생략 #
      'imagekit',
          # 생략 #
  ]
  ```

### 썸네일 만들기

- 2가지 방식으로 썸네일 만들기 진행
  
  1. 원본 이미지 저장 `X`
     
     ```python
     #articles/model.py
     
     from imagekit.processors import Thumbnail
     from imagekit.models import ProcessedImageField
     
     # Create your models here.
     class Article(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      title = models.CharField(max_length=10)
      content = models.TextField()
        #########추가#########
      image = ProcessedImageField(
          blank=True,
          upload_to='thumbnails/',
          processors=[Thumbnail(200,300)],
          format='JPEG',
          options={'quality': 80},
      )
        #########추가#########
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
     
      def __str__(self):
          return self.title
     ```
     
     ⇒ 화질이 안 좋아지고 기존 이미지가 잘린 느낌
  
  2. 원본 이미지 저장 `O`
     
     ```python
     #articles/model.py
     
     from imagekit.processors import Thumbnail
     from imagekit.models import ProcessedImageField, ImageSpecField
     
     # Create your models here.
     class Article(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      title = models.CharField(max_length=10)
      content = models.TextField()
        #########추가#########
     # 스키마에 생성되지 않는 걸보니 물리적인 colunm은 아니네!!
      image_thumnail = ImageSpecField(
          source='image',
          processors=[Thumbnail(200,300)],
          format='JPEG',
          options={'quality': 80},
        #########추가#########
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
     
      def __str__(self):
          return self.title
     ```
     
     ⇒ 이 상태로 새로운 이미지 업로드 하면 원본 파일만 올라감
     
     ```html
     <!-- detail.html -->
     
     <img src="{{ article.image_thumnail.url }}" alt="{{ article.image_thumnail }}">
     ```
  - 업로드 시 리사이징 된 이미지가 새로 생성됨
    
    ![원본유지썸네일.PNG](Static%20Media%20659f322185b148f490dd03dd577d600e/%25EC%259B%2590%25EB%25B3%25B8%25EC%259C%25A0%25EC%25A7%2580%25EC%258D%25B8%25EB%2584%25A4%25EC%259D%25BC.png)
    
    ![원본유지썸네일2.PNG](Static%20Media%20659f322185b148f490dd03dd577d600e/%25EC%259B%2590%25EB%25B3%25B8%25EC%259C%25A0%25EC%25A7%2580%25EC%258D%25B8%25EB%2584%25A4%25EC%259D%25BC2.png)