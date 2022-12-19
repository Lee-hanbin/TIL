# M:N

22/10/12

# Many to many relationship

## Intro

### 개요

- 병원에 내원하는 환자와 의사의 예약 시스템을 구축하라는 업무를 지시 받음
    - 필요한 데이터베이스 모델을 고민해보고 모델링 진행하기
    - 모델링을 하는 이유는 현실 세계를 최대한 유사하게 반영하기 위함
- 무엇부터 고민해야 할까?
    - 병원 시스템에서 가장 핵심이 되는 것은? `의사와 환자`
    - 이 둘의 관계를 어떻게 표현할 수 있을까?
- 우리 일상에 가까운 예시를 통해 DB를 모델링 하고 그 내부에서 일어나는 데이터의 흐름을 어떻게 제어할 수 있을지 고민

```powershell
시작 전 용어 정리
1. target model
	- 관계 필드를 가지지 않은 모델
2. source model
	- 관계 필드를 가진 모델
```

### N:1의 한계

- 각각 2명의 의사와 환자를 생성하고 환자는 서로 다른 의사에게 예약을 했다고 가정
    
    ```powershell
    #shell_plus
    
    doctor1 = Doctor.objects.create(name='alice')
    doctor2 = Doctor.objects.create(name='bella')
    patient1 = Patient.objects.create(name='carol', doctor=doctor1)
    patient2 = Patient.objects.create(name='dane', doctor=doctor2)
    ```
    
- 1번 환자(carol)가 두 의사 모두에게 방문하려고 함
    - 새로운 환자
    
    ```powershell
    patient3 = Patient.objects.create(name='carol', doctor=doctor2)
    ```
    

⇒ `예약 테이블을 따로 만들자`

### 중개 모델

- 환자 모델의 외래 키를 삭제하고 별도의 예약 모델을 새로 작성
- 예약 모델은 의사와 환자에 각각 N:1 관계를 가짐
    
    ```python
    class Patient(models.Model):
        # 외래키 삭제 #
        # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
        name = models.TextField()
    
        def __str__(self):
            return f'{self.pk}번 환자 {self.name}'
    
    # 예약 모델 생성 # 
    class Reservation(models.Model):
        doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
        patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
        def __str__(self):
            return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
    ```
    
- 데이터베이스 초기화 후 Migration 진행 및 shell_plus 실행
    1.  migration 파일(`0001_initial.py`) 삭제
    2. 데이터베이스 파일 (`db.sqlide3`)삭제
    3. migration
    4. migrate
    5. shell_plus
- 의사와 환자 생성 후 예약 만들기
    
    ```powershell
    In [1]: doctor1  = Doctor.objects.create(name='alice')
    In [2]: patient1 = Patient.objects.create(name='carol')
    In [3]: Reservation.objects.create(doctor=doctor1, patient=patient1)
    Out[3]: <Reservation: 1번 의사의 1번 환자>
    ```
    
- 예약 정보 조회
    
    ```powershell
    In [6]: doctor1.reservation_set.all()
    Out[6]: <QuerySet [<Reservation: 1번 의사의 1번 환자>]>
    In [7]: patient1.reservation_set.all()
    Out[7]: <QuerySet [<Reservation: 1번 의사의 1번 환자>]>
    ```
    
- 1번 의사에게 새로운 환자 예약이 생성 된다면
    
    ```powershell
    In [8]: patient2 = Patient.objects.create(name='dane')
    
    In [9]: Reservation.objects.create(doctor=doctor1, patient=patient2)
    Out[9]: <Reservation: 1번 의사의 2번 환자>
    ```
    
- 1번 의사의 예약 정보 조회
    
    ```powershell
    In [13]: doctor1.reservation_set.all()
    Out[13]: <QuerySet [<Reservation: 1번 의사의 1번 환자>, <Reservation: 1번 의사의 2번 환자>]>
    ```
    

### Django ManyToManyField

- 환자 모델에 Django ManyToManyField 작성
    
    ```powershell
    class Patient(models.Model):
        # 다대다필드 생성 #
        doctors =models.ManyToManyField(Doctor) # 환자가 의사를 참조함 Doctor에 넣으면 반대
        name = models.TextField()
    
        def __str__(self):
            return f'{self.pk}번 환자 {self.name}'
    ```
    
- 데이터베이스 초기화 후 Migration 진행 및 shell_plus 실행
    1.  migration 파일(`0001_initial.py`) 삭제
    2. 데이터베이스 파일 (`db.sqlide3`)삭제
    3. migration
    4. migrate
    5. shell_plus
- 의사 1명과 환자 2명 생성
    
    ```powershell
    In [1]: doctor1 = Doctor.objects.create(name='alice')
    In [2]: patient1 = Patient.objects.create(name='carol')
    In [3]: patient2 = Patient.objects.create(name='dane')
    ```
    
- 예약 생성 (`환자 ⇒ 의사`)
    
    ```powershell
    # patient1이 doctor1에게 예약
    In [4]: patient1.doctors.add(doctor1)
    
    In [5]: patient1.doctors.all()
    Out[5]: <QuerySet [<Doctor: 1번 의사 alice>]>
    
    # 역참조 이므로 patient_set으로 불러와야함!
    In [6]: doctor1.patient_set.all()
    Out[6]: <QuerySet [<Patient: 1번 환자 carol>]>
    ```
    
- 예약 생성 (`의사 ⇒ 환자`)
    
    ```powershell
    # doctor1이 patient2을 예약
    In [8]: doctor1.patient_set.add(patient2)
    
    In [9]: doctor1.patient_set.all()
    Out[9]: <QuerySet [<Patient: 1번 환자 carol>, <Patient: 2번 환자 dane>]>
    
    In [10]: patient1.doctors.all()
    Out[10]: <QuerySet [<Doctor: 1번 의사 alice>]>
    
    In [11]: patient2.doctors.all()
    Out[11]: <QuerySet [<Doctor: 1번 의사 alice>]>
    ```
    
- 예약 취소하기 (삭제)
    
    ```powershell
    # doctor1이 patient1 진료 예약 취소
    In [12]: doctor1.patient_set.remove(patient1)
    
    In [13]: doctor1.patient_set.all()
    Out[13]: <QuerySet [<Patient: 2번 환자 dane>]>
    
    In [14]: patient1.doctors.all()
    Out[14]: <QuerySet []>
    ```
    
    ```powershell
    # patient2가 doctor1 진료 예약 취소
    In [15]: patient2.doctors.remove(doctor1)
    
    In [16]: patient2.doctors.all()
    Out[16]: <QuerySet []>
    
    In [17]: doctor1.patient_set.all()
    Out[17]: <QuerySet []>
    ```
    

### related_name argument

- target model이 source model을 참조할 때 사용할 manager name
    - ForeignKey()의 related_name과 동일
    
    ```powershell
    class Patient(models.Model):
    		# related_name을 통해 역참조를 할 경우에도 patient_set이 아닌 patients로 사용 가능
        doctors =models.ManyToManyField(Doctor, related_name='patients')
        name = models.TextField()
    
        def __str__(self):
            return f'{self.pk}번 환자 {self.name}'
    ```
    
- related_name 설정 값 확인
    
    ```powershell
    In [1]: doctor1 = Doctor.objects.create(name='alice')
    
    #에러 발생 (related_name 을 설정하면 기존 _set manager는 사용할 수 없음)
    In [2]: doctor1.patient_set.all()
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-2-e81b89c43a95> in <module>
    ----> 1 doctor1.patient_set.all()
    
    AttributeError: 'Doctor' object has no attribute 'patient_set'
    
    # 변경 후
    In [3]: doctor1.patients.all()
    Out[3]: <QuerySet []>
    
    ```
    

### thorough argument

- 개요
    - 중개 모델을 직접 작성
        
        ⇒ 중개 테이블을 수동으로 지정하려는 경우 `through` 옵션을 사용하여 사용하려는 중    개 테이블을 나타내는 Django 모델을 지정할 수 있음
        
    - 가장 일반적인 용도는 `중개테이블에 추가 데이터를 사용` 해 다대다 관계와 연결하려는 경우
- through 설정 및 Reservation Class 수정
    - 예약 정보에 증상과 예약일이라는 추가 데이터가 생김
    
    ```python
    class Patient(models.Model):
    		# through를 사용하면 Reservation을 직접 호출할 일 없음!
        doctors =models.ManyToManyField(Doctor, related_name='patients', through='Reservation') # 환자가 의사를 참조함 Doctor에 넣으면 반대
        name = models.TextField()               
    
        def __str__(self):
            return f'{self.pk}번 환자 {self.name}'
    
    class Reservation(models.Model):
        doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
        patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
        symptom = models.TextField()
        reserved_at = models.DateTimeField(auto_now_add=True)
    
        def __str__(self):
            return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
    ```
    
    ⇒ 예약작업을 할때 reservation을 사용하여 저장하겠다는 의미.
    
- 데이터베이스 초기화 후 Migration 진행 및 shell_plus 실행
    1.  migration 파일(`0001_initial.py`) 삭제
    2. 데이터베이스 파일 (`db.sqlide3`)삭제
    3. migration
    4. migrate
    5. shell_plus
- 의사 1명과 환자 2명 생성
    
    ```powershell
    In [1]: doctor1 = Doctor.objects.create(name='alice')
    In [2]: patient1 = Patient.objects.create(name='carol')
    In [3]: patient2 = Patient.objects.create(name='dane')
    ```
    
- 예약 생성1
    
    ```powershell
    #1. Reservation class를 통한 예약 생성
    
    reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')
    reservation1.save()
    
    # ppt랑 다르게 related_name을 사용했으므로 patients로 불러옴
    doctor1.patients.all()
    patient1.doctors.all()
    ```
    
- 예약 생성2
    
    ```powershell
    #2. Paitent 객체를 통한 예약 생성
    
    patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})
    
    doctor1.patients.all()
    patient1.doctors.all()
    
    ```
    
- 예약 삭제
    
    ```powershell
    doctor1.patients.remove(patient1)
    patient2.doctors.remove(doctor1
    ```
    

### 정리

- M:N 관계로 맺어진 두 테이블에는 변화가 없음
- Django의 ManyToManyField은 중개 테이블을 자동으로 생성함
- Django의 ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음
    - 대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것
- N:1은 완전한 종속의 관계였지만 M:N은 의사에게 진찰받는 환자, 환자를 진찰하는 의사의 두 가지 형태로 모두 표현이 가능!

## ManyToManyField

### 개요

- ManyToManyField(to, **options)
- 다대다 관계 설정 시 사용하는 모델 필드
- 하나의 필수 위치인자(`M:N관계로 설정할 모델 클라스`)가 필요
- 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거 및 생성 가능
    - `add()`, `remove()` , `create()` , `clear()` , …

### 데이터베이스에서의 표현

- Django는 다대다 관계를 나타내는 중개 테이블을 만듦
- 테이블 이름은 ManyToManyField 이름과 이를 포함하는 모델의 테이블 이름을 조합하여 생성됨
- `db_table` arguments을 사용하여 중개 테이블의 이름을 변경할 수도 있음

### ManyToManyField’s Arguments

1. related_name
    - target model이 source model을 참조할 때 사용할 manager name
    - ForeignKey의 related_name과 동일
2. through
    - 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정
    - 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우에 사용
3. symmetrical
    - default: True
    - ManyToManyField가 동일한 모델(`on self`)을 가리키는 정의에서만 사용
    
    ```python
    # 예시
    
    class Person(models.Model):
    	friends = models.ManyToManyField('self')
    	# friends = models.ManyToManyField('self', symmetrical=False)
    ```
    
    - True일 경우
        - _set 매니저를 추가 하지 않음
        - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함(대칭)
        - `즉, 팔로우 하면 자동으로 팔로윙 됨`
    - 대칭을 원하지 않는 경우 False로 설정
        - Follow 기능 구현에서 다시 확인할 예정

### Related Manager

- N:1 혹은 M:N 관계에서 사용 가능한 문맥
- Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 `역참조시`에 사용할 수 있는 `manager를 생성` (`ex) _set`)
    - 우리가 이전에 모델 생성 시 objects 라는 매니저를 통해 queryset api를 사용했던 것처럼 related manager를 통해 queryset api를 사용할 수 있게 됨
- 같은 이름의 메서드여도 각 관계(N:1, M:N)에 따라 다르게 사용 및 동작됨
    - N:1에서는 target 모델 객체만 사용 가능
    - `M:N 관계에서는 관련된 두 객체에서 모두 사용 가능`
- 메서드 종류
    - `add(), remove()` , create(), clear(), set() 등

### methods

- `add()`
    - 지정된 객체를 관련 객체 집합에 추가
    - 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
    - 모델 인스턴스, 필드 값(`PK`)을 인자로 허용
- `remove()`
    - 관련 객체 집합에서 지정된 모델 개체를 제거
    - 내부적으로 QuerySet.delete()를 사용하여 관계가 삭제됨
    - 모델 인스턴스, 필드 값(`PK`)을 인자로 허용

# M:N (Article-User)

## 개요

- Articler과 User의 M:N 관계 설정을 통한 `좋아요` 기능 구현

## LIKE

### 모델 관계 설정

- ManyToManyField 작성
    
    ```python
    # article/models.py
    
    # Create your models here.
    class Article(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        # 추가 # 
        # 보통 참조하는 모델의 복수형을 사용하지만, 기능 구현을 고려해서 적어주는 것이 
    		# 가독성이 좋음
        like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    		# 생략 #
    ```
    
- Migration 진행 후 에러 확인
    
    ![에러.PNG](M%20N%2020513dd99bed4539afffdc22f1bebc6f/%25EC%2597%2590%25EB%259F%25AC.png)
    
    ⇒  이 관계에 있어서 기존의 역참조와 생성 역참조가 충돌했다
    
    ![충돌.PNG](M%20N%2020513dd99bed4539afffdc22f1bebc6f/%25EC%25B6%25A9%25EB%258F%258C.png)
    
    ⇒ related_name 생성 해야함
    
    ⇒ `기존 article_set을 articls로 바꿔도 되고 생성 article_set을 articles로 바꿔도 되지만, 보통 N:M의 관계에 있는 역참조를 바꿔줍니다.( like_articles )` 
    
- ManyToManyField에 related_name 작성 후 Migration & Migrate
    
    ```python
    # article/models.py
    
    # Create your models here.
    class Article(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        # 수정 #
    		# related_name 옵션 추가 #
        like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    		# 생략 #
    ```
    
- User-Article간 사용 가능한 related manager 정리
    
    ```python
    - article.user : 게시글을 작성한 유저 (N:1)
    - user.article_set : 유저가 작성한 게시글(역참조) (N:1)
    - article.like_users : 게시글을 좋아요한 유저 (M:N)
    - user.like_articles : 유저가 좋아요한 게시글(역참조) (M:N)
    ```
    

### LIKE 구현

- url 및 views 함수 작성
    
    ```python
    #articles/urls.py
    
    urlpatterns = [
        path('<int:article_pk>/likes/', views.likes, name='likes'),
    ]
    ```
    
    ```python
    #articles/views.py
    
    def likes(request, article_pk):
        article = Article.objects.get(pk=article_pk)
        # 좋아요 추가 및 취소를 무슨 기준으로 조건(if)를 작성할까?
        
    		# 1. 현재 게시글에 좋아요를 누른 유저 목록에 / 현재 좋아요를 요청하는 유저 여부
        # if request.user in article.like_users.all():    #이미 과거에 좋아요를 눌렀음
        
        # 2.현재 게시글에 좋아요를 누른 유저 중에 / 현재 좋아요를 요청하는 유저를 검색해서 존재하는 지 확인
          # get 대신 filter를 이용하는 이유는 get은 없으면 오류를 반환 (1번 보다 데이터가 클때 더 빠름)
        if article.like_users.filter(pk=request.user.pk).exists(): 
            # 좋아요 취소 (remove)
            article.like_users.remove(request.user)
        else:
            # 좋아요 추가 (add)
            article.like_users.add(request.user)    # 게시글에 현재 '좋아요' 할 유저와 관계를 추가
        return redirect('articles:index')
    
        # 싫어요 추가 (add)
        # 싫어요 취소 (remove)
    ```
    
- index 템플릿에서 각 게시글에 좋아요 버튼 출력
    
    ```html
    <!-- articles/index.html -->
    
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>Articles</h1>
    	<!--------------생략 ----------------->
      {% for article in articles %}
        <p><b>작성자 : {{ article.user }}</b></p>
        <p>글 번호 : {{ article.pk }}</p>
        <p>제목 : {{ article.title }}</p>
        <p>내용 : {{ article.content }}</p>
    	<!-------------추가------------->
        <div>
          <form action="{% url 'articles:likes' article.pk %}" method="POST">
            {% csrf_token %}
            {% if request.user in article.like_users.all %}
              <input type="submit" value="좋아요 취소">        
            {% else %}
              <input type="submit" value="좋아요">
            {% endif %}
          </form>
        </div>
    	<!--------------생략------------->
      {% endfor %}
    {% endblock content %}
    ```
    
    ![창 생성.PNG](M%20N%2020513dd99bed4539afffdc22f1bebc6f/%25EC%25B0%25BD_%25EC%2583%259D%25EC%2584%25B1.png)
    
    ⇒ 좋아요는 콤보상자 필요 없음
    
    ```python
    #articles/forms.py
    
    class ArticleForm(forms.ModelForm):
    
        class Meta:
            model = Article
            # fields = '__all__'
            exclude = ('user','like_users') # like_users 추가
    ```
    
    ![창 사라짐.PNG](M%20N%2020513dd99bed4539afffdc22f1bebc6f/%25EC%25B0%25BD_%25EC%2582%25AC%25EB%259D%25BC%25EC%25A7%2590.png)
    
    ⇒ 뿅 사라짐
    
    ![좋아요 확인.PNG](M%20N%2020513dd99bed4539afffdc22f1bebc6f/%25EC%25A2%258B%25EC%2595%2584%25EC%259A%2594_%25ED%2599%2595%25EC%259D%25B8.png)
    
    ![좋아요 확인2.PNG](M%20N%2020513dd99bed4539afffdc22f1bebc6f/%25EC%25A2%258B%25EC%2595%2584%25EC%259A%2594_%25ED%2599%2595%25EC%259D%25B82.png)
    
- 데코레이터 및 is_authenticated 추가
    
    ```python
    # POST 만 받아라
    @require_POST
    def likes(request, article_pk):
        # 인증된 사용자면
        if request.user.is_authenticated:
            article = Article.objects.get(pk=article_pk)
            ########## 생략 #############
            return redirect('articles:index')
        return redirect('accounts:login')
    ```
    

# M:N (User-User)

## 개요

- User 자기 자신과의 M:N 관계 설정을 통한 팔로우 기능 구현

## Profile

### 개요

- 자연스러운 follow 흐름을 위한 프로필 페이지를 먼저 작성
    - 보통 follow 버튼은 개인 페이지에 존재하기 때문에 pofile 부터 구현해보자!!

### profile 구현

- url 및 view 함수 작성
    
    ```python
    # accounts/urls.py
    
    urlpatterns = [
    		'''
    		이렇게 인스타를 따라하겠다고 프로필 빼고, 유저네임만 넣고 제일 윗쪽에
    		경로를 설정하면 모든 경로를 profile로 간다!
    		why? 모든 login, logout, ... 모두 string이므로 !!!! 
        '''
        # path('<str:username>/', views.profile, name='profile'),
        path('login/', views.login, name='login'),
        path('logout/', views.logout, name='logout'),
        path('signup/', views.signup, name='signup'),
        path('delete/', views.delete, name='delete'),
        path('update/', views.update, name='update'),
        path('password/', views.change_password, name='change_password'),
        path('profile/<str:username>/', views.profile, name='profile'),
    ]
    ```
    
    ```python
    # accounts/views.py
    
    from django.contrib.auth import get_user_model
    
    def profile(request, username):
        # User를 get_user_model을 통해 직접 가져와
        User = get_user_model()
        person = User.objects.get(username=username)
        context = {
            'person': person,
        }
        return render(request, 'accounts/profile.html', context)
    ```
    
- profile 템플릿 작성
    
    ```html
    <!-- accounts/profile.html -->
    
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>{{ person.username }}님의 프로필</h1>
    
      <h2>{{ person.username }}이 작성한 모든 게시글</h2>
      {% for article in person.article_set.all %}
        <div>{{ article.title }}</div>
      {% endfor %}
    
      <h2>{{ person.username }}이 작성한 모든 댓글</h2>
      {% for comment in person.comment_set.all %}
        <div>{{ comment.content }}</div>
      {% endfor %}
    
      <h2>{{ person.username }}이 좋아요한 모든 게시글</h2>
      {% for article in person.like_articles.all %}
        <div>{{ article.title }}</div>
      {% endfor %}
    
      <a href="{% url 'articles:index' %}">back</a>
    {% endblock content %}
    ```
    
- Profile 템플릿으로 이동할 수 있는 하이퍼 링크 작성
    
    ```html
    <p>
    	<!------------------- 게시글의 유저 프로필에 연동되어 있어야 함!! ------------>
      {% comment %} <b>작성자 : <a href="{% url 'accounts:profile' user.username%}">{{ article.user }}</a></b> {% endcomment %}
      <b>작성자 : <a href="{% url 'accounts:profile' article.user.username%}">{{ article.user }}</a></b>
    </p>
    ```
    
    - `article.user.username` 대신 `article.user` 만 적어도 된다!
        - `accounts/models.py`
            
            ```python
            class User(AbstractUser):
            	pass
            # 의 디폴트는
            class User(AbstractUser):
            	def __str__(self) -> str:
            		return self.username
            # 이므로
            ```
            

## Follow

### 모델 관계 설정

- ManyToManyField 작성 및 Migration 진행
    
    ```python
    # accounts/models.py
    
    class User(AbstractUser):
    		 # True로 하면 팔로우와 팔로윙 동시
        followings = models.ManyToManyField('self', symmetrical=False, related_name='followers') 
    ```
    
    ⇒ makemigrations ⇒ migrate
    
    ![중개테이블.PNG](M%20N%2020513dd99bed4539afffdc22f1bebc6f/%25EC%25A4%2591%25EA%25B0%259C%25ED%2585%258C%25EC%259D%25B4%25EB%25B8%2594.png)
    
    ⇒ 중개 테이블 생성
    

### Follow 구현

- url 및 view 함수 작성
    
    ```python
    # accounts/urls.py
    
    urlpatterns = [
    		# 생략 #
        path('<int:user_pk>/follow/', views.follow, name='follow'),
    ]
    ```
    
    ```python
    # accounts/views.py
    
    def follow(request, user_pk):
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=user_pk)
        # 나 자신을 팔로우 하면 안된다이!!
        if me != you:
            # 현재 내가(request.user) 그 사람의 팔로워 목록에 있다면
            if me in you.followers.all():
                # 언팔로우
                you.followers.remove(me)
            else:
                # 팔로우
                you.followers.add(me)
        return redirect('accounts:profile', you.username)
    ```
    
- 프로필 유저의 팔로잉, 팔로워 수 & 팔로우, 언팔로우 버튼 작성
    
    ```html
    <!-- accounts/profile.html -->
    
    {% extends 'base.html' %}
    
    {% block content %}
    <h1>{{ person.username }}님의 프로필</h1>
      <div>
        팔로워 : {{ person.followers.all|length }} / 팔로잉 : {{ person.followings.all|length }}
      </div>
        <!--프로필 주인은 팔로잉 버튼 안보이게!!-->
        {% if request.user != person %}
        <div>
          <form action="{% url 'accounts:follow' person.pk %}" method="POST">
            {% csrf_token %}
            {% if request.user in person.followers.all %}
              <input type="submit" value="언팔로우">
            {% else %}
              <input type="submit" value="팔로우">
            {% endif %}
          </form>
        </div>
        {% endif %}
    <!------------------------- 생략 ------------------------>
    {% endblock content %}
    ```
    

---

추가자료!!(22/10/13)

# Fixtures

# Providing data with fictures

# Improve Query