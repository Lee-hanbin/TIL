# ws

# JavaScript 기초

## 1. 제공된 HTML을 활용하여 a 태그의 속성을 수정하시오.

```html
<body>
  <a id="anchor" href="">GOOGLE</a>

  <script>
    /*
      JavaScript 코드만을 활용하여 a#anchor 요소를 아래와 같이 수정합니다.
        1) a 태그에 text-decoration-none 클래스를 추가합니다.
        2) a 태그의 href 속성은 https://google.com/ 입니다.
        3) a 태그의 target 속성은 _blank 입니다. (새 탭에서 열기)
    */

  </script>
</body>
```

- 답
    
    ```jsx
    aTag = document.querySelector('#anchor')
    aTag.setAttribute('class', 'text-decoration-none')
    aTag.setAttribute('href', 'https://google.com/')
    aTag.setAttribute('target', '_blank')
    ```
    
    - 교재 답
        
        ```jsx
        const anchor = document.querySelector('#anchor')
        anchor.classList.add('text-decoration-none')
        anchor.setAttribute('href', 'https://google.com')
        // anchor.href = 'https://google.com'
        anchor.setAttribute('target', '_blank')
        // anchor.target = '_blank'
        ```
        

## 2. 제공된 HTML을 수정하지 않고, JS만으로 주석을 참고하여 아래 사진과 같이 마크업을 추가하시오.

![ㅇㅊ.PNG](ws%20a97ec696527b4021a50736eb0ab1e583/%25E3%2585%2587%25E3%2585%258A.png)

```html
<body>

  <div id="app"></div>

  <script>
    // div#app 요소 선택
    
    // h1 태그를 createElement 로 생성

    // 생성한 h1태그의 내용을 '오늘의 Todo' 로 설정

    // ul, li 태그들을 생성 및 내용 추가

    // 각 태그들을 적절하기 div#app 요소에 자식요소로 추가. (#app > ul > li)

  </script>
</body>
```

- 답
    
    ```jsx
    // div#app 요소 선택
        const divTag = document.querySelector('#app')
        // h1 태그를 createElement 로 생성
        const h1Tag = document.createElement('h1') 
        // 생성한 h1태그의 내용을 '오늘의 Todo' 로 설정
        h1Tag.innerText = '오늘의 Todo'
        
        // ul, li 태그들을 생성 및 내용 추가
        const ulTag = document.createElement('ul')
        const liTag1 = document.createElement('li') 
        const liTag2 = document.createElement('li') 
        const liTag3 = document.createElement('li') 
        
        liTag1.innerText = '양치하기'
        liTag2.innerText = '공부하기'
        liTag3.innerText = '휴식하기'
        
        // 각 태그들을 적절하기 div#app 요소에 자식요소로 추가. (#app > ul > li)
        divTag.appendChild(h1Tag)
        divTag.appendChild(ulTag)
        ulTag.appendChild(liTag1)
        ulTag.appendChild(liTag2)
        ulTag.appendChild(liTag3)
    ```
    

## 3. 제공된 HTML 파일에서 예시로 주어진 Bootstrap Card 컴포넌트와 동일한 컴포넌트를 JS만으로 생성하시오. 최종 결과 화면은 아래와 같습니다.

![bc.PNG](ws%20a97ec696527b4021a50736eb0ab1e583/bc.png)

```html
<body>

  <div class="container">

    <section id="cardsSection" class="row">

      <!-- 카드 예시 -->
      <article class="col-4">
        <div class="card m-1">
          <div class="card-body">
            <h5 class="card-title">Example</h5>
            <p class="card-text">This is a card example.</p>
          </div>
        </div>
      </article>
      <!-- 카드 예시 -->

      <!-- JS로 위와 동일한 카드를 생성하여 section#cardSection의 자식으로 추가 -->
    </section>

  </div>

  <script>
    // section#cardSection에 예시와 같은 카드를 생성하여 추가하는 코드를 작성하시오.
    const cardsSection = document.querySelector('#cardsSection')
    
    function createCard(title, content) {
      // 여기에 카드를 작성하시오.
    }

    // 카드 생성
    const newCard = createCard('Hello', 'World')
    
    // DOM에 추가
    cardsSection.appendChild(newCard)

  </script>
</body>
```

- 답
    
    ```jsx
    function createCard(title, content) {
      // 여기에 카드를 작성하시오.
      const articleTag = document.createElement('article')
      articleTag.classList.add('col-4')
    
      const divTag1 = document.createElement('div')
      divTag1.classList.add('card', 'm-1')
    
      const divTag2 = document.createElement('div')
      divTag2.classList.add('card-body')
    
      const h5Tag = document.createElement('h5')
      h5Tag.classList.add('card-title')
    
      const pTag = document.createElement('p')
      pTag.classList.add('card-text')
      h5Tag.innerText = title
      pTag.innerText = content
    
      articleTag.appendChild(divTag1)
      divTag1.appendChild(divTag2)
      divTag2.appendChild(h5Tag)
      divTag2.appendChild(pTag)
    
      return articleTag
    }
    ```