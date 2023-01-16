# Todo with Vuex

# Todo with Vuex

## (1) 개요

- Vuex를 사용한 Todo 프로젝트 만들기
- 구현 기능
    - Todo CRUD
    - Todo 개수 계산
        - 전체 Todo
        - 완료된 Todo
        - 미완료된 Todo
- 컴포넌트 구성
    
    ![구조.PNG](Todo%20with%20Vuex%20cef350d7d456466c8ae0114c31862dbc/%25EA%25B5%25AC%25EC%25A1%25B0.png)
    
- 완성 화면
    
    ![완성.PNG](Todo%20with%20Vuex%20cef350d7d456466c8ae0114c31862dbc/%25EC%2599%2584%25EC%2584%25B1.png)
    

## (2) 컴포넌트 작성

- `TodoListItem` ⇒ `TodoList` ⇒ `App` 순으로 등록
- `TodoForm` ⇒ `App` 순으로 등록
    
    ```jsx
    1. vue + tap
    2. 최상위 스코프 생성 (div)
    3. 이름등록
    ----------------------------------------------------------------------
    4. 상속 : 자식 불러오기 => component 등록하기 => <component명/> 출력하기
    ```
    

## (3) Read Todo

### 1. state 세팅

- 출력을 위한 기본 todo 작성
    
    ```jsx
    //index.js
    
    export default new Vuex.Store({
      state: {
        todos: [
          {
            title: '할 일 1',
            isCompleted: false,
          },
          {
            title: '할 일 2',
            isCompleted: false,
          }
        ]
      },
      getters: {
      },
      mutations: {
      },
      actions: {
      },
      modules: {
      }
    })
    ```
    

### 2. state 데이터 가져오기 & Pass Props

- 컴포넌트에서 Vuex Store의 state에 접근($store.state)
- computed로 계산된 todo 목록을 가져올 수 있도록 설정
    
    ```jsx
    // Todo
    <template>
      <div>
        <TodoListItem
    		v-for="(todo, index) in todos"
    		:key="index"
    		:todo="todo"    //
    		/>
        <!-- {{ todos }} -->
      </div>
    </template>
    
    <script>
    import TodoListItem from '@/components/TodoListItem'
    
    export default {
      name: 'TodoList',
      components: {
        TodoListItem,
      },
      computed: {
        todos() {
          return this.$store.state.todos
        }
      }
    }
    </script>
    ```
    
    ⇒ TodoList.vue→ Todo.vue
    
- todo 데이터 내려받기
    
    ```jsx
    //TodoListItem.vue
    <template>
      <div>{{ todo.title }}</div>
    </template>
    
    <script>
    export default {
      name: 'TodoListItem',
      props: {
        todo: Object,
      }
    }
    </script>
    ```
    

## (4) Create Todo

```jsx
메서드(컴포넌트) CreateTodo
=> 액션 (dispatch()) : 맥션에서 todo만들어서
=> 뮤테이션 (commit()) : push만 함
=> state
```

### 1. TodoForm

- todoTitle을 입력 받을 input태그 생성
- TodoTitle을 저장하기 위해 data를 정의하고 input과 v-model을 이용해 양방향 바인딩
- enter 이벤트를 사용해 createTodo 메서드 출력 확인
    
    ```jsx
    // TodoForm.vue
    
    <template>
      <div>
        <input 
          type="text"
          v-model="todoTitle"
          @keyup.enter="createTodo"
        >
      </div>
    </template>
    
    <script>
    export default {
      name: 'TodoForm',
      data() {
        return {
          todoTitle: null,
        }
      },
      methods: {
        createTodo() {
          console.log(this.todoTitle)
        }
      }
    }
    </script>
    ```
    
    ![create.PNG](Todo%20with%20Vuex%20cef350d7d456466c8ae0114c31862dbc/create.png)
    

### 2. Actions

- createTodo 메서드에서 actions을 호출 (`dispatch`)
- todoTitle까지 함께 전달하기
    
    ```jsx
    // TodoForm.vue
    <script>
    export default {
      name: 'TodoForm',
      data() {
        return {
          todoTitle: null,
        }
      },
      methods: {
        createTodo() {
          // console.log(this.todoTitle)
          if (this.todoTitle) {
            this.$store.dispatch('createTodo', this.todoTitle)
          }
          this.todoTitle = null   // 입력 후, 입력창에 글자 지움
        }
      }
    }
    </script>
    ```
    
- createTodo에서 보낸 데이터를 수신 후 todoItem object를 생성
    
    ```jsx
    //index.js
    
    	actions: {
        createTodo(context, todoTitle) {
          // Todo 객체 만들기
          const todoItem = {
            title: todoTitle,
            isCompleted: false,
          }
          console.log(todoItem)
        }
      },
    ```
    
    ```jsx
    //참고
    actions에는 보통 비동기 관련 작업이 진행 되지만 현재 별도의 비동기 관련 작업이 불필요하기 
    때문에 입력 받은 todo 제목(todoTitle)을 todo 객체(todoItem)로 만드는 과정을 Actions에서 
    작성할 예정
    ```
    
    ![action.PNG](Todo%20with%20Vuex%20cef350d7d456466c8ae0114c31862dbc/action.png)
    

### 3. Mutations

- CREATE_TODO mutations 메서드에 todoItem를 전달하며 호출(`commit`)
    
    ```jsx
    // index.js
    
    actions: {
        createTodo(context, todoTitle) {
          // Todo 객체 만들기
          const todoItem = {
            title: todoTitle,
            isCompleted: false,
          }
          // console.log(todoItem)
          context.commit('CREATE_TODO', todoItem)   // 추가
        }
      },
    ```
    
- mutations에서 state의 todos에 접근해 배열에 요소를 추가
    
    ```jsx
    // index.js
    
    	mutations: {
        CREATE_TODO(state, todoItem) {
          state.todos.push(todoItem)
        }
      },
    ```
    

### 4. 공백 문자가 입력되지 않도록 처리하기

- `v-model.trim` & `if (this.todoTitle)`
    - 좌우 공백 삭제
    - 빈 문자열이 아닐 경우만 작성
    
    ```jsx
    // TodoForm.vue
    
    <template>
      <div>
        <!-- trim을 통해 공백제거 -->
        <input 
          type="text"
          v-model.trim="todoTitle"
          @keyup.enter="createTodo"
        >
      </div>
    </template>
    
    <script>
    export default {
      name: 'TodoForm',
      data() {
        return {
          todoTitle: null,
        }
      },
      methods: {
        createTodo() {
          // console.log(this.todoTitle)
          if (this.todoTitle) {
            this.$store.dispatch('createTodo', this.todoTitle)
          }
          this.todoTitle = null   // 입력 후, 입력창에 글자 지움
        }
      }
    }
    </script>
    ```
    

```jsx
1. Vue 컴포넌트의 method에서 dispatch()를 사용해 actions 메서드를 호출
2. Actions에 정의된 함수는 commit()을 사용해 mutations를 호출
3. Mutations에 정의된 함수가 최종적으로 state를 변경
```

## (5) Delete Todo

### 1. TodoListItem

- TodoListItem 컴포넌트에 삭제 버튼 및 deleteTodo 메서드 작성
    
    ```jsx
    <template>
      <div>
        ...
        <button @click="deleteTodo">Delete</button>
      </div>
    </template>
    
    <script>
    export default {
      ...
      methods: {
        deleteTodo() {
          console.log('삭제 메서드 호출!!')
        }
      }
    }
    </script>
    ```
    

### 2. Actions

- deleteTodo 메서드에서 deleteTodo actions 메서드 호출(`dispatch`)
- 삭제되는 todo를 함께 전달
    
    ```jsx
    <script>
    export default {
      methods: {
        deleteTodo() {
          // console.log('삭제 메서드 호출!!')
          this.$store.dispatch('deleteTodo', this.todo)
        }
      }
    }
    </script>
    ```
    
- deleteTodo actions 메서드에서 DELETE_TODO mutations 메서드 호출(`commit`)
    
    ```jsx
    actions: {
        createTodo(context, todoTitle) {
    		...
    		}
        // actions가 할게 없어보임 => 생략가능
        deleteTodo(context, todoItem) {
          context.commit('DELETE_TODO', todoItem)
        }
      },
    ```
    

### 3. Mutations

- DELETE_TODO 메서드 작성
    
    ```jsx
    	mutations: {
        CREATE_TODO(state, todoItem) {
          ...
        },
        DELETE_TODO(state, todoItem) {
          console.log(todoItem)
        },
      },
    ```
    
- 전달된 todoItem에 해당하는 todo 삭제
    
    ```jsx
    		DELETE_TODO(state, todoItem) {
          const index = state.todos.indexOf(todoItem)
          state.todos.splice(index, 1)
        },
    ```
    

## (6) Update Todo

### 1. TodoListItem

- todo를 클릭하면 완료 표시의 의미로 취소선 스타일을 적용하는 기능 구현
    - 즉, todo의 isCompleted 값 토글하기
- TodoListItem 컴포넌트에 클릭 이벤트를 추가 후 관련 actions 메서드 호출
    
    ```jsx
    <template>
      <div>
        <span @click="updateTodoStatus">{{ todo.title }}</span>
    		...
      </div>
    </template>
    
    <script>
    export default {
      ...
      methods: {
        deleteTodo() {
          ...
        },
        updateTodoStatus() {
          this.$store.dispatch('updateTodoStatus', this.todo)
        },
      }
    }
    </script>
    ```
    

### 2. Actions

- updateTodoStatus 메서드 작성
- 관련 mutations 메서드 호출
    
    ```jsx
    actions: {
        createTodo(context, todoTitle) {
    			...
        },
        // actions가 할게 없어보임 => 생략
        deleteTodo(context, todoItem) {
    			...
        },
        updateTodoStatus(context, todoItem) {
          context.commit('UPDATE_TODO_STATUS', todoItem)
        }
      },
    ```
    
- UPDATE_TODO_STATUS메서드 작성
    
    ```jsx
    mutations: {
        CREATE_TODO(state, todoItem) {
         ...
        },
        DELETE_TODO(state, todoItem) {
         ...
        },
        UPDATE_TODO_STATUS(state, todoItem) {
          console.log(todoItem)   
        }
      },
    ```
    
- map 메서드를 활용해 선택된 todo의 isCompleted를 반대로 변경 후 기존 배열 업데이트
    
    ```jsx
    mutations: {
        CREATE_TODO(state, todoItem) {
          ...
        },
        DELETE_TODO(state, todoItem) {
         ...
        },
        UPDATE_TODO_STATUS(state, todoItem) {
          console.log(todoItem)
          // todos 배열에서 선택된 todo의 is_completed값만 토글한 후
          // 업데이트 된 todos 배열로 되어야 함
          state.todos = state.todos.map((todo)=> {
            if (todo === todoItem) {
              todo.isCompleted = !todo.isCompleted
            }
            return todo
          })
        },
      },
    ```
    

### 3. 취소선 스타일링

- CSS 작성
    
    ```jsx
    //TodoListItem.vue
    
    <style>
      .is-completed {
        text-decoration: line-through;
      }
    </style>
    ```
    
- v-bind를 활용해 isCompleted 값에 따라 css 클래스가 토글 방식으로 적용되도록 작성하기
    
    ```jsx
    //TodoListItem.vue
    
    <template>
      <div>
        <span 
          @click="updateTodoStatus"
          :class="{ 'is-completed': todo.isCompleted }"  
        >
          {{ todo.title }}
        </span>
        <button @click="deleteTodo">Delete</button>
      </div>
    </template>
    ```
    

## (7) 상태별 todo 개수 계산

### 1. 전체 todo 개수

- allTodosCount getters 작성
- state에 있는 todos 배열의 길이 계산
    
    ```jsx
    //index.js
    
    	getters: {
        allTodosCount(state) {
          return state.todos.length
        }
      },
    ```
    
- getters에 계산된 값을 각 컴포넌트의 computed에서 사용
    
    ```jsx
    //App.vue
    
    <template>
      <div id="app">
        ...
        <h2>모든 Todo 개수: {{ allTodosCount }}</h2>
        ...
      </div>
    </template>
    ```
    
    ```jsx
    export default {
      ...
      computed: {
        allTodosCount() {
          return this.$store.getters.allTodosCount
        }
      }
    }
    ```
    

### 2. 완료된 todo 개수

- computedTodoCount getters 작성
- isCompleted가 true인 todo들만 필터링한 배열을 만들고 길이 계산
- filter를 활용하여 완료 여부에 따른 새로운 객체 목록을 작성 후 길이 반환
    
    ```jsx
    //index.js
    
    getters: {
        allTodosCount(state) {
          return state.todos.length
        },
        completedTodosCount(state) {
          // 1. 완료된 투두만 모아놓은 새로운 배열을 생성
          const completedTodos = state.todos.filter((todo) => {
            return todo.isCompleted === true
          })
          // 2. 그 새로운 배열의 길이를 반환
          return completedTodos.length
        }
      },
    ```
    
    ```jsx
    //App.vue
    <template>
      <div id="app">
        ...
        <h2>완료된 Todo 개수: {{ completedTodosCount }}</h2>
    		...
      </div>
    </template>
    
    export default {
      ...
      computed: {
        allTodosCount() {
          ...
        },
        completedTodosCount() {
          return this.$store.getters.completedTodosCount
        }
      }
    }
    ```
    

### 3. 미완료된 todo 개수

- 미완료된 todo 개수 === 전체 개수 - 완료된 개수
- getters가 두번째 인자로 getters를 받는 것을 활용하기
- unCompletedTodosCount getters 작성
    
    ```jsx
    getters: {
        allTodosCount(state) {
          return state.todos.length
        },
        completedTodosCount(state) {
          // 1. 완료된 투두만 모아놓은 새로운 배열을 생성
          const completedTodos = state.todos.filter((todo) => {
            return todo.isCompleted === true
          })
          // 2. 그 새로운 배열의 길이를 반환
          return completedTodos.length
        },
        unCompletedTodosCount(state, getters) {
          return getters.allTodosCount - getters.completedTodosCount
        }
      },
    ```
    
    ```jsx
    <template>
      <div id="app">
        ...
        <h2>미완료된 Todo 개수: {{ unCompletedTodosCount }}</h2>
        ...
      </div>
    </template>
    
    export default {
      name: 'App',
      components: {
        TodoList,
        TodoForm,
      },
      computed: {
        allTodosCount() {
          ...
        },
        completedTodosCount() {
          ...
        },
        unCompletedTodosCount() {
          return this.$store.getters.unCompletedTodosCount
        }
      }
    }
    ```
    

## (8) Local Storage

⇒ `새로고침하면 모든 정보가 초기화되는 현상을 고치고 싶음`

### 1. 개요

- 브라우저의 `Local Storage` 에 todo 데이터를 저장하여 브라우저를 종료하고 다시 실행해도 데이터가 보존될 수 있도록 하기

### 2. Window.`localStorage`.method()

- 브라우저에서 제공하는 저장공간 중 하나인 Local Storage에 관련된 속성
- 만료되지 않고 브라우저를 종료하고 다시 실행해도 데이터가 보존됨
- 데이터가 `문자열 형태로` 저장됨 (JSON 이라는 소리)
- 관련 메서드
    - `setItem(key, value)` - key, value 형태로 데이터 저장
    - `getItem(key)` - key에 해당하는 데이터 조회

### 3. 실습

- todos 배열을 Local Storage에 저장하기
- 데이터가 문자열 형태로 저장되어야 하기 때문에 `JSON.stringify` 를 사용해 문자열로 변환해주는 과정 필요
- state를 변경하는 작업이 아니기 때문에 mutations가 아닌 actions에 작성
    
    ```jsx
    actions: {
        createTodo(context, todoTitle) {
          ...
        },
        // actions가 할게 없어보임 => 생략
        deleteTodo(context, todoItem) {
          ...
        },
        updateTodoStatus(context, todoItem) {
         ...
        },
        saveTodosToLocalStorage(context) {
          const jsonTodos = JSON.stringify(context.state.todos)
          window.localStorage.setItem('todos' , jsonTodos ) //key는 임의 지정하면 된다.
    	    // localStorage.setItem('todos' , jsonTodos ) // window 생략해도 무방
    		},
    ```
    
- todo 생성, 삭제, 수정시에 모두 saveTodosToLocalStorage action 메서드가 실행 되도록 함
    
    ```jsx
    actions: {
        createTodo(context, todoTitle) {
          ...
          context.dispatch('saveTodosToLocalStorage')
        },
        // actions가 할게 없어보임 => 생략
        deleteTodo(context, todoItem) {
          ...
          context.dispatch('saveTodosToLocalStorage')
        },
        updateTodoStatus(context, todoItem) {
         ...
          context.dispatch('saveTodosToLocalStorage')
        },
        saveTodosToLocalStorage(context) {
         ...
        }
      },
    ```
    
    ⇒  Local Storage에 있는 todo 목록을 불러오는 것이 아니기 때문에 페이지 새로고침 이후 목록이 사라짐 (실제로 데이터틑 가지고 있음)
    
- 불러오기 버튼 생성
    
    ```jsx
    <template>
      <div id="app">
        ...
        <button @click="loadTodos">Todo 불러오기</button>
      </div>
    </template>
    ```
    
- loadTodos 메서드 작성
    
    ```jsx
    	methods: {
        loadTodos() {
          this.$store.dispatch('loadTodos')
        }
      }
    ```
    
- loadTodos actions 메서드 작성
    
    ```jsx
    actions: {
        createTodo(context, todoTitle) {
          ...
        },
        // actions가 할게 없어보임 => 생략
        deleteTodo(context, todoItem) {
          ...
        },
        updateTodoStatus(context, todoItem) {
          ...
        },
        saveTodosToLocalStorage(context) {
          ...
        },
        loadTodos(context) {
          context.commit('LOAD_TODOS')
        }
      },
    ```
    
- LOAD_TODOS mutation 메서드 작성
    - 문자열 데이터를 다시 object 타입으로 변환 (`JSON.parse`)하여 저장
    
    ```jsx
    	mutations: {
        CREATE_TODO(state, todoItem) {
          ...
        },
        DELETE_TODO(state, todoItem) {
          ...
        },
        UPDATE_TODO_STATUS(state, todoItem) {
          ...
        },
        LOAD_TODOS(state) {
          const localStorageTodos =  localStorage.getItem('todos')
          const parsedTodos = JSON.parse(localStorageTodos)
          state.todos = parsedTodos
        }
      },
    ```
    

## (9)vuex-persistedstate

⇒ context.dispatch('saveTodosToLocalStorage') 의 중복을 줄여줄 수 있음

### 1. 설치

`$ npm i vuex-persistedstate`

### 2. 적용

```jsx
import createPersistedState from 'vuex-persistedstate'
export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
```

### 3. 주석처리

- 작성한 localStorage 관련 코드를 모두 주석 처리하기
    - App.vue
        - 불러오기 버튼
        - loadTodos 메서드
    - index.js
        - LOAD_TODOS mutation 메서드
        - saveTodosToLocalStarage action 메서드
        - loadTodos action 메서드
        - context.dispatch('saveTodosToLocalStorage')  코드 3줄