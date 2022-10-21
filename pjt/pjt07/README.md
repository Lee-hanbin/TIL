# PJT07

# DB 설계를 활용한 REST API 설계

## 1. 프로젝트 목표

- DRF를 활용한 API Server 제작
- Database many to one relationship(1:N)에 대한 이해
- Database many to many relationship(M:N)에 대한 이해

## 2. 프로젝트 과정

- 가상환경 설정, 활성화 및 패키지 설치
- 모델 생성 및 관계 설정
    
    ![모델.PNG](PJT07%200d2701801e024bbcbffef96a1f81c785/%25EB%25AA%25A8%25EB%258D%25B8.png)
    
    1.  Review class 가 Movie class를 1:N 참조
    2.  Movie class 가 Actor class를 N:M 참조 
        - 역참조를 movies로 명명
- 세 개의 모델을 Admin site에 등록하고, 데이터의 생성, 조회, 수정, 삭제
    
    ![admin.PNG](PJT07%200d2701801e024bbcbffef96a1f81c785/admin.png)
    
    1. 조회
        
        ![조회.PNG](PJT07%200d2701801e024bbcbffef96a1f81c785/%25EC%25A1%25B0%25ED%259A%258C.png)
        
    2. 생성
        
        ![생성.PNG](PJT07%200d2701801e024bbcbffef96a1f81c785/%25EC%2583%259D%25EC%2584%25B1.png)
        
    3. 수정
        
        ![수정.PNG](PJT07%200d2701801e024bbcbffef96a1f81c785/%25EC%2588%2598%25EC%25A0%2595.png)
        
    4. 삭제 
        
        ![삭제.PNG](PJT07%200d2701801e024bbcbffef96a1f81c785/%25EC%2582%25AD%25EC%25A0%259C.png)
        
    
    A. 전체 배우 목록 제공
    
    - serializer.py 작성
        
        ```python
        class ActorSerListializer(serializers.ModelSerializer):
        
            class Meta:
                model = Actor
                fields = '__all__'
        ```
        
        ⇒ serializer class를 통해 데이터를 json 형태로 변환
        
    - urls.py 작성
        
        ```python
        path('actors/', views.actor_list),
        ```
        
        ⇒ 경로 설정
        
    - views.py 작성
        
        ```python
        @api_view()
        def actor_list(request):
            actors = Actor.objects.all()
            serializers = ActorSerListializer(actors, many=True)
            return Response(serializers.data)
        ```
        
        ⇒ 함수를 정의하여 함수 호출 시 Actor에 담긴 json 파일 모두 가져오기
        
    
    B. 단일 배우 정보 제공
    
    - serializer.py작성
        
        ```python
        class Moivetitle(serializers.ModelSerializer):
        
            class Meta:
                model = Movie
                fields = ('title',)
        
        class ActorSerializer(serializers.ModelSerializer):
            # movie_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
            movies = Moivetitle(many=True, read_only=True)
            class Meta:
                model = Actor
                fields = '__all__'
        ```
        
        ⇒ Movie를 역참조하여 title만 가져오기
        
    - urls.py
        
        ```python
        path('actors/<int:actor_pk>/', views.artor_detail),
        ```
        
        ⇒ 경로에 키 값을 추가해서 보내준다.
        
    - views.py
        
        ```python
        @api_view()
        def artor_detail(request, actor_pk):
            actor = Actor.objects.get(pk=actor_pk)
            serializers = ActorSerializer(actor)
            return Response(serializers.data)
        ```
        
        ⇒ 키 값에 해당하는 배우의 정보를 출력한다.
        
    
    C.  전체 영화 목록 제공
    
    - serializer.py
        
        ```python
        class MoiveListSerializer(serializers.ModelSerializer):
        
            class Meta:
                model = Movie
                fields = ('title', 'overview',)
        ```
        
        ⇒ Movie에서 title 필드와 overviw 필드만 가져와 json 타입으로 반환
        
    - urls.py와 views.py는 A의 형태와 비슷
    
    D. 단일 영화 목록 제공
    
    - serializer.py
        
        ```python
        class Actorname(serializers.ModelSerializer):
        
            class Meta:
                model = Actor
                fields = ('name',)
        
        class MoiveSerializer(serializers.ModelSerializer):
            actors = Actorname(many=True, read_only=True)
            review_set = ReviewListSerializer(many=True, read_only=True)
            class Meta:
                model = Movie
                fields = '__all__'
        ```
        
        ⇒ Actor를 참조하여 name 필드를 가져오고, Review를 역참조하여 title과 content 값을 가져온다.
        
    - urls.py와 views.py는 B의 형태와 비슷
    
    E. 전체 리뷰 목록 제공
    
    - serializer.py
        
        ```python
        class ReviewListSerializer(serializers.ModelSerializer):
        
            class Meta:
                model = Review
                fields = ('title','content',)
        ```
        
    - urls.py와 views.py는 A, C의 형태와 비슷
    
    F. 단일 리뷰 조회 & 수정 & 삭제
    
    - serializer.py
        
        ```python
        class ReviewSerializer(serializers.ModelSerializer):
            # read_only를 하여 if문을 넘겨줌
            movie = Moivetitle(read_only=True)
            class Meta:
                model = Review
                fields = '__all__'
        ```
        
        ⇒ Movie를 참조하여 title 필드와  Review의 모든 필드를 json형태로 변환
        
    - urls.py는 다른 단일 조회 문제들과 비슷하게 pk를 받아온다
    - views.py
        
        ```python
        @api_view(['GET', 'PUT', 'DELETE'])
        def review_detail(request, review_pk):
            review = Review.objects.get(pk=review_pk)
        
            if request.method == 'GET':
                serializers = ReviewSerializer(review)
                return Response(serializers.data)
            
            elif request.method == 'PUT':
                serializers = ReviewSerializer(review, data=request.data)
                if serializers.is_valid(raise_exception=True):
                    serializers.save()
                    return Response(serializers.data)
            
            elif request.method == 'DELETE':
                review.delete()
                message_d = f'review {review_pk} is deleted'
                return Response(message_d, status=status.HTTP_204_NO_CONTENT)
        ```
        
        1. GET 요청이 들어오면 ReviewSerializer에 담겨있는 json의 pk에 해당하는 데이터를 반환
        2. PUT 요청이 들어오면 ReviewSerializer에 담겨있는 json의 pk에 해당하는 데이터를 수정하여 해당 Review모델의 모든 값이 입력되면 저장해주기
        3. DELETE 요청이 들어오면 ReviewSerializer에 담겨있는 json의 pk에 해당하는 데이터를 삭제하고 ‘review `pk` is deleted’를 출력해준다.
    
    G. 리뷰 생성
    
    - serializer.py ⇒ `ReviewSerializer`
    - urls.py
        
        ```python
        	path('movies/<int:movie_pk>/reviews/', views.create_review),
        ```
        
        ⇒ 경로에 키 값을 추가
        
    - views.py
        
        ```python
        @api_view(['POST'])
        def create_review(request, movie_pk):
            movie = Movie.objects.get(pk=movie_pk)
            serializers = ReviewSerializer(data=request.data)
            if serializers.is_valid(raise_exception=True):
                # serializers.save()
                serializers.save(movie=movie)
                return Response(serializers.data, status=status.HTTP_201_CREATED)
        ```
        
        ⇒ POST 요청이 들어오면 Movie의 Queryset pk에 해당하는 값을 입력
        
        ⇒ ReviewSerializer 클래스의 모든 인자에 값을 입력
        
        ⇒ 모든 인자 값이 입력되면 pk에 해당하는 movie 값도 할당해주면서 데이터 저장
        
        ⇒ 데이터 입력에 성공하면 201 응답
        
        ⇒ 데이터의 값이 다 저장되지 않았다면 400 응답
        
    
    ## 3. 리뷰
    
    ## (1) 힘들었던 부분
    
    - 모델과 관계를 설정하고 loaddata를 받아오는 과정에서 종속관계에 대해 따지는 것에 어려움을 느꼈습니다.
        
        ⇒ 문제에서 ERD를 주어 관계를 설정하는 과정에서 중개테이블 없이 관계를 설정하여 해당 테이블을 매꿔야 했기에 이 부분에서 많은 고민을 했습니다.
        
    - serializer class를 만들어 가는 과정에서 참조를 할 때, 전체가 아닌 부분적인 정보만 가져오는 방법에 대한 고민을 깊게 했습니다.
        
        ⇒ class를 하나 더 정의하여 필드를 한정해서 가져와 해결할 수 있었습니다.
        
    
    ## (2) 느낀점
    
    - 이론적인 부분이 아니라 실습으로서 모든 문제를 구현해보니 보다 확실히 이해할 수 있었다.
    - 단순히 DRF에 대한 학습이 아니라 1:N 관계, M:N 관계에 대해서도 학습할 수 있어서 얻은게 많은 프로젝트였습니다.