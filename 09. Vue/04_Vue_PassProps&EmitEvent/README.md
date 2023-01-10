# Pass Props & Emit Event

# Pass Props & Emit Event

## (1) Data in components

### 1. 개요

- 정적 웹페이지가 아닌, 동적 웹페이지를 만들고 있음
    
    ⇒ 웹페이지에서 다뤄야 할 데이터가 등장
    
    ex) User data, 게시글 data …
    
- 한 페이지 내에서 같은 데이터를 공유 해야 함
    
    ⇒ 페이지들이 component로 구분 됨
    
- MyComponent에 정의된 data를 MyComponentItem에서 사용하고 싶다!
- MyComponentItem에도 똑같은 data를 정의
    - MyComponent의 data와 MyComponentItem의 데이터가 동일한 data가 맞니?
    - MyComponent의 data와 변경된다면 MyComponentItem도 같이 변경이 될까?
    
    ⇒ `NO` 각 Component는 독립적으로 서로 다른 data를 가짐
    
    - 완전히 동일한 data를 서로 다른 Component에서 보여주려면 어떻게 해야할까?
    
    ⇒ 필요한 컴포넌트끼리 데이터를 주고받음 
    
    ```jsx
    1. 데이터의 흐름을 파악하기 힘듦
    2. 개발 속도 저하
    3. 유지보수 난이도 증가
    ```
    
    ⇒ 컴포넌트는 부모-자식 관계를 가지고 있으므로, 부모-자식 관계만 데이터를 주고받게 함
    
    ```jsx
    1. 데이터의 흐름을 파악하기 용이
    2. 유지 보수하기 쉬워짐
    ```
    

### 2. pass props & emit event

- pass props 방식
    - 부모 ⇒ 자식으로의 데이터의 흐름
- emit event 방식
    - 자식 ⇒ 부모로의 데이터의 흐름

## (2) Pass Props

### 1. 개요

- 요소의 속성을 사용하여 데이터 전달
- props는 부모 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
- 자식 컴포넌트는 props 옵션을 사용하여 수신하는 props를 명시적을 선언해야함
- 정적인 데이터를 전달하는 경우 static props라고 명시하기도 함
- 요소에 속성을 작성하듯이 사용 가능하여, `prop-data-name=’value’`의 형태로 데이터 전달
    - 이때 속성의 키 값은 kebab-case를 사용

```jsx
html이 kebab-case => JavaScripts는 camelCase
(케밥 먹은 낙타)
: 보내는 쪽과 받는 쪽이 다르므로 주체에 따라 case를 다르게 적어야함
```

- Prop 명시
- 데이터를 받는 쪽, 즉 하위 컴포넌트에서도 props를 type과 함께 명시
- 컴포넌트를 문서화할 뿐만 아니라, 잘못된 타입이 전달하는 경우 브라우저의 자바스크립트 콘솔에서 사용자에게 경고

### 2. MyComponent to MyComponentItem

- MyComponent.vue ( `위에서 아래로 보내주고` )
    
    ```html
    <template>
      <div class="border">
        <h1>이건 이한빈 MyComponent 다! </h1>
        <!-- 1. 보내라 -->
        <MyComponentItem static-props="MyComponent에서 보낸 데이터"/>
      </div>
    </template>
    ```
    
- MyComponentItem.vue ( `아래서 받아서 선언하고 불러온다`)
    
    ```jsx
    <template>
      <div>
        <h3>나는 MyComponent의 하위 컴포넌트!</h3>
    		<!-- 3. 불러오기 -->
        <p>{{ staticProps }}</p>
      </div>
    </template>
    
    <script>
    export default {
      name: 'MyComponentItem',
      // 2. 선언
      props: {
        staticProps: String,
      }
    }
    </script>
    
    <style>
    
    </style>
    ```
    

### 3. Pass Props convention

- 부모에서 넘겨주는 props
    - `kebab-case`
- 자식에서 받는 props
    - `camelCase`
- 부모 템플릿에서 kebab-case로 넘긴 변수를 자식의 스크립트에서 자동으로 camelCase로 변환하여 인식

### 4. Dynamic props

- 변수를 props로 전달할 수 있음
- v-bind(`:`)를 사용해 데이터를 동적으로 바인딩
- 부모 컴포넌트의 데이터가 업데이트 되면 자식 컴포넌트로 전달되는 데이터 또한 업데이트

### 5. Dynamic props 실습

- MyComponent.vue
    
    ```jsx
    <template>
      <!-- div의 border class 생성 -->
      <div class="border">
        <h1>이건 이한빈 MyComponent 다! </h1>
        <!-- 1. 보내라 -->
        <MyComponentItem 
          static-props="MyComponent에서 보낸 데이터"
          :dynamic-props="dynamicProps"
        />
      </div>
    </template>
    
    <script>
    import MyComponentItem from '@/components/MyComponentItem'
    
    export default {
      name: 'MyComponent',
      components:{
        MyComponentItem,
      **},
      // 함수의 return 객체여야함 
      // 이름공간 (스코프) 때문에
      // vue-cli에서 사용
      data: function () {
        return {
          dynamicProps: '이건 동적인 데이터'
        }
      }
    }
    </script>
    ```
    
    ⇒ script에서 data를 함수로 정의하고
    
    ⇒ templates dynamic-props로 정의한 데이터를 아래로 내려준다 (MyComponentItem)
    
- MyComponentItem
    
    ```jsx
    <template>
      <div>
        <h3>나는 MyComponent의 하위 컴포넌트!</h3>
        <p>{{ staticProps }}</p>
        <p>{{ dynamicProps }}</p>
      </div>
    </template>
    
    <script>
    export default {
      name: 'MyComponentItem',
      // 2. 선언
      props: {
        staticProps: String,
        dynamicProps: String,
      }
    }
    </script>
    ```
    
    ⇒ script에서 dynamicProps를 선언
    
    ⇒ templates에서 출력
    
- `해석`
    - `:dynamic-props="dynamicProps"`
        - 앞의 key값(`dynamic-props`)이란 이름으로 뒤의 `" "` 안에 오는 데이터(`dynamicProps`)를 전달하겠다는 뜻
    - `my-props="dynamicProps"` 로 데이터를 넘긴다면, 자식 컴포넌트에서 myProps로 데이터를 받아야함

### 6. `단방향 데이터 흐름`

- 모든 props는 부모에서 자식으로 즉, 아래로 단방향 바인딩을 형성
- 부모 속성이 업데이트되면자식으로 흐르지만 반대 방향은 아님
    - 부모 컴포넌트가 업데이트될 때마다 자식 컴포넌트의 모든 props들이 최신 값으로 새로고침 됨
- 목적
    - 하위 컴포넌트가 실수로 상위 컴포넌트 상태를 변경하여 앱의 데이터 흐름을 이행하기 힘들게 만드는 것을 방지

## (3) Emit Event

### 1. 개요

- 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달할 때는 `이벤트를 발생 시킴`
- 이번트를 발생시키는 게 어떻게 데이터를 전달하는 것?
    1. 데이터를 이벤트 리스너의 콜백함수의 인자로 전달
    2. 상위 컴포넌트는 해당 이벤트를 통해 데이터를 받음

```jsx
이벤트를 발생시켜서 자식이 부모에게 보낼 수 있게 해줌!
```

### 2. `emit`

- $emit 메서드를 통해 부모 컴포넌트에 이벤트를 발생
    - $emit(’event-name’) 형식으로 사용하며 부모 컴포넌트에 `event-name` 이라는 이벤트가 발생했다는 것을 알림
    - 마치 사용자가 마우스 클릭을 하면 click 이벤트가 발생하는 것처럼 $emit(’event-name’)가 실행되면 event-name 이벤트가 발생하는 것

### 3. Emit Event 실습

- 자식 컴포넌트에 버튼을 만들고 클릭 이벤트 추가(MyComponentItem)
    
    ```jsx
    <div>
      ...
      <button @click="childToParent">클릭!</button>
    </div>
    ```
    
- $emit을 통해 부모 컴포넌트에게 child-to-parent 이벤트를 트리거(MyComponentItem)
    
    ```jsx
    <script>
    export default {
      name: 'MyComponentItem',
      props: {
        ...
      },
      methods: {
        childToParent: function () {
          this.$emit('child-to-parent') // 받는쪽이 html이므로 케밥으로 작성
        }             // 이름            
      },
    }
    </script>
    ```
    
- emit된 이벤트를 상위 컴포넌트에서 청취(MyComponent)
    
    ```html
    <template>
      <div class="border">
        <h1>이건 이한빈 MyComponent 다! </h1>
        <MyComponentItem 
          static-props="MyComponent에서 보낸 데이터"
          :dynamic-props="dynamicProps"
          @child-to-parent = "parentGetEvent"    <!-- 이거 추가 -->
        />
      </div>
    </template>
    ```
    
- 핸들러 함수 실행 (MyComponent)
    
    ```jsx
    <script>
    import MyComponentItem from '@/components/MyComponentItem'
    
    export default {
      name: 'MyComponent',
      components:{
        MyComponentItem,
      },
      data: function () {
    		...
      },
    	// 요거 추가
      methods: {
        parentGetEvent: function () {
          console.log('자식 컴포넌트에서 발생한 emit 이벤트를 받았다!')
        }
      }
    }
    </script>
    ```
    

```jsx
// 흐름
1. 자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취하여 연결된 핸들러 함수('childToParent') 호출
2. 호출된 함수에서 $emit을 통해 상위 컴포넌트에 이벤트('child-to-parent') 발생
3. 상위 컴포넌트는 자식 컴포넌트가 발생시킨 이벤트('child-to-parent')를 청취하여 
	연결된 핸들러 함수('parentGetEvent') 호출
```

### 4. emit with data

- 이벤트를 발생(emit)시킬 때 인자로 데이터를 전달 가능
    
    ```jsx
    <script>
    export default {
      name: 'MyComponentItem',
      props: {
    		...
      },
      methods: {
        childToParent: function () {
    			// 자식에서 데이터를 보냄 
          this.$emit('child-to-parent', '나는 자식이 보낸 데이터다') // 받는쪽이 html이므로 케밥으로 작성
        }             // 이름             // 데이터
      },
    }
    </script>
    ```
    
- 전달된 데이터는 이벤트와 연결된 부모 컴포넌트의 핸들러 함수의 인자로 사용 가능
    
    ```jsx
    methods: {
        parentGetEvent: function (childData) {
          console.log('자식 컴포넌트에서 발생한 emit 이벤트를 받았다!')
          console.log(childData)
        }
      }
    ```
    
    ⇒ callback 함수에 childData 인자를 받아서  출력 가능
    

```jsx
//흐름
1. 자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취하여 연결된 핸들러 함수('ChildToParent') 호출
2. 호출된 함수에서 $emit을 통해 부모 컴포넌트에 이벤트('child-to-parent')를 발생
	- 이벤트 데이터('child data')를 함께 전달
3. 부모 컴포넌트는 자식 컴포넌트의 이벤트 ('child-to-parent')를 청취하여 연결된 핸들러 함수('parentGetEvent') 호출,
	- 함수의 인자로 전달된 데이터('child data')가 포함되어 있음
4. 호출된 함수에서 console.log('~child data~')가 실행 
```

`Tip` 

- 자식을 할아버지까지 올리고 싶으면 자식 ⇒ 아버지 ⇒ 할아버지 순으로 올라가야함
    - 즉, 한 단계씩 올라가야만 한다.
- 정적인 데이터뿐만 아니라, 동적인 데이터도 올려보낼 수 있다.

### 5. emit with dynamic data ( 동적 데이터 전달)

- (MyComponentItem)
    
    ```html
    <template>
      <div>
        <h3>나는 MyComponent의 하위 컴포넌트!</h3>
        <p>{{ staticProps }}</p>
        <p>{{ dynamicProps }}</p>
        <button @click="childToParent">클릭!</button>
        <!-- 추가 -->
        <input 
          type="text"
          v-model="childInputData"
          @keyup.enter="childInput"
        >
      </div>
    </template>
    ```
    
    ```jsx
    <script>
    export default {
      ...
    	// 동적 데이터 생성
      data: function () {
        return {
          childInputData: null,
        }
      },
      methods: {
        childToParent: function () {
          this.$emit('child-to-parent', '나는 자식이 보낸 데이터다') // 받는쪽이 html이므로 케밥으로 작성
        },
    		// 생성된 동적 데이터를 부모에게 보내줌
        childInput: function () {
          this.$emit('child-input', this.childInputData)
        }
      },
    
    }
    </script>
    ```
    
- (MyComponent)
    
    ```html
    <template>
      <div class="border">
        <h1>이건 이한빈 MyComponent 다! </h1>
        <MyComponentItem 
          static-props="MyComponent에서 보낸 데이터"
          :dynamic-props="dynamicProps"
          @child-to-parent = "parentGetEvent"
          @child-input= "getDynamicData"    <!-- 이거 추가 -->
        />
      </div>
    </template>
    ```
    
    ```jsx
    <script>
    // 1. 불러오기
    import MyComponentItem from '@/components/MyComponentItem'
    
    export default {
      ...
      methods: {
        parentGetEvent: function (childData) {
          console.log('자식 컴포넌트에서 발생한 emit 이벤트를 받았다!')
          console.log(childData)
        },
    		// 요거 추가
        getDynamicData: function (childInputData) {
          console.log(`사용자가 입력한 값은 ${childInputData}입니다.`)
        }
      }
    }
    </script>
    ```
    

```jsx
//흐름
1. 자식 컴포넌트에 있는 keyup.enter 이벤트를 청취하여 연결된 핸들러 함수('ChildInput') 호출
2. 호출된 함수에서 $emit을 통해 부모 컴포넌트에 이벤트('child-input')를 발생
	- 이벤트에 v-model로 바인딩 된 입력받은 데이터를 전달
3. 상위 컴포넌트는 자식 컴포넌트의 이벤트('child-input')를 청취하여 연결된 핸들러 함수('getDynamicData') 호출,
	- 함수의 인자로 전달된 데이터가 포함되어 있음
4. 호출된 함수에서 console.log('~입력받은 데이터~') 실행
```

### 6. pass props / emit event 컨벤션

- HTML 요소 : kabab-case / JavaScript : camelCase
- props
    - 상위 ⇒ 하위 흐름에서 HTML 요소로 내려줌 : kebab-case
    - 하위에서 받을 때 JavaScript 에서 받음 : camelCase
- emit
    - emit 이벤트를 발생시키면 HTML 요소가 이벤트를 청취 : kebab-case
    - 메서드, 변수명 등은 JavaScript에서 사용 : camelCase

## (4) 실습