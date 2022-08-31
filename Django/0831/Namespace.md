## Namespace

- pages라는 새로운 어플리케이션의 templete에 index.html이라는 추가하고 url을 부여할떄,
  
  - 1. 초기 어플리케이션 articles의 index로만 움직이는 오류 발생 ()
    
    2. pages/index로 입력해도 articles의 index로만 움직이는 오류발생

- 해결방법
  
  - 1. `URL namespace`
    
    2. `Template namespace`

### URL namespace

- `app_name` + `:` + `URL name`

- `urls.py`
  
  - `path('index/', views.index, name='index')`
    
    - 위 부분중 `name= 'index'`가 articles와 pages가 동일
  
  - `app_name= 'articles'`와 `app_name= 'pages'`로 각각 `urls.py`에 작성
  
  - `{% url 'index' %}` 를 `{% url 'articles:index %}` 꼴로 변경

- `{% url 'articles:index %}` 꼴로 변경하면 클라이언트의 요구에 맞게 pages에 해당하는 index를 보내주는 것처럼 보이지만, 서버는 `articles index`를 `pages index`라고 착각하여 잘못보낸다.
  
  - 이것이 `Template namespace` 문제

---

`Tip`

- `NoReverseMatch` error가 나오면 무조건 url 태그 오류 
  
  - 즉, `<a>`나 `<form>`

---

### Template

- Django는 기본적으로 `app_name/templates/`경로에 있는 templates파일들만 찾을 수 있으며, `settings.py`의 `INSTALLED_APP`에 작성한 app 순서로 templates을 검색 후 렌더링 함
  
  - 즉, templates는 어떤 app의 index임이 중요한게 아니라 그냥 templates 안에 어떤 html파일이 존재하는 가에 따라 다르다.
  
  - 따라서 index라는 html이 2개 존재한다면 app의 등록 순서에 따라 작동한다.
  
  - 그렇기 때문에 index라는 html파일 앞에 경로를 하나 더 만들어 줘야만 한다.
    
    - 즉, 물리적인 이름공간을 만들어줌.

- templates안에 app_name과 같은 폴더 하나를 더 만들어 주고 html 파일들을 그 폴더 안에 넣어준다.
  
  ex) `articles/templates/articles/index.html`
  
  ex) `pages/templates/pages/index_html`
  
  - 따라서 앞으로 template을 가져올 때 `articles/index.html`로 가져온다.

- `views`
  
  - `return render(request, 'dtl.html')`
    
    => `return render(request, 'articles/dtl.html)`

- `index.html`
  
  - `{% extends 'base.html' %}`
    
    =>`{% extends 'pages/base.html' %}`

---

## Django Model

---

## 1. 개요

- Model의 핵심 개념과 ORM을 통한 DB 조작 이해

- Django는 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 추상적인 계층(모델 )을 제공

## 2. Database

- 체계화된 데이터의 모임

- 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템

- DB의 가장 기초적인 키워드에 대해 알아보고자 자세한 내용은 추후 DB 시간에 배움

### 기본구조

- 스키마(Schema)
  
  - 뼈대(Structure)
  
  - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조

- 테이블(Table)
  
  - 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
  
  - 관계(Relation)라고도 부름
    
    - 필드(field) 
      
      - 속성, 컬럼(Column)
      
      - 각 필드에는 고유한 데이터 형식이 지정
        
        ex)INT, TEXT ...
    
    - 레코드(record) 
      
      - 튜플, 행(Row)
      
      - 테이블의 데이터는 레코드에 저장됨

- PK(primary Key)
  
  - 기본 키
  
  - 각 레코드의 고유한 값(식별자로 사용)
  
  - 기술적으로 `다른 항목과 절대로 중복되어 나타날 수 없는  단일 값을 가짐`
  
  - DB 관리 및 테이블 간 관계 설정 시 주요하게 활용 됨

- 쿼리(Quaey)
  
  - 데이터를 조회하기 위한 명령어
  
  - 조건에 맞는 데이터를 추출하거나 조작하는 명령어
    
    - 주로 테이블형 자료구조에서 사용
  
  - Query를 날린다.
    
    => DB를 조작한다.

### 3.  Model

#### 개요

- Django는 Model을 통해 데이터에 접근하고 조작

- 사용하는 데이터들의 필수적인 필드들과 동작들을 포함

- 저장된 데이터베이스의 구조(layout)

- 일반적으로 각각의 모델은 하나의 DB 테이블에 매핑(mapping)

#### 스키마

- 프로젝트의 settings에 app을 설치하고 시작

- `models.py`
  
  ```python
  # models.py
  from django.db import models
  
  # Create your models here.
  class Article(models.Model):
      title = models.CharField(max_length=10) #필드이름 = 타입(최대 길이 = 10)
      content = models.TextField()            # CharField는 길이가 제한적이지만 TextField는 길이제한이 유함
      # PK는 자동 생성되기에 따로 지정 x
  ```

#### 필드

- `CharField(max_length=None, **options)`
  
  - 길이의 제한이 있는 문자열을 넣을 때 사용
  
  - max_length
    
    - 필드의 최대 길이(문자) : 최대 255자
    
    - CharField의 필수 인자
    
    - 데이터베이스와 Django의 유효성 검사(값을 검증하는 것)에서 활용

- `TextField(**optionals)`
  
  - 글자의 수가 많을 때 사용 
    
    - DB가 `SQLite`, `Oracle`, `MySQL` 인지에 따라 달라짐
  
  - max_length 옵션 작성 시 사용자 입력 단계에서는 반영 되지만, 모델과 데이터베이스 단계에는 적용되 지 않음 (CharField를 사용해야함)
    
    - 실제로 저장될 때 길이에 대한 유효성을 검증하지 않음( 불필요함 )

### 4. Migrations

#### 개요

- 모델에 대한 청사진을 만들고 이를 통해 테이블을 생성하는 일련의 과정

- Django가 모델에 생긴 변화(필드 추가, 모델 삭제 등)를 DB에 반영하는 방법

#### 필수 명령어

- `makemigrations`
  
  - `python manage.py makemigraions`
  
  - `articles/migrations`에 `0001_initial.py`이 생성
    
    - fields 안에 `id, title, content` => 위에사 작성한 스키마에 `id`가 추가 돼서 생성
  
  - 스키마를 파이썬에서 클래스로 만들고 `makemigrations`를 통해 `migration` 을 만들고 이렇게 만들어진 것이 `설계도(청사진)` 이다
  
  - 기타 명령어
    
    - `showmigrations`
      
      - `python manage.py showmigrations`
      
      - migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 용도
      
      - [x]표시가 있으면 migrate가 완료되었음을 의미
    
    - `sqlmigrate`
      
      - `python manage.py sqlmigrate articles 0001`
      
      - 해당 migrations 파일이 SQL 문으로 어떻게 해석 될 지 미리 확인 할 수 있음
      
      - `python 언어`가 `SQL 언어`로 `어떻게` 바뀌었는지 알 수 있음

- `migrate`
  
  - `makemigrations`로 만든 설계도를 실제 `db.sqlite3 DB` 파일에 반영하는 과정
  
  - 결과적으로 모델에서의 변경사항들과  DB의 스키마가 동기화를 이룸
    
    - `모델과 DB의 동기화`
  
  - `python manage.py migrate`
  
  - `db.sqlite3` => `우클릭` => `open database` => 좌하단 `SQLITE EXPLORER`
    
    - `articles_article` <----`APP_name` + `_` + ` Class_name`

#### 추가 정의 필드

- `created_at = models.DateTimeField(auto_now_add=True)`
  
  - 만들었을 때 시간

- `update_at = models.DateTimeField(auto_now= True)`
  
  - 업데이트 했을 때 시간
  
  - `python manage.py makemigrations`
    
    - `1` => `enter`
      
      - 지금 default 값을 설정할게 => 알아서 설정해줄게
    
    - `2` 
      
      - 너가 나가서 `created_at = models.DateTimeField(auto_now_add=True, default= xxxxx)` 같이 default 값 넣어 
  
  - `0002_auto_20220831_2139.py` 라는 두번째 설계도 생성
    
    - 2번 설계도는 1번 설계도에 종송적인 설계도
  
  - `python manage.py migrate` 하면 두번째 설계도가 DB와 동기화 되었음을 알 수 있음

- `migration의 3단계`
  
  1. models.py에서 변경이 발생하면
  
  2. migrations 파일 생성 (설계도 생성)
     
     - makemigrations
  
  3- DB 반영 (모델과 DB의 동기화)
  
  - migrate

- `DateTimeField()`
  
  - python의 datetime.datetime 인스턴스로 표시되는 날짜 및 시간을 값으로 사용하는 필드
  
  - DataField를 상속받는 클래스
  
  - 선택인자 ( `문제내기 너무 좋지`)
    
    1. auto_now_add
       
       - 최초 생성 일자 (Useful for creation of timestamps)
       
       - Django ORM이 최초 insert(테이블에 데이터 입력)시에만 현재 날짜와 시간으로 갱신
    
    2- auto_now
    
    - 최종 수정 일자(Useful for "last-modified" titmestamps)
    
    - Django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신

### 5. ORM

#### 개요

- makemigrations로 인해 만들어진 설계도는 파이썬으로 작성되어 있음

- 누가 SQL만 알아 들을 수 있다는 DB가 어떻게 이 설계도를 이해하고 동기화를 이룰 수 있을까?

- 이러한 과정에서 중간에 번역을 담당하는 것이 `ORM`

- Object-Relational-Mapping

- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술 ( Django <-> DB)

- 객체 지향 프로그래밍에서 데이터베이스를 연동할 때, 데이터베이스와 객체 지항 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

- Django는 내장 Django ORM을 사용

- 즉, SQL을 사용하지 않고 데이터베이스를 조작할수 있게 만들어주는 매개체

- 장점
  
  - SQL을 잘 알지 못해도 객체지향 언어로 DB 조작이 가능
  
  - 객체 지향적 접근으로 인한 높은 생산성

- 단점
  
  - ORM 만으로 완전한 서비스를 구현하기 어려운 경우가 있음

- ORM 사용 이유
  
  - `생산성`

#### QuerySet API

- `pip install ipython`+ ` ` + `django-extentions`
  
  - 2개를 한번에 설치하려면 띄어쓰고 하나 더 입력

- `crud` => `settings` => `INSTALLED_APPS` => `'django_extensions',` 추가

- `pip freeze > requirment.txt`

##### 준비과정

###### python Shell

- `git bash`에서 python shell 써보기
  
  ```git
  # 기본 shell
  SSAFY8_HB@DESKTOP-6EUOHOI MINGW64 ~/Desktop
  $ python -i
  Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
  Type "help", "copyright", "credits" or "license" for more information.
  >>> print(1)
  1
  >>> exit()
  
  # ipython shell (자동완성기능과 색상 기)
  SSAFY8_HB@DESKTOP-6EUOHOI MINGW64 ~/Desktop
  $ ipython
  Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (
  AMD64)]
  Type 'copyright', 'credits' or 'license' for more information
  IPython 8.4.0 -- An enhanced Interactive Python. Type '?' for help.
  
  In [1]: print(1)
  1
  
  In [2]: exit()
  ```

###### Django Shell

- ORM 관련 구문 연습을 위해 파이썬 쉘 환경을 사용

- 다만, 일반 파이썬 쉘을 통해서는 장고 프로젝트 환경에 영향을 줄 수 없기 때문에  Django환경 안에서 진행할 수 있는 Django 쉘을 사용

- `python manage.py shell_plus`은 친절
  
  - `'python manage.py shell'`은 불친절

#### QuerySet API

- `Article.obiects.all()` => `<QuerySet []>`로 빈 쿼리셋을 줌
  
  - `models.py`의 전체 데이터를 모두 다 조회해봐

- `Class` + `.` + `objects` + `.` +`Queryset API`
  
  - `Queryset API`에 해당하는 메서드들이 중요
  
  - `objects`는 변하지 않아 `Queryset API`를 위해 존재하는 것

- `Query`
  
  - 데이터베이스에 특정한 데이터를 보여 달라는 요청
    
    - 쿼리문을 작성한다.
      
      => 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성
  
  - 파이썬으로 작성한 코드가 ORM이 `QuerySet`이라는 자료 형태로 변환하여 우리에게 전달

- `QuerySet`
  
  - 데이터베이스에게서 전달 받은 객체 목록(데이터 모음)
    
    - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음
  
  - Django ORM을 통해 만들어진 자료형이며, 필터를 걸거나 정렬 등을 수행할 수 있음

#### CRUD

- `Create/ Read/ Update / Delete`

- 생성/ 조회 / 수정 / 삭제

##### Create

- ```python
  In [1]: Article.objects.all()
  Out[1]: <QuerySet []>
  
  # 생성 첫번째 방법
  In [2]: article = Article()         # 생성
  
  In [3]: article
  Out[3]: <Article: Article object (None)>
  
  In [4]: article.title = 'first'
  
  In [5]: article.content = 'django!'
  
  In [6]: article.save()
  
  In [7]: article
  Out[7]: <Article: Article object (1)>  # 1이라는 id가 부여
  ```

- DB (SQLITE EXPLORER) 에 새로고침을 하고 화살표를 누르면 데이터 생성을 확인 가능

- 실제 입력시는 UTC가 디폴트
  
  - 번역할때 한국시간으로 변경

- ```python
  # 생성 두번째 방법
  In [9]: article = Article(title='second', content='django!')
  
  In [10]: article
  Out[10]: <Article: Article object (None)>
  
  In [11]: article.save()
  
  In [12]: article
  Out[12]: <Article: Article object (2)>
  
  In [13]: Article.objects.all()
  Out[13]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>
  
  In [14]: article.title
  Out[14]: 'second'
  
  In [15]: article.content
  Out[15]: 'django!'
  
  In [16]: article.id
  Out[16]: 2
  
  In [17]: article.pk            # id 와 동일하지 pk도 제공
  Out[17]: 2
  ```

- save를 호출하지 않는 방법(세번쨰)

- ```python
  # 생성 세번째 방법
  In [18]: Article.objects.create(title='third', content='django!')     
  Out[18]: <Article: Article object (3)>
  ```

- `.save()`
  
  - Saving object
  
  - 객체를 데이터베이스에 저장함
  
  - 데이터 생성 시 save를 호출하기 전에는 객체의 id값은 None
    
    - id값은 Django가 아니라 데이터베이스에서 계산되기 때문
  
  - 단순히 모델 클래스를 통해 인스턴스를 생성하는 것은 DB에 영향을 미치지 않기 때문에 반드시 save를 호출해야 테이블에 레코드가 생성됨

##### Read (`조회`가 `가장중요`)

- `all()`
  
  - QuerySet return
  
  - 전체 데이터 조회
  
  - ```python
    n [18]: Article.objects.create(title='third', content='django!')     
    Out[18]: <Article: Article object (3)>
    
    In [19]: articles= Article.objects.all()
    
    In [20]: articles
    Out[20]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
    
    In [21]: for article in articles:
        ...:     print(article)
        ...: 
    Article object (1)
    Article object (2)
    Article object (3)
    ```

- `get()`
  
  - 단일 데이터 조회
  
  - 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시킴
  
  - 둘 이상의 객체를 찾으면 MultipleObjectReturned 예외를 발생시킴
  
  => `고유성`을 보장하는 조회에서 사용
  
  - ```python
    In [22]: Article.objects.get(id=1)
    Out[22]: <Article: Article object (1)>
    
    In [23]: Article.objects.get(pk=1
        ...: )
    Out[23]: <Article: Article object (1)>
    
    In [24]: Article.objects.get(pk=100)    #없는 키값 100을 넣어서 error
    ----------------------------------------------------------------------DoesNotExist                         Traceback (most recent call last)Input In [24], in <cell line: 1>()
    ----> 1 Article.objects.get(pk=100)
    
    File ~\ssafy8\TIL\Django\0831\django-Model\venv\lib\site-packages\django\db\models\manager.py:85, in BaseManager._get_queryset_methods.<locals>.create_method.<locals>.manager_method(self, *args, **kwargs)      
         84 def manager_method(self, *args, **kwargs):
    ---> 85     return getattr(self.get_queryset(), name)(*args, **kwargs)
    
    File ~\ssafy8\TIL\Django\0831\django-Model\venv\lib\site-packages\django\db\models\query.py:435, in QuerySet.get(self, *args, **kwargs)     
        433     return clone._result_cache[0]
        434 if not num:
    --> 435     raise self.model.DoesNotExist(
        436         "%s matching query does not exist." %
        437         self.model._meta.object_name
        438     )
        439 raise self.model.MultipleObjectsReturned(
        440     'get() returned more than one %s -- it returned %s!' % (  
        441         self.model._meta.object_name,
        442         num if not limit or num < limit else 'more than %s' % 
    (limit - 1),
        443     )
        444 )
    
    DoesNotExist: Article matching query does not exist.
    ```
  
  - ```python
    # 중복된 값을 조회할 경우 
    In [25]: Article.objects.get(content =='django!')
    ----------------------------------------------------------------------NameError                            Traceback (most recent call last)Input In [25], in <cell line: 1>()
    ----> 1 Article.objects.get(content =='django!')
    
    NameError: name 'content' is not defined
    
    In [26]: Article.objects.get(content ='django!')
    ----------------------------------------------------------------------MultipleObjectsReturned              Traceback (most recent call last)Input In [26], in <cell line: 1>()
    ----> 1 Article.objects.get(content ='django!')
    
    File ~\ssafy8\TIL\Django\0831\django-Model\venv\lib\site-packages\django\db\models\manager.py:85, in BaseManager._get_queryset_methods.<locals>.create_method.<locals>.manager_method(self, *args, **kwargs)      
         84 def manager_method(self, *args, **kwargs):
    ---> 85     return getattr(self.get_queryset(), name)(*args, **kwargs)
    
    File ~\ssafy8\TIL\Django\0831\django-Model\venv\lib\site-packages\django\db\models\query.py:439, in QuerySet.get(self, *args, **kwargs)     
        434 if not num:
        435     raise self.model.DoesNotExist(
        436         "%s matching query does not exist." %
        437         self.model._meta.object_name
        438     )
    --> 439 raise self.model.MultipleObjectsReturned(
        440     'get() returned more than one %s -- it returned %s!' % (  
        441         self.model._meta.object_name,
        442         num if not limit or num < limit else 'more than %s' % 
    (limit - 1),
        443     )
        444 )
    
    MultipleObjectsReturned: get() returned more than one Article -- it returned 3!
    ```

- `filter()`
  
  - ```python
    In [27]: Article.objects.filter(content='django')
    Out[27]: <QuerySet []>
    
    In [28]: Article.objects.filter(content='django!')
    Out[28]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
    
    In [29]: Article.objects.filter(title='ssafy`)
      Input In [29]
        Article.objects.filter(title='ssafy`)
                                             ^
    SyntaxError: EOL while scanning string literal
    
    In [30]: Article.objects.filter(title='ssafy')
    Out[30]: <QuerySet []>
    
    In [31]: Article.objects.filter(title='first')
    Out[31]: <QuerySet [<Article: Article object (1)>]>
    # pk는 되도록 get에서만 사용하도록 하자.
    In [32]: Article.objects.filter(pk=1)
    Out[32]: <QuerySet [<Article: Article object (1)>]>
    ```
  
  - `Field lookups`
    
    ```python
    # 조회할 때 조건을 붙임
    In [33]: Article.objects.filter(content__contains='ja')
    Out[33]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]
    ```

##### Updtae

- 수정하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장

- article 인스턴스 객체의 인스턴스 변수 값을 새로운 값으로 할당

- save() 인스턴스 메서드 호출

- ```python
  In [34]: article = Article.objects.get(pk=1)
  
  In [35]: article
  Out[35]: <Article: Article object (1)>
  
  In [36]: article.title
  Out[36]: 'first'
  
  In [37]: article.title = 'byebye'
  # 반드시 save를 헤야 바뀐 값이 DB에 영향을 준다.
  In [38]: article.save()
  ```

##### DELETE

- 삭제하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장

- delete() 인스턴스 메서드 호출

- ```python
  In [41]: article=Article.objects.get(pk=1)
  
  In [42]: article
  Out[42]: <Article: Article object (1)>
  
  In [44]: article.delete()
  Out[44]: (1, {'articles.Article': 1})
  
  In [45]: Article.objects.all()
  Out[45]: <QuerySet [<Article: Article object (2)>, <Article: Article object (3)>]>
  
  In [46]: Article.objects.get(pk=1)
  ----------------------------------------------------------------------DoesNotExist                         Traceback (most recent call last)Input In [46], in <cell line: 1>()
  ----> 1 Article.objects.get(pk=1)
  
  File ~\ssafy8\TIL\Django\0831\django-Model\venv\lib\site-packages\django\db\models\manager.py:85, in BaseManager._get_queryset_methods.<locals>.create_method.<locals>.manager_method(self, *args, **kwargs)      
       84 def manager_method(self, *args, **kwargs):
  ---> 85     return getattr(self.get_queryset(), name)(*args, **kwargs)
  
  File ~\ssafy8\TIL\Django\0831\django-Model\venv\lib\site-packages\django\db\models\query.py:435, in QuerySet.get(self, *args, **kwargs)     
      433     return clone._result_cache[0]
      434 if not num:
  --> 435     raise self.model.DoesNotExist(
      436         "%s matching query does not exist." %
      437         self.model._meta.object_name
      438     )
      439 raise self.model.MultipleObjectsReturned(
      440     'get() returned more than one %s -- it returned %s!' % (  
      441         self.model._meta.object_name,
      442         num if not limit or num < limit else 'more than %s' % 
  (limit - 1),
      443     )
      444 )
  
  DoesNotExist: Article matching query does not exist.
  ```

- 1번을 빼고 다시 넣는다고 하더라도 id가 1부터 채워지는 것이 아니라 4번부터 나온다.

> Tip

- __str__을 이용하여 출력을 깔끔하게 한 경우, Django shell을 다시 켜야함. 즉,`exit()`후, `python manage.py shell_plus`

- ```python
  #models.py
  from turtle import update
  from django.db import models
  
  # Create your models here.
  class Article(models.Model):
      title = models.CharField(max_length=10) #필드이름 = 타입(최대 길이 = 10)
      content = models.TextField()            # CharField는 길이가 제한적이지만 TextField는 길이제한이 유함
      # PK는 자동 생성되기에 따로 지정 x
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now= True)
  
  
      # 이거 추가
      def __str__(self):
          return self.title
  ```

- 이건 DB에 영향을 주지 않기 때문에 `makemigrations` 을 사용하지 않는다.
