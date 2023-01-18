# Navigation Guard

# Navigation Guard

## (1) 개요

- Vue router를 통해 특정 URL에 접근할 때, 다른 url로 redirect를 하거나 해당 URL로의 접근을 막는 방법

## (2) 종류

1. 전역 가드
    - 애플리케이션 전역에서 동작
2. 라우터 가드
    - 특정 URL에서만 동작
3. 컴포넌트 가드
    - 라우터 컴포넌트 안에 정의

## (3) 전역 가드

### 1. Global Before Guard

- 다른 url주소로 이동할 때 항상 실행
- router/index.js에 `router.beforeEach()` 를 사용하여 설정
- 콜백 함수의 값으로 다음과 같이 3개의 인자를 받음
    - `to` : 이동할 URL 정보가 담긴 Route 객체
    - `from` : 현재 URL 정보가 담긴 Route 객체
    - `next` : 지정한 URL로 이동하기 위해 호출하는 함수
        - 콜백 함수 내부에서 반드시 한 번만 호출되어야 함
        - 기본적으로 `to`에 해당하는 `URL로 이동`
- URL이 변경되어 `화면이 전환되기 전` router.beforeEach()가 `호출`됨
- next를 호출하지 않으면 화면이 전환되지 않고 대기 상태가 됨
    - `next()가 호출되기 전까지 화면이 전환되지 않음`
    
    ⇒ 변경된 URL로 라우팅하기 위해서는 next()를 호출해줘야 함
    

### 2. Global Before Guard 실습

- `/home` 으로 이동하더라도 라우팅이 되지 않고 아래와 같이 로그만 출력됨
- `next()` 가 호출되지 않으면 화면이 전환되지 않음

```jsx
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
/////////////////////// router를 사용하기 때문에 router 아래 ////////////////
router.beforeEach((to, from, next) => {
  console.log('to', to)
  console.log('from', from)
  console.log('next', next)
})
////////////////////////////////////////////////////////////////////////////
export default router
```

![next X.PNG](Navigation%20Guard%201175af759a96423b90aaf6d4bcb2a0d8/next_X.png)

- `next()` 가 호출되어야 화면이 전환됨
    
    ```jsx
    router.beforeEach((to, from, next) => {
      console.log('to', to)
      console.log('from', from)
      console.log('next', next)
      next()      //next 추가! 
    })
    ```
    
    ![next O.PNG](Navigation%20Guard%201175af759a96423b90aaf6d4bcb2a0d8/next_O.png)
    
- About으로 이동해보기
    - `to`에는 `이동할 url`인 about에 대한 정보가, `from`에는 `현재 url`인 home에 대한 정보가 들어있음!

### 3. Login 여부에 따른 라우팅 처리

- Login이 되어있지 않다면 Login 페이지로 이동하는 기능 추가
    - LoginView.vue 생성
        
        ```jsx
        //views/LoginView.vue
        
        <template>
          <div>
            <h1>Login page</h1>
          </div>
        </template>
        
        <script>
        export default {
          name: 'LoginView',
        }
        </script>
        ```
        
    - index.js에 등록
        
        ```jsx
        import LoginVuew from '@/views/LoginView'
        
        const routes = [
          ...
          {
            path: '/login/',
            name: 'login',
            component: LoginVuew,
          }
        ]
        ```
        
    - LoginView에 대한 라우터 링크 추가
        
        ```html
        <!--App.vue-->
        
        <template>
          <div id="app">
            <nav>
              ...
              <router-link :to="{ name: 'login'}">Login</router-link>
            </nav>
            <router-view/>
          </div>
        </template>
        ```
        
- HellowView에 로그인을 해야만 접근할 수 있게 하기
    - 로그인 여부에 대한 임시 변수 생성
    - 로그인이 필요한 페이지를 저장
        - 로그인이 필요한 페이지들의 이름(라우터에 등록한 name)을 작성
    - 앞으로 이동할 페이지(to)가 로그인이 필요한 사이트인지 확인
    
    ```jsx
    //index.js
    
    router.beforeEach((to, from, next) => {
      //로그인 여부
      const isLoggedIN = false
    
      //로그인이 필요한 페이지
      const authPages= ['hello','home']
    
      // authPages라는 배열에 to에 들어있는 url의 name이 포함되어 있는 지 확인
      const isAuthRequired = authPages.includes(to.name) 
    })
    ```
    
- isAuthRequired 값에 따라 로그인이 필요한 페이지이고 로그인이 되어있지 않으면 Login 페이지로 이동
- 그렇지 않으면 기존 루트로 이동
- next()인지가 없을 경우 to로 이동
    
    ```jsx
    router.beforeEach((to, from, next) => {
      //로그인 여부
      const isLoggedIN = false
    
      //로그인이 필요한 페이지
      const authPages= ['hello','home']
    
      // authPages라는 배열에 to에 들어있는 url의 name이 포함되어 있는 지 확인
      const isAuthRequired = authPages.includes(to.name) 
    
      // 해당 페이지가 로그인이 필요한 페이지이고 로그인이 되어 있는 경우
      if (isAuthRequired && !isLoggedIN) {
        console.log('Login으로 이동!')
        next({ name: 'login'})
      } else {  //비로그인 사용자는 Hello로 못 들어감
        console.log('to로 이동!')
        next()
      }
    })
    ```
    
    ![dd.PNG](Navigation%20Guard%201175af759a96423b90aaf6d4bcb2a0d8/dd.png)
    
    ⇒ `const authPages= ['hello','about']` 대신 
    
    ⇒ `const allowAllPages = ['login','home']` 정의하고 조건을 바꿔주면 해당 페이지만 들어갈 수 있음
    

## (4) 라우터 가드

### 1. 정의

- 전체 route가 아닌 특정 route에 대해서만 가드를 설정하고 싶을 때 사용
- `beforeEnter()`
    - route에 진입했을 때 실행됨
    - 라우터를 등록한 위치에 추가
    - 단, (매개변수, 쿼리, 해시) 값이 변경될 때는 실행되지 않고 다른 경로에서 탐색할 때만 실행됨
    - 콜백 함수는 to, from, next를 인자로 받음

### 2. Login 여부에 따른 라우팅 처리

- 이미 로그인 되어있는 경우 HomeView로 이동하기
    
    (라우터 가드 실습을 위해 전역 가드 실습코드는 주석처리)
    
- 로그인 여부에 대한 임시 변수 생성
    
    ```jsx
    // index.js
    const isLoggedIn = true 
    
    const routes = [
      ...
      {
        path: '/login/',
        name: 'login',
        component: LoginVuew,
        //추가
        beforeEnter(to, from, next) {
          if (isLoggedIn === true) {
            console.log('이미 로그인 되어있음') //이미 로그인 된 사용자는
            next({ name: 'home' })            //home으로 바로 이동시키기
          } else {
            next()                            //아닌 사용자는 login으로
          }
        }
      },
    ]
    ```
    
    ![로그인.PNG](Navigation%20Guard%201175af759a96423b90aaf6d4bcb2a0d8/%25EB%25A1%259C%25EA%25B7%25B8%25EC%259D%25B8.png)
    
    +나중에는 로그인 상태에서 login 링크를 가려주자!!!
    

## (5)컴포넌트 가드

### 1. 정의

- 특정 컴포넌트 내에서 가드를 지정하고 싶을 때 사용
- `beforeRouteUpdate()`
    - 해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행

### 2. Params 변화 감지

- about에서 jun에게 인사하는 페이지로 이동
    
    => `http://localhost:8080/hello/jun` 로 이동
    
    ⇒ Hello bar를 click
    
    ⇒ 화면은 그대로 이고 `http://localhost:8080/hello/ssafy` 로 url만 변경
    
    ⇒ 화면도 바뀌도록 해주자!
    
- 변화 x 이유
    
    ⇒ 컴포넌트가 재사용되었기 때문
    
    ⇒ 기존 컴포넌트를 지우고 새로 만드는 것보다 효율적
    
    ⇒ 단, lifecycle hook이 호출되지 않음
    
    ⇒ `$route.params` 에 있는 데이터를 새로 가져오지 않음
    
- beforeRouteUpdate()를 사용해서 처리
    - userName을 이동할 params에 있는 userName으로 재할당
    
    ```jsx
    <script>
    export default {
     ...
      // 해당 컴포넌트를 렌더링하는 경로가 변경될때 실행
      beforeRouteUpdate(to, from, next) {
        this.userName = to.params.userName   
        next()
      }
    }
    </script>
    ```
    
    ⇒ `속도 측면에서 유리하게 만들기 위해 사용!`
    

## (6) 404 Not Found

### 1. 404 Not Found component 생성

- 사용자가 요청한 리소스가 존재하지 않을 때 응답
    
    ```jsx
    //NotFound404View.vue
    <template>
      <div>
        <h1>404 Not Found</h1>
      </div>
    </template>
    
    <script>
    export default {
      name: 'NotFound404View'
    }
    </script>
    ```
    
    ```jsx
    // index.js
    import NotFound404View from '@/views/NotFound404View'
    
    const routes = [
      ...
      {
        path: '/404',
        name: 'NotFound404View',
        component: NotFound404View,
      }
    ]
    ```
    

### 2. 요청한 리소스가 존재하지 않는 경우

- 모든 경로에 대해서 404page로 redirect 시키기
    - 기존에 명시한 경로가 아닌 모든 경로가 404 page로 redirect 됨
    - `이때, routes에 최하단부에 작성해야 함`
    
    ```jsx
    const routes = [
      ...
      {
        path: '*',
        redirect: '/404',
      }
    ]
    ```
    
    ⇒ 정의되어 있지 않은 url로 들어가면 404 페이지 출력
    

### 3 .형식은 유효하지만 특정 리소스를 찾을 수 없는 경우

ex) Django에서 `articles/1/` 로 요청을 보냈는데 `1번 게시글`이 이미 `지워진 경우`

⇒ path: ‘*’를 만나 404 page로 렌더링 되는 것이 아니라 기존에 명시한 `articles/:id/`에 대한 components가 렌더링됨

⇒ 하지만 존재 x 

⇒ 정상적인 렌더링 불가

- 해결책
    1. 데이터가 없음을 명시
    2. 404 page로 이동해야 함
- 실습
    1. Axios 설치  : `$ npm i axios` ←전역으로 설치 
    2. DogView 컴포넌트 작성
        
        ```jsx
        //views/DogView.vue
        
        <template>
          <div>
          </div>
        </template>
        
        <script>
        import axios from 'axios'
        
        export default {
          name: 'DogView',
        }
        </script>
        ```
        
    3. routes에 등록
        1. `‘*’` 보다 상단에 등록 
        
        ```jsx
        //index.js
        
        const routes = [
          ...
          {
            path: '/dog/:breed',  //품종
            name: 'dog',
            component: DogView,
          },
          {
            path: '*',
            redirect: '/404',
          }
        ]
        ```
        
    4. Dog api 문서를 참고하여 axios 로직을 작성
        
        ```jsx
        //DogView.vue
        <template>
          <div>
            <img :src="imgSrc" alt="">
          </div>
        </template>
        ```
        
        ```jsx
        <script>
        import axios from 'axios'
        
        export default {
          name: 'DogView',
          data() {
            return {
              imgSrc: null,
            }
          },
          methods: {
            getDogImage() {
              const breed = this.$route.params.breed
              const dogImageUrl = `https://dog.ceo/api/breed/${breed}/images/random`
              
              axios({
                method: 'get',
                url: dogImageUrl,
              })
                // axios 요청이 성공 했을 때,
                .then((response) => {
                  //이 console을 통해 img 주소를 찾는다.
                  console.log(response)
                  const imgSrc = response.data.message
                  this.imgSrc = imgSrc
                })
                .catch((error) => {
                  console.log(error)
                })
            }
          },
          // getDohImage 호출
          created() {
            this.getDogImage()
          }
        }
        </script>
        ```
        
        ![캡처.PNG](Navigation%20Guard%201175af759a96423b90aaf6d4bcb2a0d8/%25EC%25BA%25A1%25EC%25B2%2598.png)
        
        ⇒ response를 출력하여 imgSrc의 위치를 찾음
        
    5. axios 요청이 오는 중 동작하고 있음을 표현하기 위해 `로딩중` 띄워주기
        
        ```jsx
        //DogView.vue
        <template>
          <div>
        		// 이미지가 아직 안 나오면
            <p v-if="!imgSrc">{{ message }}</p>
            <img :src="imgSrc" alt="">
          </div>
        </template>
        ```
        
        ```jsx
        <script>
        export default {
          name: 'DogView',
          data() {
            return {
              imgSrc: null,
              message: '로딩중...',
            }
          },
          ...
        }
        </script>
        ```
        
    6. axios 요청이 실패할 경우 자료가 없음을 표시
        
        ```jsx
        <script>
        import axios from 'axios'
        
        export default {
          ...
          methods: {
            ...
              axios({
               ...
                .catch((error) => {
                  this.message = `${this.$route.params.breed}은 없는 품종입니다.`
                  console.log(error)
                })
            }
          },
          ...
        </script>
        ```
        
    7. axios가 없는 경우에도 404 page로 이동 시키자
        
        ```jsx
        .catch((error) => {
          // this.message = `${this.$route.params.breed}은 없는 품종입니다.`
          this.$router.push('/404')  // 404 페이지로 보내주기
          console.log(error)
        })
        ```