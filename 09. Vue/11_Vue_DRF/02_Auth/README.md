# Vue with DRF (2) - 인증

# DRF Auth System

## (1) 개요

### 1. Authentication - 인증, 입증

- 자신이라고 주장하는 사용자가 누구인지 확인하는 행위
- 모든 보안 프로세스의 첫 번째 단계 (가장 기본 요소)
    
    ⇒ 내가 누구인지를 확인하는 과정
    
- 401 Unathorized
    
    ⇒ 비록 HTTP 표준에서는 ‘미승인’을 명확히 하고 있으나, 의미상 이 응답은 ‘비인증’을 의미
    

### 2. Authorization - 권한 부여, 허가

- 사용자에게 특정 리소스 또는 기능에 대한 액세스 권한을 부여하는 과정(절차)
- 보안 환경에서 권한 부여는 항상 인증이 먼저 필요함
    - 사용자는 조직에 대한 액세스 권한을 부여 받기 전에 먼저 자신의 ID가 진짜인지 먼저 확인해야 함
- 서류의 등급, 웹 페이지에서 글을 조회 & 삭제 & 수정할 수 있는 방법, 제한 구역
    
    ⇒ 인증이 되었어도 모든 권한을 부여 받은 것은 아님
    
- 403 Forbidden
    - 401과 다른 점은 서버는 클라이언트가 누구인지 알고 있음!

## (2) 인증 방법 (How to authentication determined)

### 1. `TokenAuthentication` 방법 채택

- 매우 간단하게 구현가능
- 기본적인 보안 기능 제공
- 다양한 외부 패키지 존재

### 2. 정의

- settings.py에서 `DEFAULT_AUTHENTICATION_CLASSES`를 정의
    
    ⇒  TokenAuthentication 인증 방식을 사용할 것임을 명시
    

### 3. 사용 방법

- INSTALLED_APPS에 `rest_framework.authtoken` 등록
- 각 User 마다 고유 Token 생성
- 생성한 Token을 각 User에게 발급
    - User는 발급 받은 Token을 요청과 함께 전송
    - Token을 통해 User 인증 및 권한 확인
- Token 발급 방법
    
    ```python
    def some_view_func(request):
    	token = Token.objects.create(user= ...)
    	return Response({ 'token': token.key })
    ```
    
- User는 발급 받은 Token을 headers에 담아 요청과 함께 전송
    
    (단, 반드시 Token 문자열 함께 삽입)
    
    ⇒ 삽입해야 할 문자열은 각 인증 방식 마다 다름
    
- Authorization HTTP headers 작성 방법
    
    `Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b` 
    
    ⇒ 사이사이 띄어쓰기도 정확히 해줘야 함
    

## (3) dj-rest-auth 라이브러리

### 1. 정의

- 회원가입, 인증, 비밀번호 재설정, 사용자 세부 정보 검색, 회원 정보 수정 등을 위한 REST API end point 제공

### 2. 사용방법

1. 패키지 설치
    
    `$ pip install dj-rest-auth`
    
2. App 등록
    
    settings.py
    
    ```python
    INSTALLED_APPS = [
        ...
        # Auth
        'rest_framework.authtoken',
        'dj_rest_auth',
    
        ...
    ]
    ```
    
3. url 등록
    
    ```python
    # my_api/urls.py
    urlpatterns = [
    		...
        path('accounts/', include('dj_rest_auth.urls')),
    ]
    ```
    
4. auth.User를 accounts.User로 변경 
    - DB 제거
    - settings.py
        - `AUTH_USER_MODEL = 'accounts.User’`
    - makemigrations & migrate
    - 결과 확인
        
        ![Untitled](Vue%20with%20DRF%20(2)%20-%20%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%B3%E1%86%BC%202a81065298da4c449749aabc282b7d04/Untitled.png)
        
        ⇒ 와옹 엄청 많이 생김
        
        ⇒ 근데 `회원가입은 없음`! why? 이미 인증이 되어 있는 값들만 고려하므로!
        
        ⇒ 회원가입은 토큰을 생성한다는 점에서 `핵심!!`
        
        ![Untitled](Vue%20with%20DRF%20(2)%20-%20%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%B3%E1%86%BC%202a81065298da4c449749aabc282b7d04/Untitled%201.png)
        
        ⇒ 지금은 단순 Registration 기능을 사용하지만, 추후에 Social Authentication 기능 써봐
        
        [`https://dj-rest-auth.readthedocs.io/en/latest/`](https://dj-rest-auth.readthedocs.io/en/latest/)
        
5. Registeration
    - django-allauth 설치
        
        `pip install 'dj-rest-auth[with_social]'`
        
    - App 등록 및 SITE_ID 설정
        
        ```python
        INSTALLED_APPS = [
            ...
        
            # registration
            'django.contrib.sites',
            'allauth',
            'allauth.account',
            'allauth.socialaccount',
            'dj_rest_auth.registration',
        
             ...
        ]
        ```
        
    - my_api/urls.py 에  경로 설정
        
        ```python
        urlpatterns = [
            ...
            path('accounts/signup/', include('dj_rest_auth.registration.urls'))
        ]
        ```
        
    - migrate
    - 페이지 확인 (`/accounts/signup/`)
        
        ![Untitled](Vue%20with%20DRF%20(2)%20-%20%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%B3%E1%86%BC%202a81065298da4c449749aabc282b7d04/Untitled%202.png)
        
        ⇒ Get method는 접근 불가
        
        ⇒ 회원가입 POST 요청 양식 제공 (email은 생략가능)
        
6. Sign up & Login
    - 회원 가입 요청 후 결과 확인
        
        ⇒ 요청에 대한 응답으로 Token 발급
        
    - 로그인 시에도 동일한 토큰 발급
        
        ⇒ 정상적인 로그인 가능
        
    - 발급 받은 토큰은 테스트를 위해 기록
    
    ![Untitled](Vue%20with%20DRF%20(2)%20-%20%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%B3%E1%86%BC%202a81065298da4c449749aabc282b7d04/Untitled%203.png)
    
7. Password change
    - DRF 자체 제공 HTML form에서는 토큰을 입력할 수 있는 공간이 없음
        
        ⇒ Postman에서 진행
        
        ![Untitled](Vue%20with%20DRF%20(2)%20-%20%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%B3%E1%86%BC%202a81065298da4c449749aabc282b7d04/Untitled%204.png)
        
        ⇒ 누가 보냈는 지 안 알려줘서 403 에러!
        
        ⇒ Token을 보내줘야함
        
    - Headers에 Token을 보내줌
        
        ![Untitled](Vue%20with%20DRF%20(2)%20-%20%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%B3%E1%86%BC%202a81065298da4c449749aabc282b7d04/Untitled%205.png)
        
        ⇒ 그래도 403 에러가 발생!!
        
        ⇒ why? 등록 안해줌
        
    - settings.py
        
        ```python
        REST_FRAMEWORK = {
            # Authentication
            'DEFAULT_AUTHENTICATION_CLASSES': [
                'rest_framework.authentication.TokenAuthentication',
            ],
        }
        ```
        
        ![Untitled](Vue%20with%20DRF%20(2)%20-%20%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%B3%E1%86%BC%202a81065298da4c449749aabc282b7d04/Untitled%206.png)
        
    1. Permission settings
        - 공식문서
            
            [`https://www.django-rest-framework.org/api-guide/permissions/`](https://www.django-rest-framework.org/api-guide/permissions/)
            
        - 권한 세부 설정
            1. 모든 요청에 대해 인증을 요구하는 설정
            2. 모든 요청에 대해 인증이 없어도 허용하는 설정
            
            ```python
            REST_FRAMEWORK = {
                # Authentication
                ...
            
                # permission
                'DEFAULT_PERMISSION_CLASSES': [
                    # 'rest_framework.permissions.IsAuthenticated',     # 인증되면 모두 허용
                    'rest_framework.permissions.AllowAny',
                ],
            }
            ```
            
            ```python
            #articles/views.py
            
            # permission Decorators
            from rest_framework.decorators import permission_classes
            from rest_framework.permissions import IsAuthenticated
            
            @api_view(['GET', 'POST'])
            @permission_classes([IsAuthenticated])  # 토큰이 없으면 접근 불가
            def article_list(request):
                ...
            ```
            
            ⇒ 글 생성할 때도 headers에서 토큰을 부여해야함