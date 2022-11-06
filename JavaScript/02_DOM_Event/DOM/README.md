# DOM

# DOM

## (1) 개요

- Browser APIs의 한 종류
    - 웹 브라우저에 내장된 API로, 현재 컴퓨터 환경에 관한 데이터를 제공하거나 여러가지 유용하고 복잡한 일을 수행

## (2) 정의

- 문서 객체 모델 (`Document Object Model`)
- 문서의 구조화된 표현을 제공하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공
    - 문서 구조, 스타일, 내용 등을 변경할 수 있게 도움
    - HTML 콘텐츠를 추가, 제거, 변경하고, 동적으로 페이지에 스타일을 추가하는 등 HTML/CSS를 조작할 수 있음
- 문서가 구조화되어 있으며 각 요소는 `객체(object)`로 취급
- 단순한 속성 접근, 메서드 활용 뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
- DOM은 문서를 `논리 트리` 로 표현
- DOM 메서드는 사용하면 프로그래밍적으로 트리에 접근할 수 있고 이를 통해 문서의 구조, 스타일, 컨텐츠를 변경할 수 있음
- 웹 페이지는 일종의 문서로 이 문서는 웹 브라우저를 통해 그 내용이 해석되어 웹 브라우저 화면에 나타나거나 HTML 코드 자체로 나타나기도 함
- DOM은 `동일한 문서`를 `표현하고 저장하고, 조작하는 방법`을 `제공`
- DOM은 `웹 페이지`의 `객체 지향 표현` 이며, JavaScript와 같은 스크립트 언어를 이용해 DOM을 수정할 수 있음

## (3) DOM 접근

- DOM을 사용하기 위해 특별히 해야 할 일은 없음
- 모든 웹 브라우저는 스크립트가 언어가 접근 할 수 있는 웹페이지를 만들기 위해 DOM을 항상 사용
- `DOM의 주요 객체` 들을 `활용` 하여 문서를 조작하거나 특정 요소들을 얻을 수 있음
    1. `window`
    2. `document`

### 1. window object

- DOM을 표현하는 창
- 가장 최상위 객체 (작성 시 생략 가능)
- 탭 기능이 있는 브라우저에서는 각각의 탭을 각각의 window 객체로 나타냄
- 메서드 예시
    - 새 탭 열기
        - `window.open()`
    - 인쇄 대화 상자 표시
        - `window.print()`
    - 경고 대화 상자 표시
        - `window.alter()`

### 2. documet object

- 브라우저가 불러온 웹 페이지
- `페이지 컨텐츠의 진입점 역할`을 하며, <body>등과 같은 수많은 다른 요소들을 포함
- 예시
    - `document` 로 사용 (원래 `window.document` 인데 window 생략 가능)
    - document.title
        
        ![title.PNG](DOM%202eb204be91eb444181b9ae58e6a39284/title.png)
        

## (4) DOM 조작

### 1. 개요

- Document가 제공하는 기능을 사용해 웹 페이지 문서 조작하기
- DOM 조작 순서
    1. 선택(Select)
    2. 조작(Manipulation)
        - 생성, 추가, 삭제

### 2. 선택 관련 메서드

- `document.querySelector(selector)`
    - 제공한 선택자와 일치하는 element 한 개 선택
    - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환
        - 없으면 null 반환
- `document.querySelectorAll(selector)`
    - 제공한 선택자와 일치하는 여러 element를 선택
    - 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
    - 제공한 CSS selector를 만족하는 NodeList를 반환
- 실습
    
    ```html
    	<h1 id="title">DOM 조작</h1>
      <p class="text">querySelector</p>
      <p class="text">querySelectorAll</p>
    	<ul>
        <li>Javascript</li>
        <li>Python</li>
      </ul>
    ```
    
    ```jsx
    		// #은 id 선택자
        console.log(document.querySelector('#title'))
        // .은 class 선택자
        console.log(document.querySelectorAll('.text'))
        // 단일 선택으로 class 선택해보기 (class의 첫번째 요소만 출력됨)
        console.log(document.querySelector('.text'))
    		// ul list들을 출력하고 싶음
        console.log(document.querySelectorAll('ul > li'))
    
    		// NodeList는 foreach문 지원
        listTag = document.querySelectorAll('body > ul > li')
        listTag.forEach(element => {
          console.log(element)
        })
    ```
    

### 3. 조작 관련 메서드

- 생성
    - `document.createElement(tagName)`
        - 작성한 tagName의 HTML 요소를 생성하여 반환
- 입력
    - `Node.innerText`
        - Node 객체와 그 자손의 텍스트 컨텐츠를 표현
        - 사람이 읽을 수 있는 요소만 남김
        - 즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현
- 추가
    - `Node.appendChild()`
        - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
        - 한번에 오직 하나의 Node만 추가할 수 있음
        - 추가된 Node 객체를 반환
        - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 현재 위치에서 새로운 위치로 이동
- 삭제
    - `Node.removeChild()`
        - DOM에서 자식 Node를 제거
        - 제거된 Node를 반환
        
        ⇒ `div에 넣기 위해 먼저 선택하는 것이 핵심!!!`
        

⇒ 실습

- 웹에 바로 작성

![웹에 바로 작성.PNG](DOM%202eb204be91eb444181b9ae58e6a39284/%25EC%259B%25B9%25EC%2597%2590_%25EB%25B0%2594%25EB%25A1%259C_%25EC%259E%2591%25EC%2584%25B1.png)

- script에서 작성

```jsx
  <div></div>
  <script>
    // 태그 생성
    const h1Tag = document.createElement('h1')
    // 텍스트 추가
    h1Tag.innerText = 'DOM 조작'
    // 선택자로 div 태그를 가져옴
    const div = document.querySelector('div')
    // div 태그의 자식 요소로 추가
    div.appendChild(h1Tag)
    // div의 h1 요소 삭제
    div.removeChild(h1Tag)
  </script>
```

- 속성 조회 및 설정
    - `Element.getAttribute(attributeName)`
        - 해당 요소의 지정된 값(문자열)을 반환
        - 인자는 값을 얻고자 하는 속성의 이름
    - `Element.setAttribute(name, value)`
        - 지정된 요소의 값을 설정
        - 속성이 이미 존재하면 값을 `갱신`
            - 존재하지 않으면 지정된 이름과 값으로 `새 속성을 추가`

⇒ 실습

- a 태그를 생성해서 구글 주소 넣기
    
    ![태그생성.PNG](DOM%202eb204be91eb444181b9ae58e6a39284/%25ED%2583%259C%25EA%25B7%25B8%25EC%2583%259D%25EC%2584%25B1.png)
    
- a태그의 이름 생성
    
    ![div에 넣기.PNG](DOM%202eb204be91eb444181b9ae58e6a39284/div%25EC%2597%2590_%25EB%2584%25A3%25EA%25B8%25B0.png)
    
- 속성 변경
    
    ![속성변경.PNG](DOM%202eb204be91eb444181b9ae58e6a39284/%25EC%2586%258D%25EC%2584%25B1%25EB%25B3%2580%25EA%25B2%25BD.png)
    
    ⇒ toggle은 클래스가 해당 값을 가지고 있으면 수정하고 아니면 추가
    
    ⇒ 사실상 blue로 변경하는 것이 아니라 list 뒤에 blue를 추가하여 blue가 적용
    

# `TIP`

## 1. 파싱

- 구문 분석, 해석
- 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정