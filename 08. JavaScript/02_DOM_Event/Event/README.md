# Event

# Event

## (1) 개요

- Event란 프로그래밍하고 있는 시스템에서 일어나는 사건 혹은 발생인데, 우리가 원한다면 그것들에 어떠한 방식으로 응답할 수 있도록 시스템이 말해주는 것
- 클릭 말고도 웹에서는 각양각색의 Event가 존재
    - 키보드 키 입력, 브라우저 닫기, 데이터 제출, 텍스트 복사 …

## (2) Intro

### 1. Event object

- 네트워크 활동이나 사용자와 의 상호작용 같은 사건의 발생을 알리기 위한 객체
- Event 발생
    - 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수 있음
    - 특정 메서드를 호출하여 프로그래밍적으로 만들어 낼 수 있음
- DOM 요소는 Event를 받고(`수신`)
- 받은 Event를 `처리` 할 수 있음
    - Event 처리는 주로 `addEventListener()` 라는 Event 처리기(`Event handler`)를 사용해 다양한 html 요소에 `부착` 하게 됨

### 2. Event handler

- `addEventListener()`
    - `대상` 에 `특정 Event` 가 발생하면 , `할 일` 을 등록하자
    - `EventTarget.addEventListener(type, listener[, options])`
        - 지정한 Event가 대상에 전달될 때마다 호출할 함수를 설정
        - Event를 지원하는 모든 객체를 대상(`EventTarget`)으로 지정 가능
        - `type`
            - 반응 할 Event 유형을 나타내는 대소문자 구분 문자열
            - 대표 이벤트 ⇒ input, click, submit …
        - `listener`
            - 지정된 타입의 Event를 수신할 객체
            - JavaScript function `객체(콜백 함수)`여야 함
                
                ⇒ 직접적으로 Event의 작동을 시켜야 하므로!!
                
            - 콜백 함수는 발생한 Event의 데이터를 가진 Event 기반 객체를 유일한 매개변수로 받음

## (3) Event 실습

### 1. button

- 버튼을 클릭하면 특정 변수 값 변경
    
    ```jsx
    	<script>
        const btn = document.querySelector('#btn')
        let countNum = 0
         //이벤트 핸들러 작성
        btn.addEventListener('click', function (event){
          //console.log(event)
          const pTag = document.querySelector('#counter')
          countNum += 1
          pTag.innerText = countNum
        })
      </script>
    ```
    

### 2. input

- input에 입력하면 입력 값을 실시간으로 출력하기
    
    ```jsx
    	<script>
        //1.input 선택
        const inputTag = document.querySelector('#text-input')
    
        //2.이벤트 핸들러 부착
        inputTag.addEventListener('input', function (event){
          // console.log(event)
          // event의 target = inputTag
          // inputTag의 value를 출력
          // console.log(event.target.value)
          // 따라서 event.target.value를 innerText에 넣어줌
    
          const pTag = document.querySelector('p')
          pTag.innerText = event.target.value
        })
      </script>
    ```
    

### 3. button_input

- input에 입력하면 입력 값을 실시간으로 출력하고 버튼을 클릭하면 출력된 값의 클래스를 토글하기
    
    ```jsx
    <script>
        const btn = document.querySelector('#btn')
        btn.addEventListener('click', function (event){
          const h1Tag = document.querySelector('h1')
          h1Tag.classList.toggle('blue')
        })
        const inputTag = document.querySelector('input')
        inputTag.addEventListener('input', function (event){
          const h1Tag = document.querySelector('h1')
          h1Tag.innerText = event.target.value
        })
      </script>
    ```
    

## (4) Event 취소

### 1. event.preventDefault()

- 현재 Event의 기본 동작을 중단
    
    ex) 복사 Event 막기
    
- HTML 요소의 기본 동작을 작동하지 않게 막음
- HTML 요소의 기본 동작 예시
    - a 태그: 클릭 시 특정 주소로 이동
    - form 태크 : form 데이터 전송

```jsx
<script>
  const h1Tag = document.querySelector('h1')
  h1Tag.addEventListener('copy', function (evnet){
    event.preventDefault()
    alert('복사 할 수 없지롱~')
  })
</script>
```

![Event취소.PNG](Event%207b40bb6c41474dc58e7511cab0f78bca/Event%25EC%25B7%25A8%25EC%2586%258C.png)

## (5) Event 종합 실습

1. Lotto
    
    ```jsx
    <script>
        const btn = document.querySelector('#lotto-btn')
        btn.addEventListener('click', function (event) {
    
          // 공이 들어갈 컨테이너 생성
          const ballContainer = document.createElement('div')
          ballContainer.classList.add('ball-container') // 하나 넣을 때는 add (toggle 대신)
    
          // 랜덤한 숫자 6개 만들기
          const numbers = _.sampleSize(_.range(1, 46), 6) // 1~46의 숫자 중 6숫자 뽑기 
          // console.log(numbers)
    
          // 공 만들기
          numbers.forEach((number) =>{
            const ball = document.createElement('div')
            ball.innerText = number
            ball.classList.add('ball')
            ball.style.backgroundColor = 'crimson'
            ballContainer.appendChild(ball)
          })
          // 공 컨테이너는 결과 영역의 자식으로 넣기
          const resultDiv = document.querySelector('#result')
          resultDiv.appendChild(ballContainer)
        })
      </script>
    ```
    
2. todo
    - CREATE, READ 기능을 충족하는 todo app 만들기
    
    ```jsx
    	<script>
        const formTag = document.querySelector('form')
    
        formTag.addEventListener('submit', function (event) {
          console.log(event)
          event.preventDefault()  // 주소가 안 바뀌게 해줌
    
          const inputTag = document.querySelector('.inputData')
          const data = inputTag.value
    
          if (data.trim()) {
          const liTag = document.createElement('li')
          liTag.innerText = data
    
          const ulTag = document.querySelector('ul')
          ulTag.appendChild(liTag)
          event.target.reset()    // 이렇게 하면 계속 입력해도 consol에는 저장 x
          } else{
            alert('내용을 입력하세요!')
          }
        })
    	</script>
    ```
    
    ```jsx
    // callback 함수가 너무 길어서 함수만 빼내기
    const addTodo = function (event) {
      console.log(event)
      event.preventDefault()  // 주소가 안 바뀌게 해줌
    
      const inputTag = document.querySelector('.inputData')
      const data = inputTag.value
    
      if (data.trim()) {
      const liTag = document.createElement('li')
      liTag.innerText = data
    
      const ulTag = document.querySelector('ul')
      ulTag.appendChild(liTag)
      event.target.reset()    // 이렇게 하면 계속 입력해도 consol에는 저장 x
      } else{
        alert('내용을 입력하세요!')
      }
    }
    formTag.addEventListener('submit', addTodo)
    
    ```