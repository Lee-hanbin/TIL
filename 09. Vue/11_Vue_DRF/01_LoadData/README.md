# Vue with DRF (1) - 데이터 불러오기

# Vue with DRF

## (1) 개요

- Server와 Client의 통신 방법 이해
- CORSR 이슈 이해하고 해결하기
- DRF Auth System 이해
- Vue와 API server 통신하기

## (2) Server & Client

### 1. Server `(DRF)`

- 정의
    - 클라이언트에게 `정보` 와 `서비스` 를 제공하는 컴퓨터 시스템
    - 서비스 전체를 제공 == Django Web Service
    - 정보를 제공 == DRF API Service
    
- 내용
    - 서비스 전체를 제공 == Django Web Service
        - **Django를 통해 전달방은 HTML에는 하나의 웹 페이지를 구성할 수 있는 모든 데이터가 포함**
            
            ⇒ 서버에서 모든 내용을 렌더링 하나의 HTML 파일로 제공
            
            ⇒ 정보를 포함한 web 서비스를 구성하는 모든 내용을 서버 측에서 제공
            
    - 정보를 제공 == DRF API Service
        - Django를 통해 관리하는 정보만을 클라이언트에게 제공
        - DRF를 사용하여 JSON으로 변환

### 2.  Client `(Vue)`

- 정의
    - `Server가 제공하는 서비스에 적절한 요청`을 통해 `Server로부터 반환 받은 응답을 사용자에게 표현`하는 기능을 가진 프로그램 혹은 시스템
- 내용
    - Server가 제공하는 서비스에 적절한 요청
        
        ⇒ Server가 정의한 방식대로 요청 인자를 넘겨 요청
        
        ⇒ Server는 정상적인 요청에 적합한 응답 제공
        
    - Server로부터 반환 받은 응답을 사용자에게 표현
        - 사용자의 요청에 적합한 data를 server에 요청하여 응답 받은 결과로 적절한 화면을 구성

## (3) Back 과 front 사전 준비

### 1. Back

- 가상환경
- migrate
- loaddata
- runserver

### 2. front

- path 설정
- component 간 상속관계
- axios 설치 (`$ npm i axios`)
- store/index.js 의 actions에서 사용하기 위해 axios 불러서 사용
- Django Server의 URL 을 할당 받아서 사용
    - `const API_URL = 'http://127.0.0.1:8000'`

```python
⇒ Django에서는 데이터를 잘 보내줘서 200응답이지만, Vue에서는 error 발생

⇒ CORS 정책에 의해 block 처리 당했다 

⇒ header가 없는 데이터는 받지 못한다.
```

## (4) CORS

- Cross-Origin Resource Sharing

### 1. 발생

- 브라우저가 요처을 보내고 서버의 응답이 브라우저에 도착
    - Server의 log는 200을 반환
        
        ⇒ Server는 정상적으로 응답했지만 브라우저가 막음
        
- 보안상의 이유로 브라우저는 `동일 출처 정책(SOP)` 에 의해 다른 출처의 리소스와 상호작용 하는 것을 제한 함

```python
#SOP(Same-Origin Policy)
- '동일 출처 정책'
- 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호작용 하는 것을 제한
- 잠재적으로 해로울 수 있는 문서를 분리함으로써 공격받을 수 있는 경로를 줄임
```

```python
#Origin
- URL의 Protocol, Host, Port를 모두 포함하여 출처라고 부름
```

![Untitled](Vue%20with%20DRF%20(1)%20-%20%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%87%E1%85%AE%E1%86%AF%E1%84%85%E1%85%A5%E1%84%8B%E1%85%A9%E1%84%80%E1%85%B5%2064e784013fc241b3986d85aebdb30055/Untitled.png)

### 2. CORS - (`교차 출처 리소스 공유` )

- 추가 `HTTP Header`를 사용하여, 특정 출처에서 실행 중인 웹 어플리케이션이 `다른 출처의 자원에 접근할 수 있는 권한` 을 부여하도록 브라우저에 알려주는  체제
    - 어떤 출처에서 자신의 컨텐츠를 불러갈 수 있는지 `서버에 지정`할 수 있는 방법
- 리소스가 자신의 출처와 다를 때 교차 출처 HTTP 요청을 실행
    
    ⇒ 만약, 다른 출처의 리소스를가져오기 위해서는 이를 제공하는 서버가 브라우저에게 `다른 출처지만 접근해도 된다는 사실`을 `알려`야함
    
    ⇒ 교차 출처 리소스 공유 정책 (CORS policy)
    

### 3. CORS policy (`교차 출처 리소스 공유 정책`)

- 다른 출처에서 온 리소스를 공유하는 것에 대한 정책
- CORS policy에 위배되는 경우 브라우저에 해당 응답 결과를 사용하지 않음
    - Server에서 응답을 주더라도 브라우저에서 거절
- 다른 출처의 리소스를 불러오려면 그 출처에서 `올가른 CORS header` 를 포함한 응답을 반환

## (5) CORS 정책 해결 방안

- CORS 표준에 의해 추가된 HTTP Response Header를 통해 이를 통제 가능
- HTTP Response Header 예시
    - `Access-Control-Allow-Origin`
    - Access-Control-Allow-Credentials
    - Access-Control-Allow-Headers
    - Access-Control-Allow-Methods
- `Access-Control-Allow-Origin`
    - 단일 출처를 지정하여 브라우저가 해당 출처가 리소스에 접근하도록 허용

### 1. 해결 방안 (Django-cors-headers library 사용)

- `응답에 CORS header를 추가` 해주는 라이브러리
- 다른 출처에서 Django 애플리케이션에 대한 브라우저 내 요청을 허용
1. `pip install django-cors-headers` 
2. `pip freeze > requirements.txt`
3. settings.py
    
    ```python
    INSTALLED_APPS = [
    		...
        # CORS policy
        "corsheaders",
    		...
    ]
    ```
    
    ```python
    MIDDLEWARE = [
        ...
        "corsheaders.middleware.CorsMiddleware",
        'django.middleware.common.CommonMiddleware',
    		...
    ]
    ```
    
    ```python
    # Vue server 주소에게 header 보내줘서 해결 (추가)
    CORS_ALLOWED_ORIGINS = [
        'http://localhost:8080',
    ]
    ```
    
    ![Untitled](Vue%20with%20DRF%20(1)%20-%20%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%87%E1%85%AE%E1%86%AF%E1%84%85%E1%85%A5%E1%84%8B%E1%85%A9%E1%84%80%E1%85%B5%2064e784013fc241b3986d85aebdb30055/Untitled%201.png)
    
    ⇒ 서버에서 데이터 잘 받아옴
    
    ![Untitled](Vue%20with%20DRF%20(1)%20-%20%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%87%E1%85%AE%E1%86%AF%E1%84%85%E1%85%A5%E1%84%8B%E1%85%A9%E1%84%80%E1%85%B5%2064e784013fc241b3986d85aebdb30055/Untitled%202.png)
    
    ⇒ 받은 header가 어디 있는 지 확인 가능
    

## (6) Article Read

### 1. 응답 받은 데이터 구조 확인

- `data Array` 에 각 게시글 객체
- 각 게시글 객체는 다음으로 구성
    1. id
    2. title
    3. content
    
    ![Untitled](Vue%20with%20DRF%20(1)%20-%20%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%87%E1%85%AE%E1%86%AF%E1%84%85%E1%85%A5%E1%84%8B%E1%85%A9%E1%84%80%E1%85%B5%2064e784013fc241b3986d85aebdb30055/Untitled%203.png)
    

### 2. `store/index.js` 수정

- 기존 articles 데이터 삭제
- Mutations 정의
    - 응답 받아온 데이터를 state에 저장
    - `store/index.js`
        
        ```jsx
        const API_URL = 'http://127.0.0.1:8000'     // Django server URL 작성
        
        export default new Vuex.Store({
          state: {
            articles: [],
          },
          getters: {
          },
          mutations: {
            GET_ARTICLES(state, articles) {
              state.articles = articles
            }
          },
          actions: {
            getArticles(context) {
              axios({
                method: 'get',
                url: `${API_URL}/api/v1/articles/`
              })
                .then((response) => {
                  // console.log(response, context)
                  // console.log(response.data)
                  context.commit('GET_ARTICLES', response.data)
                })
                .catch((error) => {
                  console.log(error)
                })
            }
          },
          modules: {
          }
        })
        ```
        

## (7) Article Create

### 1. `views/CreateView.vue` 코드 확인

- 게시글 생성을 위한 form을 제공
- `v-model.trim` 을 활용해 사용자 입력 데이터에서 공백 제거
- `.prevent` 를 활용해 form의 기본 이벤트 동작 막기
- title, content가 비었다면 alert를 통해 경고창을 띄움
- AJAX 요청을 보내지 않도록 return 시켜 함수를 종료
- `views/CreateView.vue`
    
    ```jsx
    // CreateView.vue
    
    <template>
      <div>
        <h1>게시글 작성</h1>
        <form @submit.prevent="createArticle">  
          ...
        </form>
      </div>
    </template>
    
    <script>
    export default {
      name: 'CreateView',
      data() {
        return {
          title: null,
          content: null,
        }
      },
      methods: {
        createArticle() {
          const title = this.title
          const content = this.content
          if (!title) {
            alert('제목을 입력해주세요')
            return
          } else if (!content) {
            alert('내용을 입력해주세요')
            return
          }
        }
      }
    }
    </script>
    ```
    

### 2. `router/index.js`에 가서 path 생성

### 3. `ArticleView.vue` 에 가서 CreateView path 생성

- `ArticleView.vue`
    
    ```jsx
    <template>
      <div>
        ...
        <router-link :to="{ name: 'CreateView' }">[CREATE]</router-link>
        ...
      </div>
    </template>
    
    <script>
    ...
    </script>
    ```
    

### 4. CreateView.vue 코드 수정

- createArticle method 수정 게시글 생성 완료 후, ArticleView로 이동
- 응답 확인을 위해 정의한 인자 `response` 제거
- `CreateView.vue`
    
    ```jsx
    <template>
      ...
    </template>
    
    <script>
    import axios from 'axios'
    const API_URL = 'http://127.0.0.1:8000'
    
    export default {
      name: 'CreateView',
      data() {
        return {
          title: null,
          content: null,
        }
      },
      methods: {
        createArticle() {
          ...
          axios({
            method: 'post',
            url: `${API_URL}/api/v1/articles/`,
            data: {
              title: title,
              content: content
            },
          })
            // .then((response) => {
            //   console.log(response)
            .then(() => {
              this.$router.push({ name: 'ArticleView' })
            })
            .catch(error => console.log(error))
        }
      }
    }
    </script>
    ```
    

```jsx
// 비효율적인 부분 존재
1. 전체 게시글 정보를 요청해야 새로 생성된 게시글을 확인 할 수 있음
2. 만약 vuex state를 통해 전체 게시글 정보를 관리하도록 구성한다면, 내가 새롭게
	생성한 게시글은 확인할 수 있겠지만 나 이외의 유저들이 새롭게 생성한 게시글을
	불러오는 시점에 대한 의문
3. 무엇을 기준으로 새로운 데이터가 생겼다는 것을 확인 할 수 있을까?
```

## (8) Article Detail

### 1. `views/DetailView.vue` 코드

- 게시글 상세 정보를 표현할 컴포넌트
- AJAX 요청으로 응답 받아올 article의 살세 정보들을 표현

### 2. `router/index.js`에서 경로 설정

### 3. `components/ArticleListItem.vue` 에서 링크 설정

- router-link를 통해 특정 게시글의 id 값을 동적 인자로 전달
- 게시글 상세 정보를 Server에 요청
- `ArticleListItem.vue`
    
    ```jsx
    <template>
      <div>
        ...
        <router-link :to="{ name: 'DetailView', params: { id: article.id } }">[DETAIL]</router-link>
        <hr>
      </div>
    </template>
    
    ```
    

### 4. `views/DetailView.vue` 에서 AJAX 요청

- this.$route.params를 활용해 컴포넌트가 create될 때, 넘겨받은 id로 상세 정보 AJAX 요청
- `DetailView.vue`
    
    ```jsx
    <template>
      <div>
        ...
      </div>
    </template>
    
    <script>
    import axios from 'axios'
    
    const API_URL = 'http://127.0.0.1:8000'
    
    export default {
      name: 'DetailView',
      data() {
        return {
          
        }
      },
      created() {
        this.getArticleDetail()
      },
      methods: {
        getArticleDetail() {
          axios({
            method: 'get',
            url: `${API_URL}/api/v1/articles/${ this.$route.params.id }`
          })
            .then((response) => {
              console.log(response)
            })
            .catch((error) => {
              console.log(error)
            })
        }
      }
    }
    </script>
    ```
    
    ⇒ data에 return {} 을 안 적어주면 에러발생
    

### 5. `views/DetailView.vue` 에서 데이터 받아오기

- 응답 받은 정보를 data에 저장
- data에 담기까지 시간이 걸리므로 optional chaining을 활용해 데이터 표기
- `DetailView.vue`
    
    ```jsx
    <template>
      <div>
        <h1>Detail</h1>
        <p>글 번호 : {{ article?.id }}</p>
        <p>제목 : {{ article?.title }}</p>
        <p>내용 : {{ article?.content }}</p>
        <p>작성시간 : {{ article?.created_at }}</p>
        <p>수정시간 : {{ article?.updated_at }}</p>
      </div>
    </template>
    
    <script>
    import axios from 'axios'
    const API_URL = 'http://127.0.0.1:8000'
    export default {
    	...
    	data() {
        return {
          article: null
        }
      },
      ...
      methods: {
        getArticleDetail() {
          axios({
    	       ...
          })
            .then((response) => {
              ...
              this.article = response.data
            })
            ...
            })
        }
      }
    }
    </script>
    ```