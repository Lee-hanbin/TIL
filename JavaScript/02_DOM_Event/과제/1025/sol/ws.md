# ws

# JavaScript 기초

## 1. 제공된 html 파일을 활용하여 실시간 메시지 필터링 기능을 완성하시오.

![바보.PNG](ws%20a740a83205054164befbed5fd240554f/%25EB%25B0%2594%25EB%25B3%25B4.png)

```jsx
<body>
  <div>
    Input: <input id="userInput" type="text" autofocus>
  </div>
  <div>
    Output: <span id="output"></span>
  </div>

  <script>
    /* 
      현재 코드에서는 input#userInput에 입력한 내용이 그대로 span#output에 출력된다.
      아래 이미지를 참고하여 badWords에 포함된 단어가 사용자 입력에 포함되어 있을 경우,
      span#output에서 해당 단어를 '**' 로 바꿔 출력하도록 filterMessage 함수를 완성하시오.
      replaceAll 메서드를 검색 후 활용할 수 있습니다.
    */
    const badWords = ['바보', '멍청', '메롱',]
    const userInput = document.querySelector('#userInput')
    const output = document.querySelector('#output')

    function filterMessage(event) {
      let filteredInput = event.target.value
      // badWords에 포함된 단어가 입력될 경우, '**'으로 변환하여 output에 출력 
      output.innerText = filteredInput
    }
    userInput.addEventListener('input', filterMessage)   
  </script>
</body>
```

- 답
    
    ```jsx
        function filterMessage(event) {
          let filteredInput = event.target.value
          // badWords에 포함된 단어가 입력될 경우, '**'으로 변환하여 output에 출력 
    			for (const i of badWords){
    			        filteredInput = filteredInput.replaceAll(i,'**')
    			      }
    			      output.innerText = filteredInput
        }
    
    ```
    
    - replaceAll 을 통해 모든 인자를 대체할 수 있음

## 2. 제공된 html 파일을 활용하여 실시간 Bootstrap 카드 생성페이지를 완성하시오.

![카드.PNG](ws%20a740a83205054164befbed5fd240554f/%25EC%25B9%25B4%25EB%2593%259C.png)

```html
<body>

  <div class="container">

    <form id="form" class="my-3">
      <div class="mb-3">
        <input type="text" class="form-control" id="title">
      </div>
      <div class="mb-3">
        <textarea class="form-control" id="content" rows="3"></textarea>
      </div>
      <div class="d-grid gap-2">
        <button class="btn btn-primary">add</button>
      </div>
    </form>

    <section id="cardsSection" class="row">

      <!-- 카드 예시 -->
      <article class="col-4">
        <div class="card m-1">
          <div class="card-body">
            <h5 class="card-title">Example</h5>
            <p class="card-text">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Deleniti placeat odit rerum
              asperiores beatae vitae doloremque consectetur magni delectus, fuga autem laudantium, quidem iusto
              voluptates non earum dolorem totam dolores.</p>
          </div>
        </div>
      </article>
      <!-- 카드 예시 -->

    </section>

  </div>

  <script>
    /*
      사용자가 form 에 title과 content를 입력하고 submit하면, 예시와 같은 카드를 생성하여 div#cardSection에 추가하는 코드를 작성하시오.
      카드가 생성되면 기존에 입력된 input과 textarea의 내용은 삭제되어야 합니다.
      (완성 이후 카드 예시는 삭제)
    */

  </script>
</body>
```

- 답
    
    ```jsx
    const form = document.querySelector('#form')
    const cardsSection = document.querySelector('#cardsSection')
    
    function createCard(title, content) {
      const article = document.createElement('article')
      article.classList.add('col-4')
    
      const card = document.createElement('div')
      card.classList.add('card', 'm-1')
    
      const cardBody = document.createElement('div')
      cardBody.classList.add('card-body')
    
      const cardTitle = document.createElement('h5')
      cardTitle.classList.add('card-title')
      cardTitle.innerText = title
    
      const cardText = document.createElement('p')
      cardText.classList.add('card-text')
      cardText.innerText = content
    
      cardBody.appendChild(cardTitle)
      cardBody.appendChild(cardText)
      card.appendChild(cardBody)
      article.appendChild(card)
    
      return article
    }
    
    form.addEventListener('submit', function (event) {
      event.preventDefault()
    
      const title = document.querySelector('#title')
      const content = document.querySelector('#content')
    
      if (title.value.trim() && content.value.trim()) {
        const newCard = createCard(title.value, content.value)
        cardsSection.appendChild(newCard)
    
        title.value = ''
        content.value = ''
      } else {
        alert('내용을 입력하세요.')
      }
    
    })
    ```
    
    - **`trim()`**
     메서드는 문자열 양 끝의 공백을 제거합니다. 공백이란 모든 공백문자(space, tab, NBSP 등)와 모든 개행문자(LF, CR 등)를 의미합니다.

## 3. 제공된 html 파일을 활용하여 todo 생성/조회 페이지를 완성하시오.

![밥먹기.PNG](ws%20a740a83205054164befbed5fd240554f/%25EB%25B0%25A5%25EB%25A8%25B9%25EA%25B8%25B0.png)

```html
<body>
  <form action="/todos/">
    <input type="text">
    <button>Add</button>
  </form>
  <ul></ul>

  <script>
    /*
    [필수사항]	
      form에서 submit 이벤트가 발생되었을 때 input에 작성된 값이 todo로 추가된다.
      todo는 ul 태그의 li 태그로 추가된다.
      todo가 추가된 후 input value의 값은 초기화 된다.
      
      (선택) 빈 값인 데이터는 입력을 방지한다.
      빈 값이면 알림창을 띄워 값을 입력하도록 안내한다.
    */

  </script>
</body>
```

- 답
    
    ```jsx
    <script>
      const form = document.querySelector('form')
    
      function addTodo() {
        // form의 submit 기본 동작을 취소
        event.preventDefault()
    
        // input 요소를 선택하고, value 값을 새 변수에 할당
        const input = document.querySelector('input')
        const content = input.value
    
        // 선택 : 빈 값을 허용하지 않음.
        if (content.trim()) {
    
          // 새로운 li 요소를 생성하고, input value를 innerText로 지정
          const li = document.createElement('li')
          li.innerText = content
    
          // ul 요소를 선택하고, li 요소를 자식요소로 추가
          const ul = document.querySelector('ul')
          ul.appendChild(li)
    
          // input 요소의 value 값을 초기화
          event.target.reset()
    
          // 선택 : 빈 값 입력시 alert 창 출력
        } else {
          alert('할 일을 입력해주세요.')
        }
      }
    
      // submit 되었을 때 addTodo 함수를 실행
      form.addEventListener('submit', addTodo)
    </script>
    ```