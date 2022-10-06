# 22/10/05

# 데이터베이스 관계

## 개요

- 관계형 데이터베이스에서의 외래 키 속성을 사용해 모델간 N:1 관계 설정하기
- `외래 키` 를 사용하여 각 행에서 서로 다른 테이블 간의 `관계`를 만드는 데 사용할 수 있음
- N:1
    - Many-to-one relationships
    - 한 테이블(`주문`)의 0개 이상의 레코드가 다른 테이블(`고객`)의 레코드 한 개와 관련된 경우
    - 기준 테이블에 따라(1:N) 이라고도 함
- M:N
    - Many-to-many relationships
    - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
    - 양쪽 모두에서 N:1 관계를 가짐
    

## Foreign Key

- 개념
    - 외래 키
    - 관계형 데이터베이스에서 한 테이블의 필드(`주문`) 중 다른 테이블(`고객`)의 행을 식별할 수 있는 키
    - 참조하는 테이블에서 1개의 키에 해당하고, 이는 참조되는 측 테이블의 기본 키(PK)를 가리킴
    - 참조하는 테이블의 행 1개의 값은, 참조되는 측 테이블의 행 값에 대응됨
        - 이 때문에 참조하는 테이블의 행에는, 참조되는 테이블에 나타나지 않는 값을 포함할 수 없음
    - 참조하는 테이블 행 여러 개가, 참조되는 테이블의 동일한 행을 참조할 수 있음
- 특징
    - 키를 사용하여 부모 테이블의 유일한 값을 참조 (`참조 무결성`)
    - 외래 키의 값이 반드시 부모 테이블의 기본 키 일 필요는 없지만 유일한 값이어야 함
- 참조 무결성
    - 데이터베이스 관계 모델에서 관련된 2개의 데이블 간의 일관성을 말함
    - 외래 키가 선언된 테이블의 외래 키 속성의 값은 그 테이블의 부모가 되는 테이블의 기본 키 값으로 존쟂

`사전작업`

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

# N:1 (`Comment-Article`)

## 개요

- Comment(N) - Article(1)
    - Comment 모델과 Article 모델 간 관계 설정
- `0개 이상의 댓글은 1개의 게시글에 작성 될 수 있음`

## 모델 관계 설정

- 게시판의 게시글과 N:1 관계를 나타낼 수 있는 댓글을 구현
- N:1 관계에서 댓글을 담당할 Comment 모델은 N, Article 모델은 1

## Django Relationship fields

### 종류

1. OneToOneField()
    - A one-to-one relationship
2. ForeignKey()
    - A many-to-one relationship
3. ManyTomanyField()
    - A many-to-many relationship

### `ForeignKey(to, on_delete, **options)`

- A many-to-one relationship을 담당하는 Django의 모델 필드 클래스
- Django 모델에서 관계형 데이터베이스의 외래 키 속성을 담당
- 2개의 필수 위치 인자가 필요
    1. `to` ⇒ 참조하는 `model class`
    2. `on_delete` 옵션
       
        ```python
        #on_delete
        '''
        - 외래 키가 참조하는 객체가 사라졌을 때, 외래키를 가진 객체를 어떻게 처리할 지를 정의
        - 데이터 무결성을 위해서 #매우 중요한# 설정
        - on_delete 옵션 값
          - CASCADE : 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
          - PROTECT : 댓글있으면 게시글 못 지움
          - SET_NULL : 게시글을 지우면 댓글을 모두 NULL로 바꿈
          - SET_DEFAULT : 무언가 지워졌을 때 default 값 설정
        	...등 여러 옵션 값들이 존재
          - 수업에서는 CASCADE 값만 사용
        '''
        ```
        

### Comment Model

- Commnet 모델 정의
  
    ```python
    class Comment(models.Model):
        article = models.ForeignKey(Article, on_delete=models.CASCADE)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    
        def __str__(self):
            return self.content
    ```
    
    - 외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계없이 `필드의 마지막에 작성됨`
    - ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장
    

[참조]

```python
#데이터 무결성
1. 데이터의 정확성과 일관성을 유지하고 보증하는 것
2. 데이터베이스나 RDBMS의 중요한 기능
3. 무결성 제한의 유형
	- 개체 무결성
	- 참조 무결성
	- 범위 무결성
```

- Migration 과정 진행
  
    ```python
    models.py 저장
    python manage.py makemigrations  # 설계도 생성
    python manange.py migrate     # db에 설계도 연동
    ```
    
    - models.py에서 모델을 수정했으므로 migration 과정 진행
    - 마이그레이션 파일 0002_comment.py 생성 확인
    - migrate 진행
    - FoeignKey 모델 필드로 인해 작성된 컬럼의 이름이 `article_id` 임을 확인
      
        ⇒ 클래스 이름의 소문자로 작성하는 것이 권장된 이유!
        
    
    (`article`이라고 지정해야지 `article_id`로 지정 시`article_id_id` )
    

[참조]

```bash
$ python manage.py sqlmigrate articles 0002
```

이 명령어를 통해 Migrationdl 넘어가는 과정을 sql문을  통해 보여줌

- 댓글 생성 연습하기
    - shell_plus 실행
      
        `$ python manage.py shell_plus` 
    1. 댓글 생성
       
        ```bash
        comment = Comment()                # Commnet 클래스의 인스턴스 comment 생성
        comment.content = 'first comment'  # 인스턴스 변수 저장
        comment.save()                     # DB에 댓글 저장
        => error 발생
        => IntegrityError: NOT NULL constraint failed: articles_comment.article_id
          ( NOT NULL 제약 조건 실패 = article_id 에 NULL 값이 들어감)
        => 어떤 게시글에 댓글을 적어주는 지 안 써줌
        
        # 게시글 생성
        article = Article.objects.create(title='title', content='content')
        article.pk                # pk = 1
        comment.article = article # 외래 키 데이터 입력
        comment.save()            # 댓글저장  (error 발생 x)
        comment                   # 댓글 확인
        ```
        
    
    [참고]
    
    ```bash
    comment.article_id  => 직접 comment가 가지고 있는  column의 값을 가져옴
    
    comment.article.pk  => article 테이블에 있는 pk를 가져옴
    ```
    
    1. 댓글 속성 값 확인
       
        ```bash
        # 클래스 변수명인 article로 조회 시 해당 참조하는 게시물 객체 조회 가능
        comment.article   #<Article: title>
        
        # article_pk는 존재하지 않는 필드이기 때문에 사용 불가
        comment.article_id  #1
        ```
        
    1. comment 인스턴스를 통한 article 값 접근하기
       
        ```bash
        # 1번 댓글이 작성된 게시물의 pk 조회
        comment.article.pk #1
        
        # 1번 댓글이 작성된 게시물의 content 조회
        comment.article.content #content
        ```
        
    1. 두 번째 댓글 작성해보기
       
        ```bash
        comment = Comment(content='second comment', article=article)
        comment.save()
        comment.pk
        ```
        

## 관계 모델 참조

### Related manageer

- N:1 혹은 M:N 관계에서 사용 가능한 문맥 (context)
- Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 `역참조` 할 때에 사용할 수 있는 manager를 생성
    - 우리가 이전에 모델 생성 시 `onjects` 라는 매니저를 통해 queryset api를 사용했던 것처럼 related manager를 통해 queryset api를 사용할 수 있게 됨
- 지금은 N:1 관계에서의 related manager 만을 학습할 것

```bash
N -> 1을 참조하지만, 1 -> N을 참조하지 않음
따라서 1 -> N을 참조할 수 있도록 하는 것이 역참조!
```

### 역참조

- 나를 참조하는 테이블(`나를 외래키로 지정한`)을 참조하는 것
- 즉, 본인을 외래 키로 참조 중인 다른 테이블에 접근하는 것
- N:1 관계에서는 1이 N을 참조하는 상황
    - 외래 키를 가지지 않은 1이 외래 키를 가진 N을 참조

### `article.comment_set.method()`

- Article 모델이 Comment 모델을 참조(`역참조`)할 때 사용하는 매니저
- `article.comment` 형식으로는 댓글 객체를 참조 할 수 없음
    - 실제로 Article 클래스에는 Comment와의 어떠한 관계도 작성되어 있지 않음
- 대신 Django가 역참조 할 수 있는 `comment_set` manager를 자동으로 생성해 `article.comment_set` 형태로 댓글 객체를 참조할 수 있음
- 반면, 참조 상황에서는 실제 ForeignKey 클래스로 작성한 인스턴스가 Comment 클래스의 클래스 변수이기 때문에 `comment.article` 형태로 작성 가능

### Ralated manager 실습

1. shell_plus 실행
   
    `$ python manage.py shell_plus`
    
2. 1번 게시글 조회하기
   
    `article = Article.objects.get(pk=1)`
    
3. `dir()` 함수를 사용해 클래스 객체가 사용할 수 있는 메서드를 확인
   
    ```shell
    dir(article)
    ...
    'comment_set',
     'content',
     'created_at',
     'date_error_message',
     'delete',
     'from_db',
     'full_clean',
    ...
    ```
    
4. 1번 게시글에 작성된 모든 댓글 조회하기 (`역참조`)
   
    ```shell
    article.comment_set.all()
    # <QuerySet [<Comment: first comment>, <Comment: second comment>]>
    ```
    
5. 1번 게시글에 작성된 모든 댓글 출력하기
   
    ```python
    comments = article.comment_set.all()
    for comment in comments:
    	print(comment.content)
              
    '''
    first comment
    second comment
    '''
    
    ```
    

### ForeignKey arguments - `related_name`

```python
# articles/models.py

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE, 
                                related_name = 'comment')
		...
```

- ForeigKey 클래스의 `선택 옵션`
    - n:1 에서는 굳이  사용하지 않음 단, n:m에서는 사용
- 역참조 시 사용하는 매니저 이름을 변경할 수 있음
- 작석후, migration 과정이 필요
- 선택 옵션이지만 상황에 따라 반다시 작성해야 하는 경우가 생김
- 작성 후 다시 원래 코드로 복구

### admin site 등록

- admin 계정 생성

  ```bash
  $ python manage.py createsuperuser
  ```

- 새로 작성한 Comment 모델을 admin site에 등록
  
    ```python
    # article/admin.py
    from .models import Article, Commnet
    
    admin.site.register(Article)
    admin.site.register(Comment)
    ```
    
    - 암기법 : admin site에 등록(register) 한다.
- admin 확인
  
    ```python
    1. admin.py 저장
    2. python manage.py runserver
    3. 주소/admin
    ```
    

## Comment 구현

### `CREATE`

- 사용자로부터 댓글 데이터를 입력 받기 위한 CommnetForm 작성
  
    ```python
    # article/forms.py
    from .models improt Article, Comment
    
    class CommentForm(forms.ModelForm):
    		
    	class Meta:
    		model = Comment
    		fields = '__all__`
    ```
    
- detail 페이지에서 CommentForm 출력 (`view 함수`)
  
    ```python
    from .form import ArticleForm, CommentForm
    
    @require_safe
    def detail(request, pk):
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm()###### 여기 추가#######
        context = {
            'article': article,
            'comment_form': comment_form,###### 여기 추가#######
        }
        return render(request, 'articles/detail.html', context)
    ```
    
- detail 페이지에서 CommentForm 출력 (`templates`)
  
    ```html
    {% extends 'base.html' %}
    
    {% block content %}
    	<--...(생략)...-->
      <a href="{% url 'articles:index' %}">뒤로가기</a>
      <hr>
      <--추가 start-->
    	<form action="#" method="POST">
        {% csrf_token %}
        {{comment_form}}
        <input type="submit">
      </form>
      <--추가 end-->
    {% endblock content %}
    ```
    
- detail 창
  
    ![댓글.PNG](22%2010%2005%20436f6ef7739e48158eb183caf54bb688/%25EB%258C%2593%25EA%25B8%2580.png)
    
    ```
    이런식으로 Article이라는 게시글을 지정해서 댓글을 사용하게 함
    이건, 사용자에게 선택권을 줬기 때문!
    사용자가 detail 페이지에 들어왔다는 것은 그 페이지에 댓글을 
    달고자 하는 것이 암묵적인 사실!
    따라서 이러한 기능을 사용자한테 주면 안됨
    => view 함수 내에서 받아 별도로 처리되어 저장되어야 함
    ```
    
- 외래 키 필드를 출력에서 제외 후 확인
  
    ```python
    # articles/forms.py
    
    class CommentForm(forms.ModelForm):
    		
        class Meta:
            model = Comment
            # fields = '__all__'
            exclude = ('article',)########이거 추가#########
    ```
    
    ⇒ `Article 콤보상자 사라짐!`
    
    ![댓글2.PNG](22%2010%2005%20436f6ef7739e48158eb183caf54bb688/%25EB%258C%2593%25EA%25B8%25802.png)
    
- 출력에서 제외된 외래 키 데이터는 어디서 받아와야 하는가!?
  
    ```python
    1. detail 페이지의 url을 살펴보면 path('<int:pk>/', views.detail, name='detail')
    	url에 해당 게시글의 pk 값이 사용 되고 있음
    2. 댓글의 외래 키 데이터에 필요한 정보가 바로 게시글 pk값
    3. 이전에 학습했던 url을 통해 변수를 넘기는 variable routing을 사용
    ```
    
    - articles/urls.py
    
    ```python
    app_name = 'articles'
    urlpatterns = [
    	  ...
    		path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    ]
    ```
    
    - articles/views.py
    
    ```python
    def comments_create(request, pk):
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
        return redirect('article:detail', article.pk)
    ```
    
    - articles/detail.html
    
    ```html
    {% extends 'base.html' %}
    
    {% block content %}
    	<-- ... -->
      <hr>
    	<-- 여기 # 대신 url 적어줌 -->
      <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
        {% csrf_token %}
        {{comment_form}}
        <input type="submit">
      </form>
    {% endblock content %}
    ```
    
    ⇒ `NOT NULL constraint failed; articles_comment.article_id` error
    
- error 발생 이유와 해결
  
    ```python
    원래 shell을 이용하면
    1. comment = Comment()      # 이건 위에서 필요하지 않고
    2. comment.content = 'aaa'  # comment_form = CommentForm(request.POST)
    3. comment.article = article # 이게 존재하지 않아!!!
    4. comment.save()           # 바로 여기로 넘어가니까
    ```
    
- save 메서드의 commit 옵션을 사용해 DB에 저장되기 전 article 객체 저장하기
  
    ```python
    # articles/views
    '''
    따라서 save의 메서드인 commit을 사용한다
    commit은 default값으로 True를 가지고 있다
    여기서 commit 을 False로 바꿔주면 save 하기 전에 틈이 생긴다.
    즉, save 될 값을 먼저 받아서 처리 할 수 있게된다.
    여기서 아직 DB에 저장되지 않은 인스턴스를 반환
    '''
    def comments_create(request, pk):
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
    		comment = comment_form.save(commit =False) # False
    		comment.article = article                  # 추가
    		comment.save()                             # save
        return redirect('articles:detail', article.pk)
    ```
    

### `READ`

- 작성한 댓글 목록 출력하기
- 특정 article에 있는 모든 댓글을 가져온 후 context에 추가
  
    ```python
    # articles/views.py
    
    @require_safe
    def detail(request, pk):
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm()
        comments = article.comment_set.all()    # 이거 추가
        context = {
            'article': article,
            'comment_form': comment_form,
            'comments': comments,              # 이거 추가
        }
        return render(request, 'articles/detail.html', context)
    ```
    
- detail 템플릿에서 댓글 목록 출력하기
  
    ```html
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>DETAIL</h1>
    	<-- 생략 -->
      <a href="{% url 'articles:index' %}">뒤로가기</a>
      <hr>
      <h4>댓글 목록</h4>
      <ul>
        {% for comment in comments %}
          <li>{{comment.content}}</li>  
        {% endfor %}
      </ul>
    	<-- 생략 --> 
    {% endblock content %}
    ```
    
    ![댓글출력.PNG](22%2010%2005%20436f6ef7739e48158eb183caf54bb688/%25EB%258C%2593%25EA%25B8%2580%25EC%25B6%259C%25EB%25A0%25A5.png)
    

### `DELETE`

- 댓글 삭제 구현하기 (url, view)
  
    ```python
    from django.urls import path
    from . import views
    
    app_name = 'articles'
    urlpatterns = [
        path('', views.index, name='index'),
        path('create/', views.create, name='create'),
        path('<int:pk>/', views.detail, name='detail'),
        path('<int:pk>/delete/', views.delete, name='delete'),
        path('<int:pk>/update/', views.update, name='update'),
        path('<int:pk>/comments/', views.comments_create, name='comments_create'),
        # path('<int:comment_pk>/comments/delete/', views.comments_delete, name = 'comments_delete'),
        path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name = 'comments_delete'),
        # 위에 걸로 하면 갑자기 comment가 뜬금없이 나오는 느낌! 
        # 웬만하면 아래 걸로 쓰자!
    ]
    ```
    
    ```python
    # articles/views.py
    from .models import Article, Comment
    
    # def comments_delete(request, comment_pk):
    def comments_delete(request, article_pk, comment_pk):
        comment = Comment.objects.get(pk=comment_pk)
        # article_pk = comment.article.pk
        comment.delete()
        return redirect('articles:detail', article_pk)
    ```
    
- 댓글을 삭제할 수 있는 버튼을 각각 댓글 옆에 출력 될 수 있도록 함
  
    ```html
    <!-- articles/detail.html -->
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>DETAIL</h1>
      <-- 생략 -->
      <h4>댓글 목록</h4>
      <ul>
        {% for comment in comments %}
          <li>
            {{comment.content}}
    <-- 추가 start -->
            <form action="{% url 'articles:comments_delete' article.pk comment.pk %}"
            method="POST">
            {% csrf_token %}
            <input type="sumbit" value="DELETE">
            </form>	
    <-- 추가 end -->
          </li>  
        {% endfor %}
      <-- 생략 -->
    {% endblock content %}
    ```
    
    ![댓글삭제.PNG](22%2010%2005%20436f6ef7739e48158eb183caf54bb688/%25EB%258C%2593%25EA%25B8%2580%25EC%2582%25AD%25EC%25A0%259C.png)
    

### 댓글 수정은 지금 구현 X

- 댓글 수정도 게시글 수정과 마찬가지로 구현 가능
    - 게시글 수정 페이지가 필요했던 것처럼 댓글 수정 페이지가 필요하게 됨
- 하지만 일반적으로 댓글 수정은 수정 페이지로 이동 없이 현재 페이지가 유지된 상태로 댓글 작성 Form 부분만 변경되어 수정 할 수 있도록 함
- 이처럼 페이지의 일부 내용만 업데이트 하는 것은 `JavaScript` 의 영역이기 때문에 `JavaScript` 를 학습한 후 별도로 진행해야 함

## Comment 추가 사항

### 개요

- 댓글에 관련된 아래 2가지 사항을 작성하면서 마무리하기
    1. 댓글 개수 출력하기
        1. DTL filter - `length` 사용
        2. Queryset API - `count()` 사용
    2. 댓글이 없는 경우 대체 컨텐츠 출력하기

### 댓글 개수 출력하기

- DTL filter - `length` 사용
  
    ```html
    <-- 댓글이 있으면 -->
    {% if comments %}
    	<p> {{% comments|length %}} 개의 댓글이 있습니다.</p>
    {% endif %}
    ```
    
- Queryset API - `count()` 사용
  
    ```html
    <-- 댓글이 있으면 -->
    {% if comments %}
        <p>{{ comments.count }} 개의 댓글이 있습니다.</p>
        <p>총 {{ article.comment_set.count}}개</p>  
    {% endif %}
    ```
    

[tip]

- 댓글이 없을 때
  
    ```html
    	{% for comment in comments %}
          <li>
          <-- 생략 -->
          </li>
        {% empty %}
          <li>댓글 없을 무</li>   
        {% endfor %}
    ```
    

# N:1 (Article - User)

## 개요

- Article(N) - User(1)
- Article 모델과 User 모델 간 관계 설정
- `0개 이상의 게시글은 1개의 회원에 의해 작성 될 수 있음`

## Referencing the User model

### Django에서 User 모델을 참조하는 방법

1. settings.AUTH_USER_MODEL
    - 반환 값: `accounts_User`(문자열)
    - User 모델에 대한 외래 키 또는 M:N 관계를 정의 할 때 사용
    - `model.py의 모델 필드에서 User 모델을 참조할 때 사용`
2. get_user_model()
    - 반환 값: `User Object` (객체)
    - 현재 활성화(`active`)된 User 모델을 반환
    - 커스터마이징한 User 모델이 있을 경우는 Custom User 모델, 그렇지 않으면 User 반환
    - `models.py가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용`

⇒ 이건 이해하려고 하지 말고 외우자  

```python
models.py ⇒ settings.AUTH_USER_MODEL
나머지 ⇒ get_user_model()
```

## 모델 관계 설정

### Article과 User간 모델 관계 설정

- `유저의 id`를 가지고 있는 `게시글`
- Article 모델에 User 모델을 참조하는 외래 키 작성
  
    ```python
    from django.conf import settings
    
    # Create your models here.
    class Article(models.Model):
    		# 이거 추가
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    		# ... 
    ```
    

### Migration 진행

- 기존에 존재하던 테이블에 새로운 컬럼이 추가되어야 하는 상황이기 때문에 migrations 파일이 곧바로 만들어지지 않고 일련의 과정이 필요
  
    `$ python manage.py makemigrations`
    
- 바로 설계도가 생성되지 않는다.
  
    ![Migration.PNG](22%2010%2005%20436f6ef7739e48158eb183caf54bb688/Migration.png)
    
    - `모든 column`은 `NOT NULL 제약조건`이 있기 대문에 데이터가 없이는 새로 추가되는 외래 키 필드 user_id가 생성되지 않음
    - 기본 값을 어떻게 작성할 것인지 선택해야 함
    
    ⇒ 1을 입력하고 Enter 진행 (`직접 기본 값 입력`)
    
- 기본 값 입력
  
    ![기본값입력.PNG](22%2010%2005%20436f6ef7739e48158eb183caf54bb688/%25EA%25B8%25B0%25EB%25B3%25B8%25EA%25B0%2592%25EC%259E%2585%25EB%25A0%25A5.png)
    
    - article의 user_id에 어떤 데이터를 넣을 것인지 직접 입력해야 함
    - 마찬가지로 1 입력하고 Eneter 진행
    - 기존에 작성된 게시글이 있다면 모두 1번 회원이 작성한 것으로 처리
- `$ python manage.py migrate`
- article 테이블 스키마 변경 및 확인
  
    SQLITE EXPLORER/ `articles_article`에 `user_id : binint 생성`
    

## `CREATE`

### 개요

- 인증된 회원의 게시글 작성 구현하기
- 작성하기 전 로그인을 먼저 진행한 상태로 진행

### AriticleForm

- ArticleForm 출력을 확인해보면 create 템플릿에서 `불필요한 필드(user)`가 출력됨

![게시글 생성.PNG](22%2010%2005%20436f6ef7739e48158eb183caf54bb688/%25EA%25B2%258C%25EC%258B%259C%25EA%25B8%2580_%25EC%2583%259D%25EC%2584%25B1.png)

- CommentForm에서 외래 키 필드 article이 출력되는 상황과 동일한 상황
- user 필드도 마찬가지로 사용자로부터 받는 것이 아니라 `reques` 를 통해 처리

⇒ `즉, 게시글을 작성할 때, 사용자가 누가 작성할지 정하는 것은 말이 안됨!!!`

- ArticleForm의 출력 필드 수정
  
    ```python
    class ArticleForm(forms.ModelForm):
    
        class Meta:
            model = Article
            # fields = '__all__'  #이거 대신
            exclude = ('user',)   #요거 
    ```
    
    ![게시글생성2.PNG](22%2010%2005%20436f6ef7739e48158eb183caf54bb688/%25EA%25B2%258C%25EC%258B%259C%25EA%25B8%2580%25EC%2583%259D%25EC%2584%25B12.png)
    
    - `뿅` 지워짐! 단, 게시글이 작성되는 것은 아님! ⇒ user 정보 같이 보내와!
- 외래 키 데이터 누락
  
    ![게시글생성3.PNG](22%2010%2005%20436f6ef7739e48158eb183caf54bb688/%25EA%25B2%258C%25EC%258B%259C%25EA%25B8%2580%25EC%2583%259D%25EC%2584%25B13.png)
    
- 게시글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 commit 옵션을 활용
  
    ```python
    # articles/views.py
    @login_required
    @require_http_methods(['GET', 'POST'])
    def create(request):
    		#....생략.....#
            if form.is_valid():
                article = form.save(commit=False)    # 저장하기 전에 인스턴스 받아와서
                article.user = request.user          # 유저 정보 넣고
                article.save()                       # 저장
                return redirect('articles:detail', article.pk)
    		#....생략.....#
        }
        return render(request, 'articles/create.html', context)
    ```
    

## `DELETE`

### 게시글 삭제 시 작성자 확인

- 이제 게시글에는 작성자 정보가 함께 들어있기 때문에 현재 삭제를 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 삭제 할 수 있도록 함
  
    ```python
    # articles/views.py
    @require_POST
    def delete(request, pk):
        article = Article.objects.get(pk=pk)
        if request.user.is_authenticated:
            if request.user == article.user:     # 요거 추가
                article.delete()
                return redirect('articles:index')
        return redirect('articles:detail', article.pk)   # 요거 추가
    ```
    
    - admin을 로그아웃하고, 새로운 아이디로 로그인 하면 게시글이 지워지지 않는다.
        - 내가 쓴 글이 아니기 때문에!!! (오~)

## `UPDATE`

### 게시글 수정 시 작성자 확인

- 수정도 마찬가지로 수정을 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 수정 할 수 있도록 함
  
    ```python
    # articles/views.py
    @login_required
    @require_http_methods(['GET', 'POST'])
    def update(request, pk):
        article = Article.objects.get(pk=pk)
        if request.user == article.user:       # 수정요청 유저와 작성자의 유저가 같으면
            if request.method == 'POST':
                form = ArticleForm(request.POST, instance=article)
                # form = ArticleForm(data=request.POST, instance=article)
                if form.is_valid():
                    form.save()
                    return redirect('articles:detail', article.pk)
            else:
                form = ArticleForm(instance=article)
        else:                           # 다르면 인덱스로 보내버리기
            return redirect('articles:index')
        context = {
            'form': form,
            'article': article,
        }
        return render(request, 'articles/update.html', context)
    ```
    
- 추가로 해당 게시글의 작성자가 아니라면, 수정/삭제 버튼을 출력하지 않도록 함
  
    ```html
    <!--articles/detail.html -->
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>DETAIL</h1>
    	<!-- 생략 -->
      <p>수정 시각 : {{ article.updated_at }}</p>
      <!-- 작성 유저와 수정 유저가 같으면 수정/삭제 버튼 나오게 하기-->
      {% if reqeust.user == article.user %}   
        <a href="{% url 'articles:update' article.pk %}">UPDATE</a>
        <form action="{% url 'articles:delete' article.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="DELETE">
        </form>
      {% endif %}
      <hr>
      <a href="{% url 'articles:index' %}">뒤로가기</a>
    	<!-- 생략 -->
    {% endblock content %}
    ```
    

## `READ`

### 게시글 작성자 출력

- index 템플릿과 detail 템플릿에서 각 게시글의 작성자 출력
  
    ```html
    <!--articles/index.html -->
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>Articles</h1>
    	<!-- 생략 -->
      {% for article in articles %}
        <!--article.user.username으로 써도 무방-->
        <p><b>작성자 : {{article.user}}</b></p>  
    	<!-- 생략 -->
      {% endfor %}
    {% endblock content %}
    ```
    
    ```html
    <!--articles/detail.html -->
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>DETAIL</h1>
      <h2>{{ article.pk }}번째 글입니다.</h2>
      <hr>
      <!--article.user.username으로 써도 무방-->
      <p><b>작성자 : {{article.user}}</b></p>  
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <p>작성 시각 : {{ article.created_at }}</p>
      <p>수정 시각 : {{ article.updated_at }}</p>
    	<!-- 생략 -->
    	<!-- 생략 -->
    {% endblock content %}
    ```
    

# N:1 (Comment - User)

## 개요

- Comment(N) - User(1)
    - Comment 모델과 User 모델 간 관계 설정
- `0개 이상의 댓글은 1개의 회원에 의해 작성 될 수 있음`

## 모델 관계 설정

### Comment와 User간 모델 관계 설정

- `몇 번 게시글`의 `누가 작성한 글`인지
- Comnet 모델에 User 모델을 참조하는 외래 키 작성
  
    ```python
    # articles/models.py
    
    class Comment(models.Model):
        article = models.ForeignKey(Article, on_delete=models.CASCADE)
    	######################추가 ##########################
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        #####################################################
    	content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    
        def __str__(self):
            return self.content
    ```
    

### Migration 진행

- 이전에 User와 Article 모델 관계 설정 때와 마찬가지로 기존에 존재하던 테이블에 새로운 컬럼이 추가되어야 하는 상황이기 때문에 migrations 파일로 곧바로 만들어지지 않고 일련의 과정 필요
  
    `$ python [manage.py](http://manage.py) makemigrations`
    
- 바로 설계도 생성 X
    - 위의 Article-User 와 동일 하게 1→ 1 하여 기본값을 1로 잡아줌
- `$ python [manage.py](http://manage.py) migrate`
- rticle 테이블 스키마 변경 및 확인
  
    SQLITE EXPLORER/ `articles_comment` 에 `user_id : binint 생성`
    

## `CREATE`

### 개요

- 인증된 회원의 댓글 작성 구현하기
- 작성하기 전 로그인을 먼저 진행한 상태로 진행

### CommentForm

- CommentForm 출력을 확인해보면 create 템플릿에서 불필요한 필드(user)가 출력됨
  
    ![댓글(user).PNG](22%2010%2005%20436f6ef7739e48158eb183caf54bb688/%25EB%258C%2593%25EA%25B8%2580(user).png)
    
    - user 필드도 마찬가지로 사용자로부터 받는 것이 아니라 request를 통해 처리해야함
- CommentForm의 출력 필드 수정
  
    ```python
    # articles/forms.py
    
    class CommentForm(forms.ModelForm):
    		
        class Meta:
            model = Comment
            # fields = '__all__'
            exclude = ('article', 'user') #####user추가#####
    ```
    
    ![댓글2(user).PNG](22%2010%2005%20436f6ef7739e48158eb183caf54bb688/%25EB%258C%2593%25EA%25B8%25802(user).png)
    
    - `뿅!` 단, 알다시피 아직 댓글이 작성되지 아니아니~
- 외래 키 데이터 누락
  
    ```python
    def comments_create(request, pk):
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user  # 댓글 작성자의 정보를 저장
            comment.save()
        return redirect('articles:detail', article.pk)
    
    # def comments_delete(request, comment_pk):
    def comments_delete(request, article_pk, comment_pk):
    ```
    

## `READ`

### 댓글 작성자 출력

- detail 템플릿에서 각 게시글의 작성자 출력
  
    ```html
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>DETAIL</h1>
    	<!-- 생략 -->
        {% for comment in comments %}
          <li>
            <!--comment.user : 작성자 - cooment.conetent : 댓글 내용-->
            {{comment.user}} - {{comment.content}}   
            <form action="{% url 'articles:comments_delete' article.pk comment.pk %}"
             method="POST">
              {% csrf_token %}
              <input type="submit" value="DELETE">
            </form>
          </li>
        {% empty %}
          <li>댓글 없을 무</li>   
        {% endfor %}
    	<!-- 생략 -->
    {% endblock content %}
    ```
    

## `DELETE`

### 댓글 삭제 시 작성자 확인

- 이제 댓글에는 작성자 정보가 함께 들어있기 때문에 `현재 삭제를 요청하려는 사람`과 `댓글을 작성한 사람`을 `비교`하여 `본인의 댓글만 삭제` 할 수 있도록 함
  
    ```python
    #articles/views.py
    
    def comments_delete(request, articles_pk, comment_pk):
    	comment = Comment.objects.get(pk=comment_pk)
    	if request.user == comment.user:
    			comment.delete()
    	return redirect('articles:detail', article_pk)
    ```
    
- 추가로 해당 댓글의 작성자가 아니라면, `삭제 버튼` 을 출력하지 않도록 함
  
    ```html
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>DETAIL</h1>
     <!-- 생략 -->
      <ul>
        {% for comment in comments %}
          <li>
            {{comment.user}} - {{comment.content}}   
    				<!-- 삭제자와 작성자가 같으면 삭제할 수 있게 하기 -->
            {% if request.user == comment.user %}
              <form action="{% url 'articles:comments_delete' article.pk comment.pk %}"
              method="POST">
                {% csrf_token %}
                <input type="submit" value="DELETE">
              </form>
            {% endif %}
          </li>
        {% empty %}
          <li>댓글 없을 무</li>   
        {% endfor %}
      </ul>
     <!-- 생략 -->
    {% endblock content %}
    ```
    

# 인증된 사용에 대한 접근 제한하기

## 개요

- `is_authenticated` 와 `View decoratorr` 를 활용하여 코드 정리하기

## 인증된 사용자인 경우만 댓글 작성

```python
@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:   # 인증 받은 유정들만 댓글 작성
		# ... 생략 ... #
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')   # 인증 받지 못했으면 login 페이지로
```

### 인증된 사용자인 경우에만 댓글 작성 상자 나오게 하기

```html
{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL</h1>
  <!-- 생략 -->
  <hr>
	<!-- 인증 되어 있으면 (로그인 상태) 댓글 창 보임 -->
  {% if request.user.is_authenticated %}
    <form action="{% url 'articles:comments_create' article.pk%}" method="POST">
      {% csrf_token %}
      {{comment_form}}
      <input type="submit">
    </form>
	<!-- 인증 되어 있지 않으면 (로그아웃 상태) 댓글 창 대신 아래 url 보임 -->
  {% else %}
    <a href="{% url 'accounts:login' %}">댓글을 작성하려면 로그인 하세요.</a>
  {% endif %}
{% endblock content %}
```

![인증.PNG](22%2010%2005%20436f6ef7739e48158eb183caf54bb688/%25EC%259D%25B8%25EC%25A6%259D.png)

## 인증된 사용자인 경우만 댓글 삭제

```python
@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:           # 로그인이 되어 있으면 삭제 가능
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)
```