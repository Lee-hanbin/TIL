# CRUD with view function

## Create

### 1.  필요한 view 함수

- `new`  view function

- `create` view function

### 2. `new`  view function

- ```python
  #App/urls.py
  urlpatterns = [
      path('', view.index, name= 'index'),    # ''는 app 이름만으로 주소입
      path('new/', views.new, name= 'new'),
  ]
  ```
  
  - app의 url에 경로 설정

- ```python
  #App/views.py
  def new(request):
      return render(request, 'apps/new.html)
  ```
  
  - app의 views function 정의

- ```html
  <!-- temlplates/apps/new.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>New</h1>
    <form action="#" method="GET">
      <label for= "title">Title:</label>
      <input type="text" name="title">
      <br>
      <label for="content"><Content: </label>
      <textarea name="content"></textarea>
      <br>
      <input type="submit">
    </form>
    <hr>
    <a href="{% url 'apps:index' %}">[back]</a>
  {% endblock content %}
  ```
  
  - new.html

- ```html
  <!-- temlplates/apps/index.html -->
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>index</h1>
    <a href="{% url 'apps:new' %}">new</a>
    <hr>
  {% endblock content %}
  ```
  
  - `index.html` => `new.html` 

- ```python
  #app/urls.py
  
  urlpatterns = [
      path('', view.index, name= 'index'),    # ''는 app 이름만으로 주소입
      path('new/', views.new, name= 'new'),
      path('create/' views.create, name= 'create'),
  ]
  ```
  
  - app의 url에 경로추가

- ```python
  #App/views.py
  
  def create(request):
      title = request.GET.get('title')
      content = request.GET.get('content')
  
      app = Article(title=title, content=content)
      app.save()
  
      return render(request, 'apps/create.html')
  ```
  
  - app의 view functon인 `create 함수` 정의 => `데이터 생성 함수`
  
  ```html
  <!-- temlplates/apps/new.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>New</h1>
    <form action="{% url 'apps:create' %}" method="GET"> <!-- 이거 변경-->
      <label for= "title">Title:</label>
      <input type="text" name="title">
      <br>
      <label for="content"><Content: </label>
      <textarea name="content"></textarea>
      <br>
      <input type="submit">
    </form>
    <hr>
    <a href="{% url 'apps:index' %}">[back]</a>
  {% endblock content %}
  ```
  
  - `new.html`에 `create함수`를 `연동`하여 `데이터를 생성`할 수 있게 함

- ```python
  # apps/views.py
  
  def create(request):
      title = request.GET.get('title')
      content = request.GET.get('content')
  
      app = Article(title=title, content=content)
      app.save()
  
      return render(request, 'apps/index.html')   # 이거 변경
  ```
  
  - 게시글 작성하면 index 페이지로 돌아가게 함

- ## `문제점 발생`
  
  1. 게시글 작성 후, index 페이지가 출력되지만 게시글은 조회 x
     
     ```markdown
     - crerate 함수에서 index.html 문서를 렌더링할 때 context 데이터와 함께 
      렌더링 하지 않기 때문
     => index 페이지 url로 다시 요청을 보내면 정상적으로 출력됨
     ```
  
  2. 게시글 작성 후 url은 여전히 create에 머물러 있음
     
     ```markdown
     - index view 함수를 통해 렌더링 된 것이 아니기 때문
     => index view 함수의 반환 값이 아닌 단순히 index 페이지만 render 되었을 뿐 
     ```

- ## `Django shortcut function - "redirect()"`
  
  - 인자에 작성된 곳으로 요철을 보냄
  
  - 사용가능한 인자
    
    - view name (URL pattern name) 
      
      `return redirect('apps:index')`
    
    - absolute or relative URL
      
      ` return redirect('/apps/')` 
  
  - 동작 확인 후 불필요해진 `create.html` `삭제!`
    
    ```python
    # apps/views,py
    
    def create(request):
        title = request.GET.get('title')
        content = request.GET.get('content')
    
        app = Article(title=title, content=content)
        app.save()
    
        return redirect('apps:index')   # 이거 변경
    ```
  
  - 게시글 작성 후 터미널 로그 확인
    
    ```bash
    [날짜 시간] "GET /apps/create/?tilte=11&content=22 HTTP/1.1" 302 0
    [날짜 시간] "GET /apps/ HTTP/1.1" 200 1064
    ```
    
    - `302` 와 `200` 을 확인 해봐야 함
  
  - `동작 원리`
    
    - 클라이언트가 create url로 요청을 보냄
    
    - create view 함수의 redirect 함수가 `302 status code`를 응답
    
    - 응답 받은 브라우저는 redirect 인자에 담긴 주소(index)로 사용자를 이동시키기 위해 index url로 Django에 재요청
    
    - index page를 정상적으로 응답 받음 (`200 status code`)
  
  - HTTP response status code
    
    - 클라이언트에게 특정 HTTP 요청이 `성공적으로 완료되었는지 여부`를 알려줌
    
    - 응답 5개 그룹
      
      1. Informational responses (1xx)
      
      2. Succesful responses (2xx)
      
      3. Redirection messages (3xx)
      
      4. Client error responses (4xx)
      
      5. Server error responses (5xx)
  
  . `GET`  vs `POST`
  
    . GET
  
      1.  특정 리소스를 가져오도록 요청할 때 사용
      
      2.  반드시 데이터를 `가져올 때만` 사용해야 함
      
      3. `DB`에 변화를 주지 않음
      
      4. CRUD에서 `R 역할` 담당
  
  - POST
    
    1. `서버`로 `데이터`를 `전송`할 때 사용
    
    2. 서버에 `변경사항`을 만듦
    
    3. 리소스를 `생성/변경`하기 위해 `데이터`를 `HTTP body`에 담아 `전송`
    
    4. GET의 쿼리 스트링 파라미터와 다르게 `URL로 보내지지 않음`
    
    5. CRUD에서 `C/U/D 역할`을 담당
    
    ```html
    <!-- temlplates/apps/new.html -->
    
    {% extends 'base.html' %}
    
    {% block content %}
    <h1>New</h1>
    <form action="{% url 'apps:create' %}" method="POST"> <!-- 이거 변경-->
      <label for= "title">Title:</label>
      <input type="text" name="title">
      <br>
      <label for="content"><Content: </label>
      <textarea name="content"></textarea>
      <br>
      <input type="submit">
    </form>
    <hr>
    <a href="{% url 'apps:index' %}">[back]</a>
    {% endblock content %}
    ```
  
  - 코드 변경 후, URL에서 쿼리 스트링 파라미터가 없어진 것을 확인해보기
    
    ```bash
    Forbidden (CSRF cookekie not set): /apps/create/
    [날짜 시간] "POST /apps/create/ HTTP/1.1" 403 2870
    ```
  
  - 403 Forbidden 응답을 받았지만 나중에 확인하고 요청된 URL을 확인
    
    - 서버에 요청이 전달되었으나, 권한 때문에 거절
    
    - 서버에 요청이 도달했으나, 서버가 접근을 거부
    
    - 게시글 권한 x => `Django`가 `작성자를 모르니` `거부`함
    
    - DB를 조작하는 것은 단순 조회와 다르기 때문에 `신원 확인 필요`
  
  - 데이터가 담긴 위치가 바뀌었으므로 view 함수도 수정
    
    ```python
    # apps/views,py
    
    def create(request):
      title = request.POST.get('title')        # GET -> POST
      content = request.POST.get('content')    # GET -> POST
    
      app = Article(title=title, content=content)
      app.save()
    
      return redirect('apps:index') 
    ```
  
  - csrf_token 
    
    - Security Token 사용 방식
    
    - 사용자의 데이터에 임의의 난수 값(token)을 부여해 매 요청마다 해당 난수 값을 포함시켜 전송 시킴
    
    - 이후 서버에서 요청을 받을 때마다 전달된 token 값이 유효한지 검증
    
    - 일반적으로 데이터 변경이 가능한 POST, PATCH, DELETE Method 등에 적용
    
    - Django는 DTL에서 csrf_tocken 템플릿 태그를 제공
      
      ```html
      <!-- temlplates/apps/new.html -->
      
      {% extends 'base.html' %}
      
      {% block content %}
        <h1>New</h1>
        <form action="{% url 'apps:create' %}" method="POST"> 
      
          {% csrf_token %}        <!-- 이거 추가 -->
      
          <label for= "title">Title:</label>
          <input type="text" name="title">
          <br>
          <label for="content"><Content: </label>
          <textarea name="content"></textarea>
          <br>
          <input type="submit">
        </form>
        <hr>
        <a href="{% url 'apps:index' %}">[back]</a>
      {% endblock content %}
      ```
      
      
