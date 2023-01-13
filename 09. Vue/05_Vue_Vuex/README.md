# Vuex

# Vuex

## (1) 개요

- `상태 관리`(State Management)가 무엇인지 이해하기
- Vuex가 무엇인지, 왜 필요한지 이해
- Vuex 기본 문법 알아보기

## (2) State Management (`상태 관리`)

### 1. 상태 관리

- `상태`는 현재에 대한 정보(data) 를 뜻함
- `Web Application에서의 상태`는 현재 App이 가지고 있는 Data로 표현 가능
    
    ⇒  여러 개의 component를 조합해서 하나의 App을 만듦
    
    ⇒ 각 component는 독립적이기 때문에 각각의 상태를 가짐
    
    ⇒ `여러 개의 component가 같은 상태를 유지해야 함`
    
    ⇒ 상태관리가 중요!!!
    

### 2. Pass props & Emit Event

- props와 event를 이용해서 상태를 관리 해옴
- 각각의 component들이 독립적으로 데이터를 관리하며 같은 데이터를 공유하고 있으므로, 각 component가 동일한 상태를 유지하고 있음
    
    ⇒ 데이터의 흐름을 직관적으로 파악 가능
    

`=>` component의 중첩이 깊어지면 데이터 전달이 쉽지 않음

⇒ 공통의 상태를 유지해야 하는 component가 많아지면 데이터 전달 구조가 복잡해짐

⇒ How to do? `Centralized Store`

### 3. Centralized Store

- `중앙 저장소(store)에 데이터를 모아서 상태 관리`
- 각 component는 중앙 저장소의 데이터를 사용
    
    ⇒ component의 계층에 상관없이 중앙 저장소에 접근해서 데이터를 얻거나 변경 가능
    
    ⇒ 중앙 저장소의 데이터가 변경되면 각각의 component는 해당 데이터의 변화에 반응하여 새로 변경된 데이터를 반영
    
    ⇒ 규모가 크거나 component 중첩이 깊은 프로젝트의 관리가 매우 편리
    

### 4. Vuex의 정의

- `state management pattern` + `Library` for vue.js
- 중앙 저장소를 통해 상태 관리를 할 수 있도록 하는 라이브러리
- 데이터가 예측 가능한 방식으로만 변경 될 수 있도록 하는 `규칙을 설정`하며, `Vue의 반응성을 효율적으로 사용하는 상태 관리 기능`을 `제공`
- `Vue의 공식 도구` 로써 다양한 기능을 제공

## (3) Vuex 시작

### 1. 프로젝트 with vuex 실행

- vue 프로젝트 생성 : `$vue create vuex-app`
- 디렉토리 이동 : `$cd vuex-app`
- Vue CLI를 통해 vuex plugin 적용 : `$vue add vuex`
    
    ![vuex.PNG](Vuex%20f8dc7935aec14ca980d452c6903559a3/vuex.png)
    
    ⇒ store 생성 : 이 공간이 위에서 언급한 `중앙 저장소` !
    

### 2. Vue와 Vuex 인스턴스 비교

![vuevsvuex.PNG](Vuex%20f8dc7935aec14ca980d452c6903559a3/vuevsvuex.png)

1. `State`
    - vue 인스턴스 data에 해당
    - 중앙에서 관리하는 모든 상태 정보
    - 개별 component는 state에서 데이터를 가져와서 사용
        - 개별 component가 관리하던 data를 중앙 저장소에서 관리하게 됨
    - state의 데이터가 변화하면 해당 데이터를 사용(공유)하는 component도 자동으로 다시 렌더링
    - `$store.state` 로 state 데이터에 접근
2. `Mutations`
    - `실제로 state를 변경하는 유일한 방법`
    - vue 인스턴스의 methods에 해당하면 Mutations에서 호출되는 핸들러 함수는 반드시 `동기적` 이어야 함
        - 비동기 로직으로 mutations를 사용해서 state를 변경하는 경우, state의 변화의 시기를 특정할 수 없기 때문!!!!
    - 첫 번째 인자로 `state` 를 받으며, component 혹은 Actions에서 `commit()` 메서드로 호출됨
        - mutation, action에서 호출되는 함수를 handler 함수라고 함
3. `Actions`
    - mutations와 비슷하지만 `비동기` 작업을  포함할 수 있다는 차이가 있음
    - `state를 직접 변경하지 않고 commit() 메서드를 mutations를 호출해서 state를 변경`
    - context 객체를 인자로 받으며, 이 객체를 통해 store.js의 모든 요소와 메서드에 접근할 수 있음(⇒ state를 직접 변경할 수 있지만 하지 마!!!)
    - component에서 `dispatch()` 메서드에 의해 호출됨
4. `Getters`
    - vue 인스턴스의 computed에 해당
    - `state를 활용하여 계산된 값을 얻고자 할 때 사용`
        - state의 원본 데이터를 건들지 않고 계산된 값을 얻을 수 있음
    - computed와 마찬가지로 getters의 결과는 캐시 되며, 종속된 값이 변경된 경우에만 재계산됨
    - getters에서 계산된 값은 state에 영향을 미치지 않음
    - 첫번째 인자로 `state`, 두번째 인자로 `getter` 를 받음

```jsx
//정리
1. state : 중앙에서 관리하는 '모든 상태 정보'
2. mutations : 'state를 변경'하기 위한 methods
3. actions : '비동기 작업이 포함될 수 있는(외부 API와의 소통 등) methods
					 : state를 변경하는 것 외의 모든 로직 진행
4. getters : state를 활용해 '계산한 새로운 변수 값'
-----------------------------------------------------------------------------
5. component에서 데이터를 조작하기 위한 데이터의 흐름
	- component => (actions) => mutations => state
6. component에서 데이터를 사용하기 위한 데이터의 흐름
	- state => (getters) => component
```

## (4) Vuex 실습

### 1. 축약형 사용

- before
    
    ```jsx
    const obj1 = {
    	addValue: function (value) {
    		return value
    	},
    }
    ```
    
- after
    
    ```jsx
    const obj2 = {
    	addValue(value) {
    		return value
    	},
    }
    ```
    

### 2. state

1. 중앙에서 관리하는 모든 상태 정보 `$store.state` 로 접근 가능
    - store의 state에 message 데이터 정의
    
    ```jsx
    //index.js
    
    import Vue from 'vue'
    import Vuex from 'vuex'
    
    Vue.use(Vuex)
    
    export default new Vuex.Store({
      state: {
        message: 'message in store',
      },
      getters: {
      },
      mutations: {
      },
      actions: {
        }
      },
      modules: {
      }
    })
    ```
    
2. component에서 state 사용
    
    ```html
    <!--App.vue-->
    <template>
      <div id="app">
        <h1>{{ $store.state.message }}</h1>
      </div>
    </template>
    ```
    
    ⇒ 이렇게 사용 가능하지만, 권장하지 않음!! ⇒ `computed` 정의해서 접근해!!
    
3. `$store.state` 로 바로 접근하기 보다는 `computed` 에 정의 후 접근하는 것을 권장
    
    ```html
    <template>
      <div id="app">
        <h1>{{ message }}</h1>
      </div>
    </template>
    ```
    
    ```jsx
    <script>
    export default {
      name: 'App',
      computed: {
        message() {
          return this.$store.state.message
        }
      },
    }
    </script>
    ```
    

### 3. actions

- state를 변경할 수 있는 `mutations 호출`
- component에서 `dispatch()에 의해 호출됨`
- `dispatch(A, B)`
    - A: 호출하고자 하는 actions 함수
    - B: 넘겨주는 데이터(payload)
1. actions에 정의된 changeMessage 함수에 데이터 전달하기
    - component에서 actions는 `dispatch()` 에 의해 호출됨
    
    ```jsx
    //App.vue
    
    <script>
    
    export default {
      name: 'App',
      data() {
        return {
          inputData: null,
        }
      },
      components: {
      },
      computed: {
        message() {
          return this.$store.state.message
        }
      },
      methods: {
        changeMessage() {
          const newMessage = this.inputData
          this.$store.dispatch('changeMessage', newMessage)
    			this.inputData = null
        },
      },
    }
    </script>
    ```
    
2. actions의 첫 번째 인자는 `context`
    - context는 store의 전반적인 속성을 모두 가지고 있으므로 context.state와 context.getters를 통해 mutations를 호출하는 것이 모두 가능
    - dispatch()를 사용해 다른 actions도 호출할 수 있음
        
         `=>` 단, actions에서 state르 직접 조작하는 것은 삼가!
        
3. actions의 두 번째 인자는 `payload`
    - 넘겨준 데이터를 받아서 사용
    
    ```jsx
    // index.js
    
    import Vue from 'vue'
    import Vuex from 'vuex'
    
    Vue.use(Vuex)
    
    export default new Vuex.Store({
      state: {
        message: 'message in store',
      },
      getters: {
      },
      mutations: {
      },
      actions: {
        changeMessage(context, newMessage) {
          console.log(context)
          console.log(newMessage)
        }
      },
      modules: {
      }
    })
    ```
    

### 4. mutations

1. `actions에서 commit()을 통해 mutations 호출하기`
    - mutations는 state를 변경하는 유일한 방법
    - component 또는 actions에서 `commit()에 의해 호출됨`
    - `commit(A, B)`
        - A : 호출하고자 하는 mutations 함수
        - B : payload
    
    ```jsx
    //index.js
    import Vue from 'vue'
    import Vuex from 'vuex'
    
    Vue.use(Vuex)
    
    export default new Vuex.Store({
      ...
      actions: {
        changeMessage(context, newMessage) {
          // console.log(context)
          // console.log(newMessage)
          context.commit('CHANGE_MESSAGE', newMessage)
        }
      },
      ...
    })
    ```
    
    ⇒ mutations는 state에 연결시켜주는 중요한 역할을 하므로 특별히 대문자로 지칭한다.
    
2. `mutations 함수 작성하기`
    - mutations는 state를 변경하는 유일한 방법
    - mutations 함수
        - 첫 번째 인자는 state
        - 두 번째 인자는 payload
    
    ```jsx
    //index.js
    	mutations: {
        CHANGE_MESSAGE(state, newMessage) {
          // console.log(state)
          // console.log(newMessage)
          state.message = newMessage
        }
      },
    ```
    
    ![bf.PNG](Vuex%20f8dc7935aec14ca980d452c6903559a3/bf.png)
    
    ![at.PNG](Vuex%20f8dc7935aec14ca980d452c6903559a3/at.png)
    
    ⇒ state를 변경시킴!
    

### 5. getters

1. `getters 사용해 보기`
    - getters는 state를 활용한 새로운 변수
    - getters 함수
        - 첫 번째 인자 : state
        - 두 번째 인자 : getters
    
    ```jsx
    //index.js
    export default new Vuex.Store({
      ...
    	getters: {
        messageLength(state) {
          return state.message.length
        },
      },
      ...
    })
    ```
    
2. `getters 출력하기`
    - getters 역시 state와 마찬가지로 computed에 정의해서 사용하는 것을 권장
    
    ```html
    <!-- App.vue -->
    <template>
      <div id="app">
        ...
        <h2>입력된 문자의 길이는 {{ messageLength }}</h2>
        ...
      </div>
    </template>
    ```
    
    ```jsx
    <script>
    
    export default {
      name: 'App',
      ...
      computed: {
        ...
        messageLength() {
          return this.$store.getters.messageLength
        },
      },
    	...
    }
    </script>
    ```