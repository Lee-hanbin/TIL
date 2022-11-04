# 

# 1. 팀 구성

- 이한빈 : Navigator, Driver / views, templates 구현

- 최종현 : Driver / templates (html, css) 구현

- 안예나 : Driver / views 구현

# 2. 과제 수행

### A. 유저 팔로우 기능

AJAX 통신을 이용, 비동기적으로 팔로우 기능 구현

### B. 리뷰 좋아요 기능

AJAX 통신을 이용, 비동기적으로 좋아요 기능 구현

### C. Movies 앱 기능

1. 전체 영화 목록 조회 (index)

전체 영화 데이터의 쿼리셋을 불러와서 출력함

2. 단일 영화 상세 조회 (detail)

해당 영화 데이터 쿼리를 불러와서 출력함

3. 영화 추천 기능 (recommended)

사용자가 추천 받고 싶은 영화 장르를 선택하면 그 장르에 해당하는 영화를 출력함

- view함수

```python
@require_http_methods(['GET', 'POST'])
def recommended(request):
    if request.method == "POST":
        genre = Genre.objects.get(name=request.POST.get('name'))
        movies = Movie.objects.filter(genres=genre.pk)
    else: 
        movies = None
    genres = Genre.objects.all()
    context = {
        'movies': movies,
        'genres': genres,
    }
    return render(request, 'movies/recommended.html', context)
```

GET과 POST 요청을 받아 처리를 다르게 함

GET일 경우 movies에 None을 반환하고, POST일 경우 request에 있는 장르 이름 데이터를 활용하여 선택된 장르에 해당하는 영화 쿼리셋을 반환

- 초기 페이지: 장르 select form 및 안내 문구 출력 (movies 쿼리셋이 없는 상태)

- 장르 선택시: 장르 select form 출력하여 장르 변경 가능하게 함, 선택한 장르의 영화 목록을 출력 (movies 쿼리셋이 있는 상태)

### (+) 추가 선택 사항

Bootstrap을 사용하여 출력되는 페이지를 디자인함

# 3. 프로젝트를 마치며..

- 예나

Bootstrap이 너무 어려웠다...

배운 것들이 생각보다 적용이 잘 되어서 재미있었다

다음에는 vue사용해서 해보면 좋을 것 같다

데이터도 fixtures가 아니라 api에서 받아오는 방식으로 하면 더 다양한 데이터를 활용할 수 있을 것 같다.

---

- 종현

## Project 08 : 알고리즘을 이용한 서버 활용

커뮤니티 게시판 기능, 영화 데이터를 활용하여 인덱스 페이지와 디테일 페이지 만들기.  
회원 정보를 기반으로 영화 추천 알고리즘을 구현하고 해당 내용을 렌더링 하기.  


### QuerySet을 자바스크립트 객체로 활용하기.

1. Movie.objects.all()을 활용하여 context를 전달할 시, QuerySet 객체 형식의 string으로 전달되어 자바스크립트에서 활용 불가능한 문제가 있음.
2. 이에 따라 `<script></script>`에서 활용 시에 `{{식별자|escapejs}}` 혹은 `{{식별자|safe}}` 등으로 파일을 전달 받을 것.
3. all()을 통해 받은 QuerySet객체는 컨트롤이 어려우므로 시리얼라이저 혹은 views에서 처리할 것.

### 컨텐츠의 크기에 비례하여 텍스트에 말줄임표 적용하기

부트스트랩의 ellipsis 클래스는 지나치게 텍스트 크기가 커지는 문제가 있다. text-truncate 클래스는 지나치게 크기가 작은 문제가 있다. (`style="max-width: 150px;"`와 같이 너비를 정해야 한다.) 

하기의 .txt_post 스타일을 클래스에 적용하면 원하는 라인수를 자유롭게 정할 수 있다.  

```html
  <style>
    .txt_post {
      overflow: hidden;
      text-overflow: ellipsis;
      display: -webkit-box;
      -webkit-line-clamp: 3; /* 라인수 */
      -webkit-box-orient: vertical;
      word-wrap:break-word; 
      line-height: 1.2em;
      height: 3.6em; /* line-height 가 1.2em 이고 3라인을 자르기 때문에 height는 1.2em * 3 = 3.6em */
    }
  </style>
```

### 마우스를 올렸을 때에 컨텐츠 보이기

css만을 이용해 컨텐츠에 마우스를 올렸을 때에 표시되도록 할 수 있다.  
이때 초기값을 display none으로 둔다.  

부모 요소에 :hover 선택자를 넣고,  
자식 요소에 display 속성을 돌려줄 수 있다.

```css
.showme {
  display: none;
}

.showhim:hover .showme {
  display: block;
}
```

모든 자식요소에 적용하고 싶은 경우 아래와 같이 한다.

```css
div {
    display: none;
}

a:hover > div {
    display: block;
} 
```

[출처](http://daplus.net/css-css-%EB%A7%8C-%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC-a-%EC%9C%84%EC%97%90-%EB%A7%88%EC%9A%B0%EC%8A%A4%EB%A5%BC-%EC%98%AC%EB%A6%AC%EB%A9%B4-div%EA%B0%80-%ED%91%9C%EC%8B%9C%EB%90%A9%EB%8B%88/)

이때 부모요소의 크기가 더 큰 쪽이 사용자 경험상 더 좋다.  


### 추천 알고리즘 구현

HTML의 select-option 을 이용하여 구현을 진행함.    
form 태그의 'name'과 views를 연결하여 진행  

```py
if request.method == "POST":
        genre = Genre.objects.get(name=request.POST.get('name'))
```

N:M 관계가 정확히 이해되지 않아 get메서드를 두 번 사용.  

해당 데이터 장르 데이터를 이용하여 이를 render로 전달 후 처리.

### 느낀 점

1. DTL에 대한 이해의 부족. DTL와 `<script></script>`태그를 합치는 데에 어려움을 겪음. DRF와 VUE를 이용할 시 DRF와 VUE를 분리하여 관리하되 원활하게 API로 소통될 수 있도록 준비 할 것.

2. 데이터를 다루는데에 대한 이해 부족. 장고 모델에 대해 다시 한 번 공부할 것.

3. CSS파일을 등록하여 사용하는 것 보다 부트스트랩으로 일관되게 사용하는 것이 관리에 용이하다.

4. 그러나, 특수한 기능을 구현하기 위해서는 부트스트랩에만 의존하거나 부트스트랩을 커스텀하기 보다는 인라인 스타일 등을 이용하여 추가적인 기능을 넣는 것이 협업에 좋다.

5. 협업을 위해서는 최대한 로직을 단순하게 하고 명확하게 하며, 매 커밋 당 하나의 작업을 완벽히 끝내는 편이 좋다.  

---

- 한빈

# 알고리즘을 적용한 서버 구성

## 1. 프로젝트 목표

- 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web Application 제작
- AJAX 통신과 JSON 구조에 대한 이행
- Database many to one relationship(N:1)에 대한 이해
- Database many to many relationship(M:N)에 대한 이해
- 영화 추천 알고리즘 설계

## 2. 개발도구

- `Visual Studio Code`
- `Google Chrome`
- `Django 3.2+`
- `bootstrap 5`
- `css`

## 3. 프로젝트 과정

### (1) INDEX

- 유저 팔로우 기능
- 리뷰 좋아요 기능
- Movies 앱 기능
    1. 전체 영화 목록 조회
    2. 단일 영화 상세 조회
    3. 영화 추천 기능
- page style setting
  
    

### (2) 과정

- 유저 팔로우 기능
    - 팔로우 버튼을 클릭하는 경우, 페이지가 새로고침 되는 것이 아니라 AJAX 통신을 이용하여 서버에서 JSON 데이터를 받아와 상황에 맞게 HTML 화면을 구성합니다.
    - `views.py 의 follow 함수`
        - 회원 가입자만 이용이 가능하게 하고 팔로우, 팔로잉 여부와 그 누적 수를 카운팅하여 JsonResponse로 보내줍니다.
    - `profile.html`
        - form이 실행되면 scripts로 결과 를 가져와 비동기식으로 팔로우 기능만 동작시키게 하였습니다.
- 리뷰 좋아요 기능
    - 좋아요 버튼을 클릭하는 경우, AJAX통신을 이용하여 서버에서 JSON 데이터를 받아와 상황에 맞게 HTML 화면을 구성합니다.
    - `views.py의 like 함수`
        - 회원 가입자만 이용이 가능하게 하고 좋아요 클릭 여부에 따라 좋아요 버튼의 상태를 다르게 구현해 줬으며, 해당 카운팅을 JsonResponse로 보내줍니다.
    - `index.html`
        - 좋아요 버튼이 클릭되면 ‘좋아요 취소’ 가 나오면서 카운팅을 갱신해줍니다.
        - 좋아요 취소 버튼이 클릭되면 ‘좋아요’가 나오면서 카운팅을 갱신해줍니다.
- Movies 앱 기능
    1. 전체 영화 목록 조회 (`Index.html`)
        - Movie 모델 쿼리 셋에서 모든 데이터를 받아 출력합니다.
    2. 단일 영화 상세 조회 (`detail.html`)
        - index.html의 전체 영화 목록에서 영화 포스터를 클릭하면 영화에 대한 상세 정보가 나오도록 구현
        - genre가 Genre form에 들어있기 때문에 해당 부분을 역참조 하여 해결
    3. 영화 추천 기능 (`recommended.html`)
        - 사용자가 인증이 되어 있다면, 알고리즘을 활용하여 10개의 영화를 추천하여 제공
        - 알고리즘
            - 사용자에게 genre를 선택할 수 있는 select 옵션을 줍니다.
            - 사용자가 genre를 선택하면 해당 genre의 영화를 10개 이하 출력합니다.
- Page Style setting
    1. accounts
       
        ![캡처.PNG](PJT08%20d9e7d56340a64e62adf07f8f41622886/%25EC%25BA%25A1%25EC%25B2%2598.png)
        
    2. movie
        - `index.html`
        
        ![캡처.PNG](PJT08%20d9e7d56340a64e62adf07f8f41622886/%25EC%25BA%25A1%25EC%25B2%2598%201.png)
        
        - `recommended.html`
        
        ![전쟁.PNG](PJT08%20d9e7d56340a64e62adf07f8f41622886/%25EC%25A0%2584%25EC%259F%2581.png)
        

## 4. 리뷰

## (1) 힘들었던 부분

- django에 관련된 부분은 비교적 오랜기간 해왔기에 익숙했으나,  script에 관련된 부분에서 많은 얼려움이 있었씁니다.
  
    ⇒ 설정되어 있는 관계를 파악해서 원하는 데이터를 출력하는 작업이 까다로웠습니다.
    
- 페이지를 꾸미는 작업을 하게 되었는데 CSS 와 BOOTSTRAP의 지식이 오랜만이라 상기해내는데 많은 시간을 썼고, 결과물 조차 만족스럽지 못했습니다.

## (2) 느낀점

- 이론적인 부분이 아니라 실습으로서 모든 문제를 구현해보니 보다 확실히 이해할 수 있었다.
- SW 역량이 뛰어난 팀원들과 함께 했기에 프로젝트를 잘 마무리 할 수 있었지만, 비교적 많은 기여를 하지 못했다는 점이 아쉬웠습니다.
- 앞으로 최종 Pjt가 얼마 남지 않은 만큼 더 열심히 해서 제 팀원에게 힘을 싣어줄 수 있게 하겠습니다!