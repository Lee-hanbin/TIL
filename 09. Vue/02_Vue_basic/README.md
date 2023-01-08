# Vue 기초문법

# Vue instance

## (1) MVVM pattern

### 1. 개요

- 소프트웨어 아키텍처 패턴의 일종
- 마크업 언어로 구현하는 그래픽 사용자 인터페이스(view)의 개발 Back-end(model)로 부터 분리시켜 view가 어느 특정한 모델 플랫폼에 종속되지 않도록 함

### 2. 도식화

![mvvm.PNG](Vue%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%E1%84%86%E1%85%AE%E1%86%AB%E1%84%87%E1%85%A5%E1%86%B8%20600105762fa749128a06bcacaa4fe234/mvvm.png)

### 3. 구조

- Model : 실제 데이터 (JSON)
- View : 우리 눈에 보이는 부분 (DOM)
- View Model (Vue)
    - View를 위한 Model
    - View와 연결(binding)되어 Action을 주고 받음
    - Model이 변경되면 View Model도 변경되고 바인딩된 View도 변경됨
    - View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩된 다른 View도 변경됨

### 4. 정리

- View는 Model을 모름 <=> Model도 View를 모름
    
    ⇒ `독립적` `적은 의존성`
    
    = DOM은 Data를 모름 <=> Data도 DOM을 모름
    

## (2) Vue instance

### 1. 생성자 함수 (`05번 파일`)

- Vue CDN 가져오기
- `new` 연산자를  사용한 생성자 함수 호출
    - vue instance 생성
    - `생성자 함수`
        - 동일한 구조의 객체를 여러 개 만들고 싶을 때 사용
        - 특별한 함수를 의미하는 것은 아님
        - 함수 이름은 반드시 대문자로 시작
        - 생성자 함수를 사용할 때는 반드시 `new`  연산자를 사용
- 인스턴스 출력확인
    
    ```jsx
    function Member(name, age, sId) {
      this.name = name
      this.age = age
      this.sId = sId
    }
    
    const member3 = new Member('isaac', 21, 2022654321)
    
    for (const i of [member, member2, member3]) {
      console.log(i)
    }
    ```
    

### 2. el(element)

- `Vue instance`와 `DOM`을 mount(`연결`)하는 옵션
    - View와 Model을 연결하는 역할
    - HTML id 혹은 class와 마운트 가능
- Vue instance와 연결되지 않은 DOM 외부는 Vue의 영향을 받지 않음
    - Vue 속성 및 메서드 사용 불가

```jsx
	// 에러 발생 => Vue와 연동되어 있음
	<div id="app">
    {{ message }}
  </div>

	// 그대로 출력 => Vue와 연동 x
  <div>
    {{ message }}
  </div>

// 1. Vue instance constructor
    const vm = new Vue()
    console.log(vm)

    // 2. el
    const app = new Vue({
      el: '#app',
```

⇒ id가 app인 element를 연결하겠다. (혹은 class로 연결)

### 3. data

- Vue instance의 `데이터 객체` 혹은 `인스턴스 속성`
- 데이터 객체는 반드시 기본 객체 `{ }(object)` 여야 함
- 객체 내부의 아이템들은 value로 모든 타입의 객체를 가질 수 있음
- 정의된 속성은 `interpolation{{ }}` 을 통해 view에 렌더링 가능
- Vue instance에 `data` 객체 추가
    
    ```jsx
    	// 에러 발생 => Vue와 연동되어 있음 => data로 인해 'Hello, Vue' 출력
    	<div id="app">
        {{ message }}
      </div>
    
    	// 그대로 출력 => Vue와 연동 x => 'message' 출력
      <div>
        {{ message }}
      </div>
    
    	// 2. el
       const app = new Vue({
         el: '#app',
         // 3. data <---- 추가
         data: {    
           message: 'Hello, Vue!'
         },
    ```
    

### 4. methods

- Vue instance의 `method` 들을 정의하는 곳
- `methods` 객체 정의
    - 객체 내 print method 정의
    - print method 실행 시 Vue instance의 data내 message 출력
- 콜솔창에서 app.print() 실행
    
    ```jsx
    // 2. el
        const app = new Vue({
          el: '#app',
          // 3. data
          data: {
            message: 'Hello, Vue!'
          },
    
          // 4. methods (s 조심!!!)
          methods: {
            print: function () {
              console.log(this.message)
            },
    ```
    
    ⇒ 여기서 this는  new Vue를 뜻함
    
- method를 호출하여 data 변경 가능
    - 객체 내 bye method 정의
    - print method 실행 시 Vue instance의 data내 message 변경
- 콘솔창에서 app.bye() 실행
    - DOM에 바로 변경된 결과 반영
    - Vue의 강력한 반응성(`reactivity`)
    
    ```jsx
          // 4. methods
          methods: {
            print: function () {
              console.log(this.message)
            },
    
            bye: function () {
              this.message = 'Bye, Vue!'
            },
    ```
    
    ⇒ this.message를 ‘Bye, Vue!’로 바꾸는 메서드
    
- `주의`
    - 메서드를 정의 할 때, Arrow Function을 사용하면 안됨
- Arrow Function의 this는 함수가 선언될 때 상위 스코프를 가리킴
- `this`가 상위 객체 `window를 가리킴`
- 호출은 문제 없이 가능하나 this로 Vue의 data를 반영하지 못함

## (3) Basic of Syntax

### 1. Template Syntax

- Vue2 guide > template syntax 참고
- `렌더링 된 DOM` 을 기본 Vue instance의 data에 `선언적으로 바인딩` 할 수 있는 HTML `기반 template syntax` 를 사용
    - 렌더링 된 DOM - 브라우저에 의해 보기 좋게 그려질 HTML 코드
    - HTML 기반 template syntax - HTML 코드에 직접 작성할 수 있는 문법 제공
    - 선언적으로 바인딩 - Vue instance와 DOM을 연결

### 2. Template Interpolation (`06번 파일`)

- 가장 기본적인 바인딩(연결) 방법
- 중괄호 2개로 표기
- DTL과 동일한 형태로 작성
- Template interpolation 방법은 HTML을 `일반 텍스트` 로 표현
    
    ```html
    <!-- 1. Text interpolation -->
      <div id="app">
        <p>메시지: {{ msg }}</p>   
        <p>HTML 메시지 : {{ rawHTML }}</p>    <!-- 이렇게 주면 span 안 먹힘 -->
        <p>HTML 메시지 : <span v-html="rawHTML"></span></p>
        <p>{{ msg.split('').reverse().join('') }}</p>
      </div>
    ```
    
    ```jsx
    	<script>
        // 1. Text interpolation
        const app = new Vue({
          el: '#app',
          data: {
            msg: 'Text interpolation',
            rawHTML: '<span style="color:red"> 빨간 글씨</span>'
          }
        })
    	</script>
    ```
    

### 3. RAW HTML

- `v-html` directive을 사용하여 data와 바인딩
- directive - HTML 기반 template syntax
- HTML의 기본 속성이 아닌 Vue가 제공하는 특수 속성의 값으로 data를 작성

## (4) Directives

### 1. 기본 구성

- v-접두사가 있는 특수 속성에는 값을 할당 할 수 있음
    - 값에는 JS 표현식을 작성 할 수 있음
- directive의 역할은 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 것

### 2. 새 Vue instance 생성 (`06번 파일`)

- instance들은 연결된 DOM element에만 영향을 미침
- 연결되지 않은 DOM이 Vue의 영향을 받지 않았던 것과 동일한 상황
    - 즉, 연동되지 않은 `div`는 작동에 영향을 끼치지 않는다.

### 3. v-text

- Template Interpolation과 함께 가장 기본적인 바인딩 방법
- `{{ }}` 와 역할 동일
    
    ```html
    	<div id="app2">
        <p v-text="message"></p>
        <p>{{ message }}</p>
      </div>
    ```
    
    ```jsx
    	<script>
    		const app2 = new Vue ({
    	      el: '#app2',
          data: {
            message: 'Hello!',
          }
        })
      </script>
    ```
    

### 4. v-html

- RAW HTML을 표현할 수 있는 방법
    
    단, `사용자`가 입력하거나 제공하는 `컨텐츠`에는 `절대 사용 금지`
    
    ```html
    	<div id="app2">
        <p v-html="html"></p>
      </div>
    ```
    
    ```jsx
    	<script>
    		const app2 = new Vue ({
    	      el: '#app2',
          data: {
    				html: '<a href=https://www.google.com">GOOGLE</a>'      }
        })
      </script>
    ```
    
    ![html.PNG](Vue%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%E1%84%86%E1%85%AE%E1%86%AB%E1%84%87%E1%85%A5%E1%86%B8%20600105762fa749128a06bcacaa4fe234/html.png)
    

### 5. v-show

- 표현식에 작성된 값에 따라 element를 보여 줄 것인지 결정
    - boolean  값이 변경 될 때 마다 반응
- 대상 element의 display 속성을 기본 속성과 none으로 toggle
- 요소 자체는 항상 DOM에 렌더링 됨
- 바인딩 된 `isActive의 값`이 `false`이므로 첫 방문 시 p tag는 `보이지 않음`
    - vue dev tools에서 isActive 변경 시 화면에 출력
    - 값을 false로 변경 시 다시 사라짐
- 화면에서만 사라졌을 뿐, DOM에는 존재
    - display 속성이 변경되었을 뿐
    
    ```html
    	<div id="app3">
        <p v-show="isActive">보이니? 안보이니?</p>
      </div>
    ```
    
    ```jsx
    	<script>
    		const app3 = new Vue ({
          el: '#app3',
          data: {
            isActive: false
          }
        })
      </script>
    ```
    
    - isActive : true
        
        ![true.PNG](Vue%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%E1%84%86%E1%85%AE%E1%86%AB%E1%84%87%E1%85%A5%E1%86%B8%20600105762fa749128a06bcacaa4fe234/true.png)
        
    - isActive: false
        
        ![false.PNG](Vue%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%E1%84%86%E1%85%AE%E1%86%AB%E1%84%87%E1%85%A5%E1%86%B8%20600105762fa749128a06bcacaa4fe234/false.png)
        
        ⇒ `화면상에는 안 보이지만 존재는 함!`
        

### 6.v-if

- v-show와 사용 방법은 동일하나, 값이 false일 경우 보이지 않는 게 아니라 DOM에서 사라짐
- v-if, v-else-if, v-else 형태로 사용
    
    ```html
    	<div id="app3">
        <p v-if="isActive">안보이니? 보이니?</p>
      </div>
    ```
    
    ```jsx
    	<script>
    		const app3 = new Vue ({
          el: '#app3',
          data: {
            isActive: false
          }
        })
      </script>
    ```
    
    - isActive : true
        
        ![true2.PNG](Vue%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%E1%84%86%E1%85%AE%E1%86%AB%E1%84%87%E1%85%A5%E1%86%B8%20600105762fa749128a06bcacaa4fe234/true2.png)
        
    - isActive : false
        
        ![false2.PNG](Vue%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%E1%84%86%E1%85%AE%E1%86%AB%E1%84%87%E1%85%A5%E1%86%B8%20600105762fa749128a06bcacaa4fe234/false2.png)
        
        ⇒ `v-show와 다르게 진짜 DOM에서 사라짐!!`
        

### 7. v-for (`07번 파일`)

- for - in - 형식으로 작성
- 반복한 데이터 타입에 모두 사용 가능
- index를 함께 출력하고자 한다면 (char, index) 형태로 사용 가능
- 배열 역시 문자열과 동일하게 사용 가능
- 각 요소가 객체라면 `dot notation`으로 접근 할 수 있음

```jsx
		<div v-for="(value, key) in myObj"  :key="key">
      <p>{{ key }} : {{ value }}</p>
    </div>
```

⇒ v-for 객체 내에서 `(value, key) 순서` 임을 주의!! 

⇒ v-for 사용 시 반드시 key 속성을 각 요소에 작성  ( `특수 속성 key`)

`<div v-for="(item, index) in myArr2" :key="arry-${index}">`

⇒ vue 화면 구성 시 이전과 달라진 점을 확인 하는 용도로 활용

⇒ key가 중복되어서는 안됨

- 객체 순회 시 value가 할당되어 출력
- 2번째 변수 할당 시 key 출력 가능

### 8. v-on (`8번 파일`)

- `:` 을 통해 전달받은 인자를 확인
    
    ⇒ 값으로 JS 표현식 작성
    
- addEventListener의 첫 번째 인자와 동일한 값들로 구성
- 대기하고 있던 이벤트가 발생하면 할당된 표현식 실행
- method를 통한 data 조작도 가능
- method에 인자를 넘기는 방법은 일반 함수를 호출할 때와 동일한 방식
- ‘:’을 통해 전달된 인자에 따라 특별한 modifiers (수식어)가 있을 수 있음
- `'@'` shortcut 제공

```html
@ => addEventListener
커멘드 =>커멘드
함수 => 함수

ex)
@click(function)
addEventListener('click',function)
```

### 9. v-bind

- HTML 기본 속성에 Vue data를 연결
- class의 경우 다양한 형태로 연결 가능
    - `조건부 바인딩`
        - { ’class Name’ : ’조건 표현식’ }
        - 삼항 연산자도 가능
    - `다중 바인딩`
        - [’JS 표현식’, ‘JS 표현식’, …]
    
    ****`<a v-bind:href="url">Go To GOOGLE</a>`****
    
    ⇒ 이런식으로 aTag가 바뀜
    
    ```jsx
    const app2 = new Vue({
          el: '#app2',
          data: {
            url: 'https://www.google.com/',
            redTextClass: 'red-text',
            borderBlack: 'border-black',
            isActive: true,
            theme: 'dark-mode'
          },
    ```
    
    ⇒ 이걸 지칭하는 것!
    
    ![캡처.PNG](Vue%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%E1%84%86%E1%85%AE%E1%86%AB%E1%84%87%E1%85%A5%E1%86%B8%20600105762fa749128a06bcacaa4fe234/%25EC%25BA%25A1%25EC%25B2%2598.png)
    
    ⇒ 이런식으로 출력됨
    
    ```jsx
    tip
    
    - v-on : `@` 로 축약
    - v-bind :  `:` 로 축약
    ```
    

### 10. v-model (`9번 파일`)

- Vue instance와 DOM의 `양방향 바인딩`
- Vue data 변경 시 v-model로 연결된 사용자 입력 element에도 적용

## (4) Vue advanced

### 1. computed(`10번 파일`)

- Vue instance가 가진 options 중 하나
- computed 객체에 정의한 함수를 페이지가 최초로 렌더링 될 때 호출하여 계산
    - 계산 결과가 변하기 전까지 함수를 재호출 하는 것이 아닌 계산된 값을 반환

### 2. method v.s computed

- method
    - 호출 될 때마다 함수를 실행
    - 같은 결과여도 매번 새롭게 계산
- computed
    - 함수의 종속 대상의 변화에 따라 계산 여부가 결정
    - 종속 대상이 변하지 않으면 항상 저장(캐싱)된 값을 반환

### 3. watch (`11번 파일`)

- 특정 데이터의 변화를 감지하는 기능
    1. watch 객체를 정의
    2. `감시`할 대상 data를 지정
    3. data가 변할 시 실행 할 함수를 정의
- 첫 번째 인자는 변동 전 data
- 두 번째 인자는 변동 후 data

### 4. filters(`12번 파일`)  ← computed와 watch로 대체                                                                                                가능

- 텍스트 형식화를 적용할 수 있는 필터
- interpolation 혹은 v-bind를 이용할 때 사용 가능
- 필터는 자바스크립트 표현식 마지막에 `'|'` (파이프)와 함께 추가되어야 함
- 이어서 사용(chaining) 가능

```jsx
<body>
  <div id="app">
    <p>{{ numbers }}</p>
    <p>{{ numbers | getOddNums}}</p>
    <p>{{ numbers | getUnderTenNums}}</p>
		<p>{{ numbers | getOddNums | getUnderTenNums}}</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
      },
      filters: {
        getOddNums: function (nums) {
          const oddNums = nums.filter((num) => {
            return num % 2
          })
          return oddNums
        },
        
        getUnderTenNums: function (nums) {
          const underTen = nums.filter((num) => {
            return num < 10
          })
          return underTen
        }
      }
    })
  </script>
</body>
```

1. 1~ 15까지의 모든 수를 출력
2. filter를 걸어줘서 홀수의 숫자만 출력할 수 있음
3. filter를 걸어줘서 10보다 작은 모든 숫자를 출력
4. 2번과 3번을 동시에 filter해줘서 10보다 작은 홀수를 출력한다.
    - 인자가 2개면 첫번째 인자를 먼저 실행하고 그 결과를 다시 2번쨰 인자에 넣어주는 식으로 진행

---

### Style Guide

- v-for는 항상 key와 같이 사용해라
- `v-for`를 쓴 `엘리먼트`에 `절대` `v-if`를 `사용하지 말아라`