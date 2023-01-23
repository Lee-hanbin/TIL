# Articles with Vue

# Articles with Vue

## (1) 개요

- 지금까지 배운 내용들을 종합하여 Django에서 만들었던 게시판 만들기
- 구현
    
    `Index` , `Create`, `Detail` , `Delete` , `404` 
    
- 컴포넌트 구성
    
    ![캡처.PNG](Articles%20with%20Vue%20300b5d3dd6504736a0fa46553c4d204d/%25EC%25BA%25A1%25EC%25B2%2598.png)
    
- 완성 화면
    
    ![캡처.PNG](Articles%20with%20Vue%20300b5d3dd6504736a0fa46553c4d204d/%25EC%25BA%25A1%25EC%25B2%2598%201.png)
    

## (2) 사전 준비

- 프로젝트 시작
    - `$ vue create articles`
    - `$ cd articles`
    - `$ vue add vuex`
    - `$ vue add router`
- App.vue는 아래 코드만 남김(CSS 코드 유지)
    
    ```jsx
    //App.vue
    <template>
      <div id="app">
        <router-view/>
      </div>
    </template>
    ```
    
    ⇒ style은 납둬도 상관없음
    

## (3) Index

### 1. 개요

- articels의 목록을 보여주는 index 페이지

### 2. 구현

- state
    - 게시글의 필드는 id, 제목, 내용, 생성일자
    - DB의 AUTO INCREMENT를 표현하기 위해 article_id를 추가로 정의해줌
    
    ```jsx
    // store/index.js
    import Vue from 'vue'
    import Vuex from 'vuex'
    
    Vue.use(Vuex)
    
    export default new Vuex.Store({
      state: {
        article_id: 3,      // 다음에 작성될 3번의 글의 id
        articles: [
          {
            id: 1,
            title: 'title',
            content: 'content',
            createdAt: new Date().getTime(),
          },
          {
            id: 2,
            title: 'title2',
            content: 'content2',
            createdAt: new Date().getTime(),
          },
        ]
      },
    })
    ```
    
- IndexView
    - views의 component 모두 삭제
    - IndexView 생성
        
        ```jsx
        <template>
          <div>
            <h1>Index</h1>
          </div>
        </template>
        
        <script>
        export default {
          name: 'IndexView',
        }
        </script>
        ```
        
    - index.js (라우터에 등록)
        
        ```jsx
        import Vue from 'vue'
        import VueRouter from 'vue-router'
        import IndexView from '../views/HomeView.vue'
        
        Vue.use(VueRouter)
        
        const routes = [
          {
            path: '/',
            name: 'index',
            component: IndexView,
          },
        ]
        
        const router = new VueRouter({
          mode: 'history',
          base: process.env.BASE_URL,
          routes
        })
        
        export default router
        ```
        
        ⇒ 필요없는 것들 모두 삭제
        
- state에서 불러온 articles 출력하기
    
    ```jsx
    <template>
      <div>
        <h1>Articles</h1>
        {{ articles }}
      </div>
    </template>
    
    <script>
    export default {
      name: 'IndexView',
      computed: {
        articles () {
          return this.$store.state.articles
        }
      },
    }
    </script>
    ```
    
- ArticleItem 컴포넌트 작성
    - componets의 HelloWorld.vue 지우고 ArticleItem.vue 생성
        
        ```jsx
        <template>
          <div></div>
        </template>
        
        <script>
        export default {
          name: 'ArticleItem',
        }
        </script>
        ```
        
    - IndexView 컴포넌트에서 ArticleItem 컴포넌트 등록 및 props 데이터 전달
        
        ```jsx
        //views/IndexView.vue
        
        <template>
          <div>
            <h1>Articles</h1>
            <ArticleItem
              v-for="article in articles"
              :key=article.id
              :article=article
            />
          </div>
        </template>
        ```
        
        ⇒ ArticleItem에 데이터를 던져
        
        ```jsx
        <script>
        import ArticleItem from '@/components/ArticleItem'
        
        export default {
          name: 'IndexView',
          components: {
            ArticleItem,
          },
          computed: {
            articles () {
              return this.$store.state.articles
            }
          },
        }
        </script>
        ```
        
        ⇒ ArticleItem를 등록해서 함수로 정의
        
    - props 데이터 선언 및 게시글 출력
        
        ```jsx
        <template>
          <div>
              <p>글 번호 : {{ article.id }}</p>
              <p>글 제목 : {{ article.title }}</p>
              <hr>
          </div>
        </template>
        ```
        
        ```jsx
        <script>
        export default {
          name: 'ArticleItem',
          props: {
            article: Object,
          }
        }
        </script>
        ```
        
        ⇒ props로 IndexView로 부터 온 데이터를 받는다.
        
        ⇒ 받아서 출력
        
    

## (4) Create

### 1. 구현

- CreateView 컴포넌트 및 라우터 작성
    - views/CreateView
        
        ```jsx
        <template>
          <div>
            <h1>게시글 작성</h1>
          </div>
        </template>
        
        <script>
        export default {
          name: 'CreateView',
        }
        </script>
        ```
        
    - router/index.js 에 등록
        
        ```jsx
        //router/index.js 
        import CreateView from '../views/CreateView.vue'
        const routes = [
        	...
          {
            path: '/create',
            name: 'create',
            component: CreateView,
          }
        ]
        ```
        
- Form 생성 및 데이터 정의
    - CreateView.vue
        
        ```jsx
        //CreateView.vue
        
        <template>
          <div>
            <h1>게시글 작성</h1>
            <form>
              <input type="text" v-model="title"><br>
              <textarea v-model="content"></textarea>
              <input type="submit">
            </form>
          </div>
        </template>
        ```
        
        ```jsx
        ////CreateView.vue
        
        <script>
        export default {
          name: 'CreateView',
          data() {
            return {
              title: null,
              content: null,
            }
          }
        }
        </script>
        ```
        
- v-on:{event}.prevent를 활용하여 submit 이벤트 동작을 취소하기
+actions에 여러 개의 데이터를 넘길 때 하나의 object로 만들어서 전달
    
    ```jsx
    <template>
      <div>
        <h1>게시글 작성</h1>
        <form @submit.prevent="createArticle">
          <input type="text" v-model.trim="title"><br>
          <textarea v-model.trim="content"></textarea>
          <input type="submit">
        </form>
      </div>
    </template>
    ```
    
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
      methods:{
        createArticle() {
          const title = this.title
          const content = this.content
          const payload = {
            title, content
          }
          this.$store.dispatch('createArticle', payload)
        }
      }
    }
    </script>
    ```
    
- 데이터가 없는 경우 alert & 데이터가 있는 경우 actions로 전달
    
    pass
    
- actions에서는 넘어온 데이터를 활용하여 article 생성 후 mutations 호출
    - 이때 id로 article_id 활용
        
        ```jsx
        actions: {
          createArticle(context, payload){    // 이거 첫 글자 소문자ㅠ
            const article = {
              id: context.state.article_id,
              title: payload.title,
              content: payload.content,
              createdAt: new Date().getTime(),
            }
            context.commit('CREATE_ARTICLE', article)
          }
        },
        ```
        
- mutations에서는 전달된 article 객체를 사용해 게시글 작성
    - 다음 게시글을 위해 article_id 값 1 증가
    
    ```jsx
    mutations: {
      CREATE_ARTICLE(state, article) {
        state.articles.push(article)
        state.article_id = state.article_id + 1 //위에 적었던 3번째 글 이후에 +1씩
      }
    },
    ```
    
- indexView 컴포넌트에 게시글 작성 페이지로 이동하는 링크 추가
    
    ```jsx
    <template>
      <div>
        <h1>Articles</h1>
        <router-link :to="{ name: 'create' }">게시글 작성</router-link>
        ...
      </div>
    </template>
    ```
    
- CreateView 컴포넌트에 Index 페이지로 이동하는 뒤로가기 링크 추가
    
    ```jsx
    <template>
      <div>
        ...
        <router-link :to="{ name: 'index' }">뒤로가기</router-link>
      </div>
    </template>
    ```
    
- 게시글 생성 후 index 페이지로 이동하도록 네비게이터 작성
    
    ```jsx
    //CreateView.vue
    
    <script>
    export default {
      ...
      methods:{
        createArticle() {
          ...
          }
          this.$store.dispatch('createArticle', payload)
          this.$router.push({ name: 'index' })    // 글 작성 후, 작성된 페이지로 가기
        }
      }
    }
    </script>
    ```
    

## (5) Detail

### 1. 구현

- DetailView 컴포넌트 및 라우터 작성
    - id를 동적인자로 전달
    
    ```jsx
    //DetailView.vue
    
    <template>
      <div>
        <h1>Detail</h1>
      </div>
    </template>
    
    <script>
    export default {
      name: 'DetailView'
    }
    </script>
    ```
    
    ```jsx
    //router/index.js
    import DetailView from '../views/DetailView.vue'
    
    const routes = [
      ...
      {
        path: '/:id',     // 변수가 동적!
        name: 'detail',
        component: DetailView,
      }
    ]
    ```
    
- article 정의 및 state에서 articles 가져오기
    
    ```jsx
    //DetailView.vue
    
    <script>
    export default {
      name: 'DetailView',
      data() {
        return {
          article: null     // 찾은 값을 여기에 저장해야함
        }
      },
      computed: {
        articles() {
          return this.$store.state.articles
        }
      },
    }
    </script>
    ```
    
- articles에서 동적인자를 통해 받은 id에 해당하는 article 가져오기
    
    ⇒ 동적 인자를 통해 받은 id는 str이므로 형변환을 해서 비교
    
    ```jsx
    //DetailView.vue
    
    <script>
    export default {
      name: 'DetailView',
      data() {
        return {
          article: null     // 찾은 값을 여기에 저장해야함
        }
      },
      computed: {
        ...
      },
      methods: {
        getArticleById() {
          //이 id 값으로 배열에서 값 찾기 (이 값은 url로 들어오므로 문자임!)
          const id = this.$route.params.id          // url로 들어온 id를 가지고
          for (const article of this.articles) {    // 배열을 순회하여
            if (article.id === Number(id)) {        // article의 id와 url로 들어온 int(id)가 같으면
              this.article = article                // 해당 article을 data의 article 변수에 할당
              break
            }
          }
        }
      }
    }
    </script>
    
    <style>
    
    </style>
    ```
    
- article 출력
    
    ```jsx
    //DetailView.vue
    
    <template>
      <div>
        <h1>Detail</h1>
        <p>글 번호: {{ article.id }}</p>
        <p>글 제목: {{ article.title }}</p>
        <p>글 내용: {{ article.content }}</p>
        <p>글 작성시간: {{ article.createAt }}</p>
      </div>
    </template>
    ```
    
- created lifecycle hook을 통해 인스턴스가 생성되었을 때 article을 가져오는 함수 호출
    
    방법 1.
    
    ```jsx
    //DetailView.vue
    
    <script>
    export default {
     ...
      methods: {
        getArticleById() {
          //이 id 값으로 배열에서 값 찾기 (이 값은 url로 들어오므로 문자임!)
          const id = this.$route.params.id          // url로 들어온 id를 가지고
          for (const article of this.articles) {    // 배열을 순회하여
            if (article.id === Number(id)) {        // article의 id와 url로 들어온 int(id)가 같으면
              this.article = article                // 해당 article을 data의 article 변수에
              break
            }
          }
        }
      },
      created() {
        this.getArticleById()
      }
    }
    </script>
    ```
    
    방법 2.
    
    ```jsx
    //DetailView.vue
    
    <script>
    export default {
      ...
      methods: {
        getArticleById(id) {
          //이 id 값으로 배열에서 값 찾기 (이 값은 url로 들어오므로 문자임!)
          // const id = this.$route.params.id          // url로 들어온 id를 가지고
          for (const article of this.articles) {    // 배열을 순회하여
            if (article.id === Number(id)) {        // article의 id와 url로 들어온 int(id)가 같으면
              this.article = article                // 해당 article을 data의 article 변수에
              break
            }
          }
        }
      },
      created() {
        this.getArticleById(this.$route.params.id)
      }
    }
    </script>
    ```
    
    ⇒ id를 함수 인자로 받음
    
- DetailView 컴포넌트에 뒤로가기 링크 추가
    
    ```jsx
    //DetailView.vue
    
    <template>
      <div>
        ...
        <router-link :to="{ name: 'index' }">뒤로가기</router-link>
      </div>
    </template>
    ```
    
- 각 게시글을 클릭하면 detail 페이지로 이동하도록 ArticleItem에 이벤트 추가
    - v-on 이벤트 핸들러에도 인자 전달 가능
    
    ```jsx
    template>
      <div @click="goDetail(article.id)">
      //<div @click="goDetail()">
          ...
      </div>
    </template>
    ```
    
    ```jsx
    <script>
    export default {
      ...
      methods: {
        goDetail(id) {
          this.$router.push({ name: 'detail', params: {id} })
        // goDetail() {
    			// this.$router.push({ name: 'detail', params: {id: `${this.article.id}`} }) 
    			// 이건 props에서 가져옴
        }
      }
    }
    </script>
    ```
    

### 2. 데이터를 서버에서 가져온 경우!

- 우리는 현재 state를 통해 데이터를 동기적으로 가져오지만, 실제로는 서버로부터 가져옴
    
    ⇒ 데이터를 가져오는데 시간이 걸림
    
- created를 주석처리하면 article에 null 값이 들어 있으므로 error 발생
    
    ⇒ `optinal chaining` (`?.`)을 통해 article 객체가 있을 때만 출력되도록 수정
    
- created 주석처리
    
    ![1.PNG](Articles%20with%20Vue%20300b5d3dd6504736a0fa46553c4d204d/1.png)
    
- `?.` 사용
    
    ```jsx
    <template>
      <div>
        <h1>Detail</h1>
        <p>글 번호: {{ article?.id }}</p>
        <p>글 제목: {{ article?.title }}</p>
        <p>글 내용: {{ article?.content }}</p>
        <p>글 작성시간: {{ article?.createdAt }}</p>
      </div>
    </template>
    ```
    
    ![2.PNG](Articles%20with%20Vue%20300b5d3dd6504736a0fa46553c4d204d/2.png)
    
- created 주석제거
    
    ![Untitled](Articles%20with%20Vue%20300b5d3dd6504736a0fa46553c4d204d/Untitled.png)
    

### 3. Date in JavaScript

- JavaScript에서 시간을 나타내는 Date객체는 1970년 1월 1일 UTC(협정 세계시)자정과의 시간 차이를 밀리초로 나타내는 정수 값을 담음
    - `Date().toLocaleString()`
    
    ```html
    <template>
      <div>
        <h1>Detail</h1>
    		...
        <!-- <p>글 작성시간: {{ article?.createdAt }}</p> -->
        <p>작성시간: {{ articleCreatedAt }}</p>
      </div>
    </template>
    ```
    
    ```jsx
    <script>
    export default {
      ...
      computed: {
        ...
        articleCreatedAt() {
          const article = this.article
          const createdAt = new Date(article?.createdAt).toLocaleString()
          return createdAt
        },
      },
      methods: {
        ...
      },
      created() {
        this.getArticleById(this.$route.params.id)
      }
    }
    </script>
    ```
    

## (6) Delete

### 1. 삭제

- DetailView 컴포넌트에 삭제 버튼을 만들고, mutations를 호출
    
    ```jsx
    // DetailView.vue
    
    <template>
      <div>
        ...
        <button @click="deleteArticle">삭제</button><br>
        <router-link :to="{ name: 'index' }">뒤로가기</router-link>
      </div>
    </template>
    ```
    
    ```jsx
    <script>
    export default {
      ...
      methods: {
        getArticleById(id) {
          ...
        },
        //actions에서 할게 없으니까 바로 mutations로 보내자
        deleteArticle() {
          this.$store.commit('DELETE_ARTICLE', this.article.id)
        }
      },
      created() {
        this.getArticleById(this.$route.params.id)
      }
    }
    </script>
    ```
    
- mutations에서 id에 해당하는 게시글을 지움
    
    ```jsx
    //store/index.js
    
    mutations: {
        CREATE_ARTICLE(state, article) {
          ...
        },
        DELETE_ARTICLE(state, article_id) {
          // filter를 통해 articles라는 배열에서 
          // article.id === article_id 이면 false를 만들고 해당 값을 빼고 배열 다시 만들기
          state.articles = state.articles.filter((article) =>{
            return !(article.id === article_id)
          })
        }
      },
    ```
    
- 삭제 후 index 페이지로 이동하도록 네비게이션 작성
    
    ```jsx
    <script>
    export default {
      ...
      methods: {
        getArticleById(id) {
          ...
        },
        deleteArticle() {
          this.$store.commit('DELETE_ARTICLE', this.article.id)
          this.$router.push({ name: 'index' })  // 삭제하면 index 페이지로
        }
      },
      created() {
        this.getArticleById(this.$route.params.id)
      }
    }
    </script>
    ```
    

## (7) 404 페이지 구현

- NotFound404 컴포넌트 및 라우터 작성
- Detail에 대한 route보다 먼저 등록해줘야 함
    
    ⇒ `/404` 로 등록하면 404번째 게시글과 혼동될 수 있음
    
    ```jsx
    //NotFound404.vue
    
    <template>
      <div>
        <h1>404 Not Found</h1>
      </div>
    </template>
    
    <script>
    export default {
      name: 'NotFound404',
    } 
    </script>
    
    ```
    
    ```jsx
    //router/index.js
    
    const routes = [
      ...
      {
        path: '404-not-found',  // 이것을 detail보다 아래 두면 404에 걸림
        name: 'NotFound404',    // 따라서 detail보다 위에 두거나 path명을 바꿔
        component: NotFound404
      },
      {
        path: '/:id',     // 변수가 동적!
        name: 'detail',
        component: DetailView,
      },
    ]
    ```
    
- DetailView 컴포넌트에 id에 해당하는 article이 없으면 404 페이지로 이동
    
    ```jsx
    //DetailView.vue
    
    <script>
    export default {
      ...
      methods: {
        getArticleById(id) {
          ...
          }
          if (this.article === null) {
            this.$router.push({ name: 'NotFound404'})
          }
        },
        //actions에서 할게 없으니까 바로 mutations로 보내자
        deleteArticle() {
        ...
        }
      },
      created() {
        this.getArticleById(this.$route.params.id)
      }
    }
    </script>
    ```
    
- 요청한 리소스가 존재하지 않는 경우 없는 id가 아닌 전혀 다른 요청에도 대비하여 404 page로 redirect 시키기
    - `$router.push` 와 마찬가지로 name을 이용하여 이동할 수 있음
        
        ```jsx
        const routes = [
          ...
          ...
          {
            path: '*',
            redirect: { name: 'NotFound404'}
          }
        ]
        ```