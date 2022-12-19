### 가상환경 설정

- `python -m venv venv` : venv라는 가상환경 설정
  
  - 마지막 venv는 가상환경의 이름 => 웬만하면 venv로 설정하자

- `pip list`  : 현재 라이브러리 보기

- `source venv/Scripts/activate` : 가상환경에 들어가기

### Django

- `pip install django==3.2.13` : 3.2버전을 명시해서 설치

- `pip freeze > requirements.txt` : 패키지 목록 생성

- `django-admin startproject firstpjt .` : firstpjt라는 프로젝트 생성
  
  - 프로젝트 이름에는 파이썬이나 쟝고에서 사용 중인 키워드 및 '-' 사용 불가
  
  - ' . '을 붙이지 않을 경우 현재 디렉토리에 프로젝트 디렉토리를 새로 생성하게 됨

### Server

- `python manage.py runserver` : 서버 실행

- `__init__.py` : python에게 이 디렉토리를 하나의 python 패키지로 다루도록 지시

- `asgi.py`
  
  - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움
  
  - 추후 배포시 사용 (현재 수정 x)

- `settings.py` : (사용) Django 프로젝트 설정을 관리

- `urls.py` : (사용) 사이트의 `url`과 적절한 `views`의 연결을 지정

- `wsgi.py` : Web Server Gateway Interface
  
  - Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움
  
  - 추후 배포시 사용 (현재 수정 x)

- `manage.py` (고려)
  
  - Django 프로젝트와 다양한 방벙으로 상호작용 하는 커맨드라인 유틸리티

- `tip`
  
  - `cntl + c` : 서버 나가기

### 어플리케이션

- `python manage.py startapp articles` : articles라는 애플리케이션(앱) 생성
  
  - 일반적으로 애플리케이션 이름은 `복수형`으로 작성하는 것을 권장

- `__init__.py` 

- `admin.py`  :  `관리자용 페이지`를 설정 하는 곳

- `apps.py`  
  
  - 앱의 정보가 작성된 곳
  - 별도로 추가 코드를 작성하지 않음

- `models.py`  
  
  - 애플리케이션에서 사용하는 `Model`을 정의하는곳
  - MTV 패턴의 `M`에 해당

- `tests.py`  : 프로젝트의 `테스트 코드`를 작성하는 곳

- `views.py`  
  
  - `view 함수`들이 정의 되는 곳
  - MTV 패턴의 `V`에 해당

`firstpjt -> settings.py`

- `INSTALLED_APPS`
  
  - 제일 위에 내 함수
    
    - 어플리케이션 articles 설치
    
    - `'article'`
  
  - 그 뒤에 3rd part
  
  - 그 뒤에 내장함수

- `firstpjt -> urls.py`
  
  - `from articles import views`
  
  - `path('index/', views.index)`
    
    - views에 있는 인덱스라는 함수를 실행하렴
  
  - `path('admin/', admin.site.urls)`
    
    - server 주소 뒤에 `admin/` 이 나오면 `admin.site.urls`을 실행시켜줘

- `articles -> views.py`
  
  - ```python
    def index(request):
        return render(request, 'index.html')
    ```
  
  - `reder(request, template_name, context)`
    
    - 주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고 렌더링 된 텍스트와 함께 응답 개체를 반환하는 함수
    
    - `request`
      
      - 응답을 생성하는 데 사용되는 요청 객체
    
    - `template_name`
      
      - 템플릿의 전체 이름 또는 템플릿 이름의 경로
    
    - `context`
      
      - 템플릿에서 사용할 데이터

- `Templates`
  
  - articles app 폴더 안에 templates 만들기
  
  - templates 안에 index.html 생성
  
  - ```html
    <!-- ariticles/templates/index.html-->
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <!-- 생략 -->
    </head>
    <body>
      <h1>만나서 반가워요!</h1>
    </body>
    </html>
    ```
  
  - `python manage.py runserver`
    
    - `http://127.0.0.1:8000/` 을 `cnt + click`
    
    - `http://127.0.0.1:8000/index` 입력하면 해당 index를 웹 브러우저로 구현

```python
#Django 실행순서
가상환경 설정

시스템 환경 설정

패키지 목록 생성

프로젝트 생성

어플리케이션 생성

서버 실행

프로젝트에 어플리케이션 정의

어플리케이션 함수 가져오기

어플리케이션에 함수 정의

프로젝트에 template를 생성하고 index.html을 생성

서버를 실행해서 index.html 확
```

---

### Variable

```python
#urls.py
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('dtl/', views.dtl),
]
```

```python
#views.py
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def dtl(request):
    name = 'jun'
    age = 20
    context = {
        'name' : name,
        'age' : age
    }
    return render(request, 'dtl.html', context)
```

```html
<!--dtl.html-->

<!-- ariticles/templates/index.html-->

<!DOCTYPE html>
<html lang="en">
<head>
  <!-- 생략 -->
</head>
<body>
  <h1>dtl</h1>
  <p>{{name}}</p>
  <p>{{age}}</p>
</body>
</html>
```

### Filter

```python
#views.py
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def dtl(request):
    # name = 'jun'
    # age = 20
    context = {
        'name' : 'ABCDEFGH',
        'age' : 20,
        'foods' : ['apple', 'grape']
    }
    return render(request, 'dtl.html', context)
```

```html
<!-- dtl.html-->

<!-- ariticles/templates/index.html-->

<!DOCTYPE html>
<html lang="en">
<head>
  <!-- 생략 -->
</head>
<body>
  <h1>dtl</h1>
  <p>{{name}}</p>
  <p>{{name|lower|truncatechars:4}}</p>
  <p>{{age}}</p>
  <p>{{name}}의 나이는 {{age}}야!</p>
  <p>{{foods.0}}</p>
  <p>{{foods.1}}</p>
</body>
</html>
```

### Tags

```python
#views
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def dtl(request):
    # name = 'jun'
    # age = 20
    context = {
        'name' : 'ABCDEFGH',
        'age' : 20,
        'foods' : ['apple', 'grape']
    }
    return render(request, 'dtl.html', context)
```

```html
<!-- dtl.html -->
<!-- ariticles/templates/index.html-->

<!DOCTYPE html>
<html lang="en">
<head>
  <!-- 생략 -->
</head>
<body>
  <h1>dtl</h1>
  <p>-----------------여기는 values야---------------</p>
  <p>{{name}}</p>
  <p>{{age}}</p>
  <p>{{name}}의 나이는 {{age}}야!</p>
  <p>{{foods.0}}</p>
  <p>{{foods.1}}</p>
  <p>------------여기는 filter야 4 넣었어-----------</p>
  <p>{{name|lower|truncatechars:4}}</p>
  <p>------------------여기는 tag야------------</p>
  <p> ########for 문######### </p>
  {% for food in foods %}
    <p>{{food}}</p>
  {% endfor %}
  <p> #########if 문#########</p>
  {% if age < 0 %}
    <p>{{ age }}</p>
  {% else%}
    <p> {{0}}</p>
  {% endif %}

</body>
</html>
```

### Comment

DTL은 가볍게 하고 넘어가도 무관하지만 시험문제는 나옴

---

### Templete 상속

```python
# urls.py

from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('dtl/', views.dtl),
    path('dtl2/', views.dtl2)        # 요거 추가
]
```

```python
#views.py

from django.shortcuts import render

#요거 추가
def dtl2(request):                   
    # name = 'jun'
    # age = 20
    context = {
        'name' : 'ABCDEFGH',
        'age' : 20,
        'foods' : ['apple', 'grape']
    }
    return render(request, 'dtl2.html', context)
```

```html
<!-- dtl2.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>dtl2</h1>
  <p>-----------------여기는 values야---------------</p>
  <p>{{name}}</p>
  <p>{{age}}</p>
  <p>{{name}}의 나이는 {{age}}야!</p>
  <p>{{foods.0}}</p>
  <p>{{foods.1}}</p>
  <p>------------여기는 filter야 4 넣었어-----------</p>
  <p>{{name|lower|truncatechars:4}}</p>
  <p>------------------여기는 tag야------------</p>
  <p> ########for 문######### </p>
  {% for food in foods %}
    <p>{{food}}</p>
  {% endfor %}
  <p> #########if 문#########</p>
  {% if age < 0 %}
    <p>{{ age }}</p>
  {% else%}
    <p> {{0}}</p>
  {% endif %}

{% endblock content %}
```

```html
<!-- base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <p>네비게이션 바</p>
  {% block content %}

  {% endblock content %}
  <p>푸터</p>
</body>
</html>
```

### Template 경로

```python
#settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], #이거 추가
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

```html
<!--index.html-->
{% extends 'base2.html' %}

{% block content %}
  <h1>만나서 방가방가</h1>
  <p> 여긴 시작점이야 하나씩 눌러봐</p>
  <a href="/dtl/">dtl</a>            <!-- 이거 누르면 dtl으로 휙! -->
  <a href="/dtl2/">dtl2</a>          <!-- 이거 누르면 dtl2로 휙! -->
{% endblock content %}
```

```html
<!--dtl.html-->
<!-- ariticles/templates/index.html-->

<!DOCTYPE html>
<html lang="en">
<head>
  <!-- 생략 -->
</head>
<body>
  <p> 이건 처음만든 drl이야</p>
  <h1>dtl</h1>
  <p>-----------------여기는 values야---------------</p>
  <p>{{name}}</p>
  <p>{{age}}</p>
  <p>{{name}}의 나이는 {{age}}야!</p>
  <p>{{foods.0}}</p>
  <p>{{foods.1}}</p>
  <p>------------여기는 filter야 4 넣었어-----------</p>
  <p>{{name|lower|truncatechars:4}}</p>
  <p>------------------여기는 tag야------------</p>
  <p> ########for 문######### </p>
  {% for food in foods %}
    <p>{{food}}</p>
  {% endfor %}
  <p> #########if 문#########</p>
  {% if age < 0 %}
    <p>{{ age }}</p>
  {% else%}
    <p> {{0}}</p>
  {% endif %}
  <a href="/index/">처음으로!</a>    <!-- 이거 추가해서 처음으로 넘어 -->
</body>
</html>
```

```html
<!--dtl2.html-->
{% extends 'base.html' %}

{% block content %}
  <p>-----------이건 말이야 상속을 연습하려고 해본 drl2야~--------------</p>
  <h1>dtl2</h1>
  <p>-----------------여기는 values야---------------</p>
  <p>{{name}}</p>
  <p>{{age}}</p>
  <p>{{name}}의 나이는 {{age}}야!</p>
  <p>{{foods.0}}</p>
  <p>{{foods.1}}</p>
  <p>------------여기는 filter야 4 넣었어-----------</p>
  <p>{{name|lower|truncatechars:4}}</p>
  <p>------------------여기는 tag야------------</p>
  <p> ########for 문######### </p>
  {% for food in foods %}
    <p>{{food}}</p>
  {% endfor %}
  <p> #########if 문#########</p>
  {% if age < 0 %}
    <p>{{ age }}</p>
  {% else%}
    <p> {{0}}</p>
  {% endif %}
  <a href="/index/">처음으로!</a>        <!-- 이거 추가해서 처음으로 넘어가 -->
{% endblock content %}
```

---

### Form

```python
#urls.py

from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('dtl/', views.dtl),
    path('dtl2/', views.dtl2),
    path('throw/', views.throw),
]
```

```python
# views.py
from django.shortcuts import render

# Create your views here.

def throw(request):
    return render(request, 'throw.html')
```

```html
<!-- throw -->
{% extends 'base2.html' %}

{% block content %}
  <p>--------이건 그냥 검색창이지롱~ 검색 안되니까 누르지마~ 확인하려면 url창 봐봐 search 보이지?------</p>
  <form action="", method="">
    <label for="search"> search </label>
    <input type="text", name="search", id="search"> <!-- 라벨이랑 input연동-->
    <input type="submit">    
  </form>

  <p>---------이건 검색 되니까 IU 쳐봐 힐링힐링 --------------</p>
  <form action="https://search.naver.com/search.naver">
    <input type="text", name="query">
    <input type="submit">
  </form>

{% endblock content %}
```

```html
<!-- base2.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <p>네비게이션 바</p>
  {% block content %}


  {% endblock content %}
  <p>푸터</p>
</body>
</html>
```

---

### GET

```python
#urls.py
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('dtl/', views.dtl),
    path('dtl2/', views.dtl2),
    path('throw/', views.throw),
    path('catch/', views.catch),
]
```

```python
#views.py
def catch(request):                         
    # print(request.GET.get('search'))
    value = request.GET.get('search')
    name = 'jun'
    context = {
        'value' : value,
        'name' : name,
    }
    return render(request, 'catch.html', context)
```

```html
<!--base2.html-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <p>네비게이션 바</p>
  {% block content %}


  {% endblock content %}
  <p>푸터</p>
</body>
</html>
```

```html
<!--catch.html-->
{% extends 'base2.html' %}

{% block content %}
  <p>{{value}}를 받았어!</p>
  <p>감사링~ {{name}}</p>
  <a href="/throw/">throw</a>
{% endblock content %}
```

```html
<!--throw.html-->
{% extends 'base2.html' %}

{% block content %}
  <p>--------이건 그냥 검색창이지롱~ 검색 안되니까 누르지마~ 확인하려면 url창 봐봐 search 보이지?------</p>
  <form action="/catch/", method="GET">
    <label for="search"> search </label>
    <input type="text", name="search", id="search"> <!-- 라벨이랑 input연동-->
    <input type="submit">
  </form>

  <p>---------이건 검색 되니까 IU 쳐봐 힐링힐링 --------------</p>
  <form action="https://search.naver.com/search.naver">
    <input type="text", name="query">
    <input type="submit">
  </form>


  <a href="/index/">처음으로</a>

{% endblock content %}
```

---

### Trailing Slashes

- Django는 URL 끝에 `/`가 없다면 자동으로 붙여주는 것이 기본 설정
  
  - 모든 주소가 `/`로 끝나도록 구성 되어있음
  
  - 모든 프레임워크가 그렇게 동작하는 것은 아니다 (Django를 제외한 다른)

- 기술적인 측면에서 `love.com/you`와 `love.com/you/`는 서로 다른 URL이다
  
  - `전자`는 `페이지`로 인식하며
  
  - `후자`는 `폴더`로 인식함을 뜻한다.

---

### Variable routing

- Variable routing의 필요성
  
  - 템플릿의 많은 부분이 중복되고, 일부분만 변경되는 상황에서 비슷한 url과 템플릿을 계속 만들어 줘야할까?

- Variable routing
  
  - URL 주소를 변수로 사용하는 것
  
  - URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음
  
  - 따라서 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음

```python
#urls.py
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('dtl/', views.dtl),
    path('dtl2/', views.dtl2),
    path('throw/', views.throw),
    path('catch/', views.catch),
    # name이라는 변수가 str이 아니면 막아 
    path('hello/<str:name>/', views.hello),     
]
```

```python
#views.py
def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'hello.html',context)
```

```html
<!--hello.html-->
{% block content %}
  <p>{{value}}를 받았어!</p>
  <p>감사링~ {{name}}</p>
  <a href="/throw/">throw</a>
{% endblock content %}
```

```html
<!--throw.html-->
{% extends 'base2.html' %}

{% block content %}
  <p>--------이건 그냥 검색창이지롱~ 검색 안되니까 누르지마~ 확인하려면 url창 봐봐 search 보이지?------</p>
  <form action="/catch/", method="GET">
    <label for="search"> search </label>
    <input type="text", name="search", id="search"> <!-- 라벨이랑 input연동-->
    <input type="submit">
  </form>

  <p>--------이건 variable routing -----------</p>
  <form action="/hello/", method="GET">
    <label for="search"> search </label>
    <input type="text", name="search", id="search"> <!-- 라벨이랑 input연동-->
    <input type="submit">
  </form>


  <p>---------이건 검색 되니까 IU 쳐봐 힐링힐링 --------------</p>
  <form action="https://search.naver.com/search.naver">
    <input type="text", name="query">
    <input type="submit">
  </form>


  <a href="/index/">처음으로</a>

{% endblock content %}
```

---

### App URL mapping

- pages라는 어플리케이션을 하나 더 만들어서 urls를 따로 사용 가능하게함
  
  - 유지보수에 유리함

- `from django.urls import` + `, include`

- `path('articles/' include('articles.urls'))`

- `path('pages/' include('pages.urls'))`
  
  - include()는다른  URLconf들을 참조할 수 있도록 돕는 함수

- 막약 pages의 urls.py에 urlpatterns가 공백리스트로 라도 존재하지 않으면 에러발생

- `/articles/index/` 로 입력해야 index로 넘어감

### Naming URL Patterns

- 문자열 주소를 변경해야 하는 상황에서 모든 곳을 변경하는 것은 너무 비효율적

- path()함수의 name인자를 정의해서 사용

- DTL의 Tag 중 하나인  URL 태그를 사용해서 path() 함수에 작성한 name을 사용가능

- 이를 통해 URL 설정에 정의된 특정한 경로들의 의존성을 제거할 수 있음

- view 함수와 templete에서 특정 주소를 쉽게 참조할 수 있도록 도움

- `<a herf="/index/">처음으로</a>`을
  
  - 으로 `<a herf="{% url 'index' %}"> 처음으로</a>` 바꿔준다.

### 

```python
#firstpjt/urls.py
"""firstpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
```

```python
#articles/urls.py
from django.urls import path
from . import views

# articles's urls.py

urlpatterns = [
    path('index/', views.index, name='index'),
    path('dtl/', views.dtl, name='dtl'),
    path('dtl2/', views.dtl2, name='dtl2'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch),
    # name이라는 변수가 str이 아니면 막아 
    path('hello/<str:name>/', views.hello),     
]
```

```python
#pages/urls.py
from django.urls import path
from . import views

# pages's urls.py

urlpatterns = [
]
```

```html
<!--article/templates-->

<!--index-->
{% extends 'base2.html' %}

{% block content %}
  <h1>만나서 방가방가</h1>
  <p> 여긴 시작점이야 하나씩 눌러봐</p>
  <a href="{% url 'dtl' %}">dtl</a>
  <a href="{% url 'dtl2' %}">dtl2</a>
  <a href="{% url 'throw' %}">검색하러가자</a>
{% endblock content %}
```

```html
<!--dtl-->

<!-- ariticles/templates/index.html-->
<!DOCTYPE html>
<html lang="en">
<head>
  <!-- 생략 -->
</head>
<body>
  <p> 이건 처음만든 drl이야</p>

  <h1>dtl</h1>
  <p>-----------------여기는 values야---------------</p>
  <p>{{name}}</p>
  <p>{{age}}</p>
  <p>{{name}}의 나이는 {{age}}야!</p>
  <p>{{foods.0}}</p>
  <p>{{foods.1}}</p>
  <p>------------여기는 filter야 4 넣었어-----------</p>
  <p>{{name|lower|truncatechars:4}}</p>
  <p>------------------여기는 tag야------------</p>
  <p> ########for 문######### </p>
  {% for food in foods %}
    <p>{{food}}</p>
  {% endfor %}
  <p> #########if 문#########</p>
  {% if age < 0 %}
    <p>{{ age }}</p>
  {% else%}
    <p> {{0}}</p>
  {% endif %}
  <a href="{% url 'index' 
%}">처음으로!</a>
</body>
</html>
```

```html
<!-- dtl2.html -->
{% extends 'base.html' %}

{% block content %}
  <p>-----------이건 말이야 상속을 연습하려고 해본 drl2야~--------------</p>
  <h1>dtl2</h1>
  <p>-----------------여기는 values야---------------</p>
  <p>{{name}}</p>
  <p>{{age}}</p>
  <p>{{name}}의 나이는 {{age}}야!</p>
  <p>{{foods.0}}</p>
  <p>{{foods.1}}</p>
  <p>------------여기는 filter야 4 넣었어-----------</p>
  <p>{{name|lower|truncatechars:4}}</p>
  <p>------------------여기는 tag야------------</p>
  <p> ########for 문######### </p>
  {% for food in foods %}
    <p>{{food}}</p>
  {% endfor %}
  <p> #########if 문#########</p>
  {% if age < 0 %}
    <p>{{ age }}</p>
  {% else%}
    <p> {{0}}</p>
  {% endif %}
  <a href="{% url 'index' %}">처음으로!</a>
{% endblock content %}
```

```html
<!--throw.html-->
{% extends 'base2.html' %}

{% block content %}
  <p>--------이건 그냥 검색창이지롱~ 검색 안되니까 누르지마~ 확인하려면 url창 봐봐 search 보이지?------</p>
  <form action="/catch/", method="GET">
    <label for="search"> search </label>
    <input type="text", name="search", id="search"> <!-- 라벨이랑 input연동-->
    <input type="submit">
  </form>

  <p>--------이건 variable routing -----------</p>
  <form action="/hello/", method="GET">
    <label for="search"> search </label>
    <input type="text", name="search", id="search"> <!-- 라벨이랑 input연동-->
    <input type="submit">
  </form>


  <p>---------이건 검색 되니까 IU 쳐봐 힐링힐링 --------------</p>
  <form action="https://search.naver.com/search.naver">
    <input type="text", name="query">
    <input type="submit">
  </form>


  <a href="{% url 'index' %}">처음으로</a>

{% endblock content %}
```
