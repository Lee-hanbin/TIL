# Vue Router

# Vue Router

## (1) 정의

- Vue의 공식 라우터
- SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공
- 라우트(routes)에 컴포넌트를 매핑한 후, 어떤 URL에서 렌더링 할지 알려줌
    - 즉, SPA를 MPA처럼 URL을 이동하면서 사용 가능
    - SPA의 단점 중 하나인 `URL이 변경되지 않는다` 를 해결

## (2) Vue Router 시작

### 1. Vuex와 마찬가지의 방식으로 설치 및 반영

- Vue 프로젝트 생성 : `$ vue create vue-router-app`
- 디렉토리 이동 : `$ cd vue-router-app`
- Vue CLI를 통해 router plugin 적용 : `$ vue add router`
- `? Use history mode for router? (Requires proper server setup for index fallback in production)` ⇒ `yes`
    
    ⇒ 브라우저의 History API를 활용한 방식
    
    ⇒ 새로고침 없이 URL 이동 기록을 남길 수 있음
    
    ⇒ 우리에게 익숙한 URL 구조로 사용 가능
    
- App.vue 달라짐

![app.PNG](Vue%20Router%201791d00c73984b3d8d295cb1a8528b0a/app.png)

- router 와 views 생성
    
    ![folder.PNG](Vue%20Router%201791d00c73984b3d8d295cb1a8528b0a/folder.png)
    

### 2. `router-link`

- `a 태그`와 비슷한 기능→ `URL을 이동`시킴
    - routes에 등록된 컴포넌트와 매핑
    - 히스토리 모드에서 router-link는 `클릭 이벤트를 차단`하여 a 태그와 달리 브라우저가 `페이지를 다시 로드 하지 않도록 함`
- 목표 경로는 `'to'` 속성으로 지정됨
- 기능에 맞게 HTML에서 a 태그로 rendering 되지만, 필요에 따라 다른 태그로 바꿀 수 있음

### 3. `router-view`

- 주어진 `URL`에 대해 `일치`하는 `컴포넌트`를 렌더링 컴포넌트
- 실제 component가 DOM에 부착되어 보이는 자리를 의미
- router-link를 클릭하면 routes에 매핑된 컴포넌트를 렌더링
- Django에서의 block tag와 비슷함
    - App.vue는 base.html 역할
    - router-view는 block-view는 block 태그로 감싼 부분

### 4. `src/router/index.js`

- 라우터에 관련된 정보 및 설정이 작성 되는 곳
- `Django`에서의 `urls.py`에 해당
- routes에 URL와 컴포넌트를 매핑

### 5. `src/views`

- router-view에 들어갈 component 작성
- 기존에 컴포넌트를 작성하던 곳은 components 폴더 뿐이었지만 이제 두 폴더로 나뉘어짐
- 각 폴더 안의 .vue 파일들이 기능적으로 다른 것은 아님
- views
    - `routes에 매핑`되는 컴포넌트
        
        ⇒ <router-view>의 위치에 렌더링 되는 컴포넌트를 모아두는 폴더
        
    - 다른 컴포넌트와 구분하기 위해 View로 끝나도록 만드는 것을 권장
- components
    - routes에 매핑된 컴포넌트의 하위 컴포넌트를 모아두는 폴더

## (3) 실습

### 1. 주소를 이동하는 2가지 방법(`선언 방식`)

- router-link의 `'to'` 속성으로 주소 전달
    - routes에 등록된 주소와 매핑된 컴포넌트로 이동
- 동적인 값을 사용하기 때문에 v-bind 사용
    
    ```jsx
    //App.vue
    <template>
      <div id="app">
        <nav>
    //      <router-link to="/">Home</router-link> |
    //      <router-link to="/about">About</router-link>
    				<router-link :to="{ name: 'home' }">Home</router-link> |
    	      <router-link :to="{ name: 'about' }">About</router-link>
        </nav>
        <router-view/>
      </div>
    </template>
    ```
    

### 2. 주소를 이동하는 2가지 방법(`프로그래밍 방식`)

- Vue 인스턴스 내부에서 라우터 인스턴스에 `$router` 로 접근 할 수 있음
- 다른 URL로 이동하려면 `this.$router.push` 를 사용
    - history stack에 이동할 URL을 넣는 방식
    - history stack에 `기록이 남기 때문에` 사용자가 브라우저의 `뒤로 가기 버튼`을 클릭하면 이전 URL로 이동가능
- 결국 `<router-link :to="...">` 를 클릭하는 것과 `$router.push(...)` 를 호출하는 것은 같은 동작
    
    ![캡처.PNG](Vue%20Router%201791d00c73984b3d8d295cb1a8528b0a/%25EC%25BA%25A1%25EC%25B2%2598.png)
    
    ⇒ 선언식과 프로그래밍식의 기능은 동일
    

### 3. Dynamic Route Matching

- 정의
    - 동적 인자 전달
        - URL의 특정 값을 변수처럼 사용할 수 있음
    - Django에서의 variable routing
- HelloView.vue 작성 및 route 추가
    - route를 추가할 때 동적 인자를 명시
    
    ```jsx
    // router/index.js
    import HelloView from '@/views/HelloView'
    
    const routes = [
      ...
      {
        path: '/hello/:userName',
        name: 'hello',
        component: HelloView,
      }
    ]
    ```
    
    ```jsx
    //views/HelloView.vue
    <template>
      <div></div>
    </template>
    
    <script>
    export default {
      name: 'HelloView',
    }
    </script>
    
    <style>
    
    </style>
    ```
    
- `$route.params` 로 변수에 접근 가능
    
    ```jsx
    // HelloView.vue
    <template>
      <div>
        <h1>hello, {{ $route.params.userName }}</h1>
      </div>
    </template>
    
    <script>
    export default {
      name: 'HelloView',
    }
    </script>
    
    <style>
    
    </style>
    ```
    
- 위의 방법처럼 HTML에서 직접 사용하기 보다는 data에 넣어서 사용하는 것을 권장
    
    ```jsx
    <template>
      <div>
        <!-- <h1>hello, {{ $route.params.userName }}</h1> -->
        <h1>hello, {{ userName }}</h1>
      </div>
    </template>
    
    <script>
    export default {
      name: 'HelloView',
      data() {
        return {
          userName: this.$route.params.userName
        }
      }
    }
    </script>
    
    <style>
    
    </style>
    ```
    

### 4. Dynamic Route Matching - `선언적 방식 네비게이션`

- App.vue에서 harry에게 인사하는 페이지로 이동해보기
- params를 이용하여 동적 인자 전달 가능
    
    ```jsx
    //App.vue
    
    <template>
      <div id="app">
        <nav>
          <router-link :to="{ name: 'home' }">Home</router-link> |
          <router-link :to="{ name: 'about' }">About</router-link> |
          <router-link :to="{ name: 'hello', params: { userName: 'ssafy'} }">Hello</router-link>
        </nav>
        <router-view/>
      </div>
    </template>
    ```
    

### 5. Dynamic Route Matcing - `프로그래밍 방식 네비게이션`

- AboutView에서 데이터를 입력 받아 HelloView로 이동하여 입력받은 데이터에게 인사하기
    
    ```html
    //AboutView.vue
    
    <template>
      <div class="about">
        ...
        <input 
          type="text"
          v-model="inputData"
          @keyup.enter='goToHello'
        >
      </div>
    </template>
    ```
    
    ```jsx
    <script>
    export default {
      name: 'AboutView',
      data() {
        return {
          inputData: null,
        }
      },
      methods: {
       ...
        goToHello() {
          this.$router.push({ name: 'hello', params: { userName: this.inputData } })
        }
      }
    }
    </script>
    ```
    

### 6. route에 컴포넌트를 등록하는 또 다른 방법

- router/index.js에 컴포넌트를 등록하는 또 다른 방식이 주어지고 있음(about)
    - 기존방식
        
        ```jsx
        {
            path: '/',
            name: 'home',
            component: HomeView
          },
        ```
        
        ⇒ 처음에 다 로딩하는 방식이므로 초기에 시간이 오래 걸린
        
    - Lazy-loading
        
        ```jsx
        {
          path: '/about',
          name: 'about',
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
         },
        ```
        
        ⇒ about으로 이동하지 않는 이상 로딩하지 않음
        
        ⇒ lazy-loading 방식 (첫 로딩에 랜더링 하지않고 해당 라우터가 동작할 때 컴포넌트를 렌더링 한다.)
        
        ⇒ `속도 측면에서 유리`
        
    - `lazy-loading`
        - 모든 파일을 한 번에 로드하려고 하면 모든 걸 다 읽는 시간이 매우 오래 걸림
        - 미리 로드를 하지 않고 특정 라우트에 방문할 때 매핑된 컴포넌트의 코드를 로드하는 방식을 활용할 수 있음
            - 모든 파일을 한 번에 로드하지 않아도 되기 때문에 최초에 로드하는 시간이 빨라짐
            - 당장 사용하지 않을 컴포넌트는 먼저 로드하지 않는 것이 핵심