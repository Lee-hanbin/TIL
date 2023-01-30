# Vue with DRF (3) - Vue로 인증

# DRF Auth with Vue

## (1) SignUp Request

### 1. `views/SignUpView.vue` 코드 확인

- Server에서 정의한 field명 확인
    1. username
    2. password1
    3. password2
- `SignUpView.vue`
    
    ```jsx
    <template>
      <div>
        <h1>Sign Up Page</h1>
        <form>
          <label for="username">username : </label>
          <input type="text" id="username" v-model="username"><br>
    
          <label for="password1"> password : </label>
          <input type="password" id="password1" v-model="password1"><br>
    
          <label for="password2"> password confirmation : </label>
          <input type="password" id="password2" v-model="password2">
          
          <input type="submit" value="SignUp">
        </form>
      </div>
    </template>
    
    <script>
    export default {
      name: 'SignUpView',
      data() {
        return {
          username: null,
          password1: null,
          password2: null,
        }
      },
      methods: {
      }
    }
    </script>
    ```
    
    ⇒ 데이터에 변수 정의해서 v-model로 받기
    
- routes/index.js에서 path 설정
- App.vue에서 router-link 생성

### 2. SignUp Request

- 회원가입을 완료 시 응답 받을 정보 Token을 store에서 관리할 수 있도록 actions를 활용하여 요청 후, state에 저장할 로직 작성
    - 회원가입이나 로그인 후 얻을 수 있는 Token은 server를 구성 방식에 따라 매 요청마다 요구 할 수 있으므로, 다양한 컴포넌트에서 쉽게 접근 할 수 있도록 중앙 상태 저장소인 vuex에서 관리
- 사용자 입력 값을 하나의 객체 payload에 담아 전달
    - `Views/SignUpView.vue`
        
        ```jsx
        <template>
          <div>
            <h1>Sign Up Page</h1>
            <form @submit.prevent="signUp">
        			...
            </form>
          </div>
        </template>
        
        <script>
        export default {
          name: 'SignUpView',
          data() {
            return {
              ...
            }
          },
          methods: {
            signUp() {
              const username = this.username
              const password1 = this.password1
              const password2 = this.password2
        
              const payload = {
                username: username,
                password1: password1,
                password2: password2,
              }
        
              this.$store.dispatch('signUp', payload)
            }
          }
        }
        </script>
        ```
        
- payload가 가진 값을 각각 할당
    - AJAX 요청으로 응답 받은 데이터는 다수의 컴포넌트에서 사용해야 함
    - `index.js`
        
        ```jsx
        import Vue from 'vue'
        import Vuex from 'vuex'
        import axios from 'axios'
        
        Vue.use(Vuex)
        
        const API_URL = 'http://127.0.0.1:8000'     // Django server URL 작성
        
        export default new Vuex.Store({
        	state: {
            articles: [],
            token: null,
          },
          getters: {
          },
          mutations: {
            ...
            SIGN_UP(state, token) {
              state.token = token
            }
          },
          actions: {
            getArticles(context) {
              ...
            },
            signUp(context, payload) {
              // const username = payload.username
              // const password1 = payload.password1
              // const password2 = payload.password2
            axios({
              method: 'post',
              url: `${API_URL}/accounts/signup/`,
              data: {
                username: payload.username,
                password1:  payload.password1,
                password2:  payload.password2,
              }
            })
              .then((res) => {
        				context.commit('SIGN_UP', res.data.key)
              })
            } 
          },
          modules: {
          }
        })
        ```
        
- Vuex에서 token 확인 가능
    
    ![Untitled](Vue%20with%20DRF%20(3)%20-%20Vue%E1%84%85%E1%85%A9%20%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%B3%E1%86%BC%20ac58cf286e9f40368537c208a8f1486f/Untitled.png)
    

### 3. 토큰 관리

- 게시물 전체 조회와 달리, 인증 요청의 응답으로 받은 Token은 매번 요청하기 힘듦
    - 비밀번호를 항상 보관하고 있을 수 없음
    - localStorage에 token 저장을 위해 `vuex-persistedstate` 활용
- 설치
    
    `$ npm install vuex-persistendstate`
    
    - `store/index.js`
        
        ```jsx
        import createPersistedStore from 'vuex-persistedstate'
        export default new Vuex.Store({
          plugins: [
            createPersistedStore(),
          ],
        	...
        })
        ```
        
    
    ![Untitled](Vue%20with%20DRF%20(3)%20-%20Vue%E1%84%85%E1%85%A9%20%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%B3%E1%86%BC%20ac58cf286e9f40368537c208a8f1486f/Untitled%201.png)
    

### 4. User 인증 정보를 localStorage에 저장해도 되는가?

- 안전한 방법 x
- vuex-perisistedstate는 아래의 2가지 방법을 제공
    1. 쿠키를 사용
    2. 로컬 저장소를 난독화 하여 관리
- 실습 편의를 위해 localStorage를 사용

## (2) Login Request

### 1. Login Page

- `views/LoginView.vue`
    - 회원가입 로직과 동일
    - Server에서 정의한 field명 확인
        1. username
        2. password
    - `LoginView.vue`
        
        ```jsx
        <template>
          <div>
            <h1>LogIn Page</h1>
            <form>
              <label for="username">username : </label>
              <input type="text" id="username" v-model="username"><br>
        
              <label for="password"> password : </label>
              <input type="password" id="password" v-model="password"><br>
        
              <input type="submit" value="logIn">
            </form>
          </div>
        </template>
        
        <script>
        export default {
          name: 'LogInView',
          data() {
            return {
              username: null,
              password: null,
            }
          },
          methods: {
          }
        }
        </script>
        ```
        
        ⇒ username과 password를 v-model로 양방향 바인드
        
- router/index.js에서 경로 설정

### 2. Login Request

- signUp과 다른 점은 password1,2 가 password로 바뀜
- 요청을 보내고 응답을 받은 Token을 state에 저장하는 것 까지도 동일
    - mutations가 처리 해야 하는 업무가 동일
    - SIGN_UP mutations를 `SAVE_TOKEN mutations` 로 대체 가능
- `Views/LogInView.vue`
    - 사용자 입력 값을 하나의 객체 payload에 담아 전달
    - `LogInView.vue`
        
        ```jsx
        <template>
          <div>
            <h1>LogIn Page</h1>
            <form @submit.prevent="logIn">
              ...
            </form>
          </div>
        </template>
        
        <script>
        export default {
          name: 'LogInView',
          data() {
            return {
              username: null,
              password: null,
            }
          },
          methods: {
            logIn() {
              const username = this.username
              const password = this.password
        
              const payload = {
                username: username,
                password: password,
              }
              this.$store.dispatch('logIn', payload)
            }
          }
        }
        </script>
        ```
        
- payload가 가진 값을 각각 할당
    - AJAX 요청으로 응답 받은 데이터는 다수의 컴포넌트에서 사용
    - `store/index.js`
        
        ```jsx
        import Vue from 'vue'
        import Vuex from 'vuex'
        import axios from 'axios'
        import createPersistedStore from 'vuex-persistedstate'
        Vue.use(Vuex)
        
        const API_URL = 'http://127.0.0.1:8000'     // Django server URL 작성
        
        export default new Vuex.Store({
          ...
          mutations: {
            GET_ARTICLES(state, articles) {
              state.articles = articles
            },
            // SIGN_UP(state, token) {
            //   state.token = token
            // },
            SAVE_TOKEN(state, token) {
              state.token = token
            },
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
            },
        		signUp(context, payload) {
              // const username = payload.username
              // const password1 = payload.password1
              // const password2 = payload.password2
              axios({
                method: 'post',
                url: `${API_URL}/accounts/signup/`,
                data: {
                  username: payload.username,
                  password1:  payload.password1,
                  password2:  payload.password2,
                }
              })
                .then((res) => {
                  // context.commit('SIGN_UP', res.data.key)
                  context.commit('SAVE_TOKEN', res.data.key)  <---SAVE_TOKEN으로 변경
                })
            },
            logIn(context, payload) {
              axios({
                method: 'post',
                url: `${API_URL}/accounts/login/`,
                data: {
                  username: payload.username,
                  password: payload.password
                }
              })
                .then((res) => {
                  console.log(res)
                  context.commit('SAVE_TOKEN', res.data.key)
                })
                .catch((err) => {
                  console.log(err)
                })
            } 
          },
          modules: {
          }
        })
        ```
        
    

## (3) IsAuthenticated in Vue

- 회원가입, 로그인 요청에 대한 처리 후 , state에 저장된 Token을 직접 확인하기 전까지 인증 여부 확인 불가
- 인증 되지 않았을 시 게시글 정보를 확인할 수 없으나 이유를 알 수 없음
    - 로그인 여부를 확인 할 수 있는 수단이 없음
- 로그인 여부 판별 코드 확인 ⇒ Token이 있으면 true 업으면 false
    - `store/index.js`
        
        ```jsx
        ...
        export default new Vuex.Store({
          ...
          getters: {
            isLogin(state) {
              return state.token ? true : false
            }
          },
          mutations: {
            GET_ARTICLES(state, articles) {
              state.articles = articles
            },
            // SIGN_UP(state, token) {
            //   state.token = token
            // },
            // 회원가입과 로그인을 할 때, token을 저장하고 ArticleView에 보내주기
            SAVE_TOKEN(state, token) {
              state.token = token
              router.push({name: 'ArticleView'})
            },
          },
          actions: {
            ...
        })
        ```
        
- isLogin 정보를  토대로 게시글 정보를 요청 할 것인지, LogInView로 이동시킬 것인지 결정
    - `views/ArticlesView.vue`
        
        ```jsx
        <script>
        import ArticleList from '@/components/ArticleList'
        
        export default {
          name: 'ArticleView',
          components: {
            ArticleList
          },
          computed:{
            isLogin() {
              return this.$store.getters.isLogin
            }
          },
          created() {
            this.getArticles()
          },
          methods: {
            getArticles() {
              if (this.isLogin === true) {
                this.$store.dispatch('getArticles')
              } else {
                alert('로그인이 필요한 서비스 입니다.')
                this.$router.push({ name: 'LogInView'})
              }
            }
          }
        }
        </script>
        
        ```
        
- 로그인을 하여 ArticleView로 넘어가도 401에러 발생
    
    ⇒ ArticleView로 넘어갈 때도 토큰 필요!
    

## (4)Request with Token

- 인증 여부를 확인하기 위한 Token이 준비되었으니, headers HTTP에 Token을 담아 요청을 보냄

### 1. Arcitle List Read with Token

- `store/index.js`
    
    ```jsx
    ...
    export default new Vuex.Store({
      ...
      state: {
        articles: [],
        token: null,
      },
      ...
      mutations: {
        ...
      },
      actions: {
        getArticles(context) {
          axios({
            method: 'get',
            url: `${API_URL}/api/v1/articles/`,
            headers: {
              Authorization: `Token ${context.state.token}`   <-- 토큰 보내주기
            }
          })
            .then((response) => {
              // console.log(response, context)
              // console.log(response.data)
              context.commit('GET_ARTICLES', response.data)
            })
            .catch((error) => {
              console.log(error)
            })
        },
        ...
      modules: {
      }
    })
    ```
    

### 2. Article Create with Token

- `views/CreateView.vue`
    
    ```jsx
    
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
          ...
          axios({
            method: 'post',
            url: `${API_URL}/api/v1/articles/`,
            data: {
              title: title,
              content: content
            },
            headers: {
              Authorization: `Token ${this.$store.state.token}` <-- 토큰 추가
            }
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
    
    <style>
    
    </style>
    ```
    

### 3. Create Article with User

- `articles/models.py` 에서 User 정의
    - User정보를 Vue에서도 확인 가능하도록 정보 제공
    - `articles/models.py`
        
        ```jsx
        class Article(models.Model):
            user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
            title = models.CharField(max_length=100)
            content = models.TextField()
            created_at = models.DateTimeField(auto_now_add=True)
            updated_at = models.DateTimeField(auto_now=True)
        ```
        
- makemigrations & migrate
- `articles/serializers.py` 에서 유저관련 내용 작성
- `articles/views` 에서 유저 관련 내용 작성
- `components/ArticleListItem.vue` 에서 user 정보 표현
    - `ArticleListItem.vue`
        
        ```jsx
        <template>
          <div>
            ...
            <p>작성자 : {{ article.username }}</p>
            ...
          </div>
        </template>
        ```