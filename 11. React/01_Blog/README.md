# BLOG

# BLOG 만들기

## 1. 상단바 만들기

- 왜 .html 아닌데 html 작성가능 ?
    
    ⇒ JSX라는 .js파일에서 쓰는 html 대용품 사용 ( 더 간단하게 이용가능 )
    
- JSX 안에서는 style 적용하기 위한 class 를 정의할때,
    
    `<div class='클래스명'> </div>` 가 아닌 `<div className='클래스명'> </div>`
    
- 변수 정의하고 `{변수명}` 하면 어디서든 변수의 값을 출력가능
- style을 변수로 넣고 싶으면 Object 형태로 넣어줘야함
    
    ⇒ `<h4 style={ {color : 'red', fontSize: '16px'} }>블로그지롱</h4>` 
    
    ⇒ 이런식으로 { } 안에 `{ style속성 }` 을 넣어줘야 함
    

## 2. 글 목록 만들기

- State를 이용해서 자료 저장하기
    
    `let [a, b] = useState('남자 코트 추천');`
    
    ⇒  a: state에 담은 자료
    
    ⇒  b: state 변경을 도와주는 함수
    
    - 굳이 왜 변수 정의해서 안 쓰고 `State` 를 쓸까?
        
        ⇒ 중간에 변수를 변경해야하는 경우, 써뒀던 모든 변수를 다 수정해줘야 함
        
        ⇒ State를 사용하면 a부분만 바꿔주면 `자동`으로 `재렌더링` 됨
        
        ⇒ 자주 변경이 되는 자료에 한해서 사용!
        
- `/* eslint-disable */`  : Lint 끄는 기능

## 3. 좋아요 버튼 만들기

- onClick 이벤트에서는 인자로 함수로 받는다
    
    ```jsx
    function 함수(){
        console.log(1);
    }
    
    <h4>{ 글제목[0] } <span onClick={ 함수 }>👍</span> { 따봉 } </h4>
    ```
    
    ⇒ 
    
    ```jsx
    <h4>{ 글제목[0] } <span onClick={ () => {
              console.log(1)
            } }>👍</span> { 따봉 } </h4>
    ```
    
- State는 두번째 요소를 변경해야 변경가능
    
    ```jsx
    let [따봉, 따봉변경] = useState(0);
    
    <h4>{ 글제목[0] } <span onClick={ () => {
      따봉변경(따봉+1)
    } }>👍</span> { 따봉 } </h4>
    ```
    

## 4. 클릭버튼으로 데이터 수정

- 버튼 클릭하면 글제목 변경
    
    ```jsx
    let [글제목, 글제목변경] = useState(['남자 코트 추천', '강남 우동맛집', '파이썬독학']);
    
    <button onClick={ () => {
      글제목[0] = '여자 코트 추천'        
      글제목변경(글제목)
    }}>글수정</button>
    ```
    
    ⇒ 원본 자료 변경되므로 비추
    
- 원본 자료를 복제해서 글제목 변경
    
    ```jsx
    <button onClick={ () => {
      let copy = [...글제목];
      copy[0] = '여자 코트 추천'
      글제목변경(copy)
    }}>글수정</button>
    ```
    
    ⇒ `let` 은  Array를 의미하고 변경을 불가하는 생성자.
    
    ⇒ `[…글제목]` 을 통해서 copy 가능
    
    ⇒ `...` 은 괄호를 벗겨라
    
    ⇒ `[...글제목]` : 괄호를 벗기고 수정해서 괄호를 다시 씌어라
    

## 5. Component 문법

### 1) 컴포넌트는 언제 만드는 게 좋을까?

- 반복적인 html을 축약할 때
- 큰 페이지들
- 자주 변경되는 것들

### 2) 예시

- 일반적
    
    ```jsx
    function App() {
      return (
        <div className="App">
    
    			<div className='modal'>
    			  <h4>제목</h4>
    			  <p>날짜</p>
    			  <p>상세내용</p>
    			</div>
    		</div>
      );
    }
    ```
    
- 컴포넌트 사용
    
    ```jsx
    function App() {
      return (
        <div className="App">
    			<Modal/>
    		</div>
      );
    }
    
    function Modal(){
      return (
        <div className='modal'>
          <h4>제목</h4>
          <p>날짜</p>
          <p>상세내용</p>
        </div>
      )
    }
    ```
    
    ```jsx
    function Modal(){
      return (
        <div className='modal'>
          <h4>제목</h4>
          <p>날짜</p>
          <p>상세내용</p>
        </div>
      )
    }
    ```
    
    ```jsx
    // 화살표 함수 이용
    const Modal = ()=> {
      return (
        <div className='modal'>
          <h4>제목</h4>
          <p>날짜</p>
          <p>상세내용</p>
        </div>
      )
    }
    ```
    

### 3) 주의

- 컴포넌트를 쓸 때, 변수를 상속하는데 어려움이 있으므로 무조건 컴포넌트로 만들지말자

## 6. 동적인 UI 만드는 법

### 1) 3 - step

- html css로 미리 디자인 완성
- UI의 현재 상태를 state로 저장
- state에 따라 UI가 어떻게 보일지 작성

### 2) html css로 미리 디자인 완성

```jsx
function Modal(){
  return (
    <div className='modal'>
      <h4>제목</h4>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  )
}
```

### 3) UI의 현재 상태를 state로 저장

```jsx
function App() {
	let [modal, setModal] = useState(false);
  return (
  );
}

function Modal(){
  return (
    <div className='modal'>
      <h4>제목</h4>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  )
```

### 4) state에 따라 UI가 어떻게 보일지 작성

```jsx
{/* {}는 html 코드를 작성하는 영역이므로 if문을 사용 x => 삼항연상자 사용
    삼항연산자 => ' 조건식 ? 참일때 실행할 코드 : 거짓일 때 실행할 코드 '
*/}

function App() {
	let [modal, setModal] = useState(false);
  return (
    <div className="App">
			{
        modal == true ? <Modal/> : null
      }
		</div>
  );
}

function Modal(){
  return (
    <div className='modal'>
      <h4>제목</h4>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  )
```

## 7. 반복문으로 같은 html 반복 생성하기 (`map`)

- map 예시
    
    ```jsx
    // 1. array의 개수만큼 함수안의 코드를 실행
    // 2. 함수의 파라미터는 array안에 있던 자료임
    // 3. return에 무엇을 적으면 array로 담아줌
    {
      [1,2,3].map( () => {
        return <div>안녕</div>
      })
    }
    // {} 안에서는 for문을 사용할 수 없음!!!!
    ```
    
    ![Untitled](BLOG%20bfd744ff412848cb96c368d5ab9fb678/Untitled.png)
    
- 반복문으로 반복되는 html 작성
    
    ```jsx
    
    let [글제목, 글제목변경] = useState(['남자 코트 추천', '강남 우동맛집', '파이썬독학']);
    
    {
        글제목.map( (article, idx) => {
          return (
            <div className="list">
              <h4>{ article }</h4>
              <h4>{ 글제목[idx] }</h4>
              <p>2월 17일 발행</p>
            </div>
          )
        })
      }
    ```
    
    - 결과
        
        ![Untitled](BLOG%20bfd744ff412848cb96c368d5ab9fb678/Untitled%201.png)
        
- 각각의 글마다 좋아요 다르게 넣기
    
    ```jsx
    let [따봉, 따봉변경] = useState([0,0,0]);
    
    {
      글제목.map( (article, idx) => {
        return (
        <div className="list">
          <h4 onClick={() => {
              setModal(true);
          }}>{ 글제목[idx] } <span onClick={ (e) => {
    				e.stopPropagation();     // e.stopPropagation 누르면 모달창은 안뜬다.
    																// 원래는 따봉만 눌러도 상위 이벤트인 모달창이 뜸!!
            let tmp_따봉 = [...따봉]
            tmp_따봉[idx] += 1;
            따봉변경(tmp_따봉)
          } }>👍</span> { 따봉[idx] } </h4>
          <p>2월 17일 발행</p>
        </div>
        )
      })
    }
    ```
    
    ⇒ 따봉[idx]를 그대로 바꿔서 넣는 것이 아니라 copy해서 넣고 state 변수를 재정의 해주는 것이 핵심!
    

## 8. props

### 1) 부모 → 자식 state 전송하려면 props 문법 쓰면 됨! (2단계)

- `<자식컴포넌트 작명={state이름}>`
    
    ⇒  보통 작명과 state이름을 동일하게 쓰기 마련
    
- props 파라미터 등록 후 `props.작명` 을 사용

### 2) 예시

- 예시
    
    ```jsx
    {
      modal == false ? <Modal 글제목={글제목}/> : null
    }
    
    function Modal(props){
      return (
        <div className='modal'>
          <h4>{props.글제목[0]}</h4>
          <p>날짜</p>
          <p>상세내용</p>
        </div>
      )
    }
    ```
    

### 3) 컴포넌트를 쓰면 좋지만, props과정이 귀찮아질 수 있음

### 4) 같은 컴포넌트에 props를 할때, 특정 행동만 바꾸고 싶으면 props하는 과정에서 parameter를 더 넘겨주면 된다.

```jsx

{
  modal == false ? <Modal color={'blue'} 글제목={글제목}/> : null
}

function Modal(props){
  return (
    <div className='modal' style={{ background : props.color }}>
      <h4>{props.글제목[0]}</h4>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  )
}
```

### 5) 응용

- prorps를 이용하여 함수도 상속하여 글 제목을 변경해보자
    
    ```jsx
    function App() {
    	let [글제목, 글제목변경] = useState(['남자 코트 추천', '강남 우동맛집', '파이썬독학']);
    	return (
    		<div className="App">
    			{
            modal == false ? <Modal color={'blue'} 글제목={글제목} 글제목변경={글제목변경}/> : null
          }
    		</div>
      );
    }
    
    function Modal(props){
      return (
        <div className='modal' style={{ background : props.color }}>
          <h4>{props.글제목[0]}</h4>
          <p>날짜</p>
          <p>상세내용</p>
          <button onClick={ () => {
            let tmp_글제목 = [...props.글제목]
            tmp_글제목[0] = '여자 코트 추천'
            props.글제목변경(tmp_글제목)
          }} >글수정</button>
        </div>
      )
    }
    ```
    
    - 결과
        
        ![Untitled](BLOG%20bfd744ff412848cb96c368d5ab9fb678/Untitled%202.png)
        

## 9. 사용자가 입력한 글 다루기

### 1) input 태그

```jsx
<input type="text"/>
<input type="range"/>
<input type="checkbox"/>
<select/>
<textarea/>
```

## 2) input Option

```jsx
<input onChange={() => {} }/>
<input onInput={ () => {} }/>
<input onMouseOver={() => {} }/>
<input onScroll={() => {}}/>
```

⇒ 30여개의 옵션이 있음!!!

## 3) input tag에 적힌 값 가져오기

```jsx
<input onChange={(e) => { console.log(e.target.value ) }}/>
```

- 결과
    
    ![Untitled](BLOG%20bfd744ff412848cb96c368d5ab9fb678/Untitled%203.png)
    

## 10 . 글 생성, 삭제

### 1) 글 생성

```jsx
let [글제목, 글제목변경] = useState(['남자 코트 추천', '강남 우동맛집', '파이썬독학']);
let [입력값, 입력값변경] = useState('');

<input onChange={(e) => { 
    입력값변경(e.target.value );
  }}/>
  <button onClick={() =>{
    let tmp_글제목 = [...글제목];
    tmp_글제목.unshift(입력값);   // 제일 앞에 추가
    // tmp_글제목.push(입력값);   // 제일 뒤에 추가
    글제목변경(tmp_글제목);
  }}>글 발행</button>
</div>
```

### 2) 글 삭제

```jsx
{
  글제목.map( (article, idx) => {
    return (
    <div className="list" key={idx}>
      <h4 onClick={() => {
        setModal(true);
        idx_func(idx);
      }}>{ article } <span onClick={ (e) => {
        e.stopPropagation();
        let tmp_따봉 = [...따봉];
        tmp_따봉[idx] += 1;
        따봉변경(tmp_따봉)
      } }>👍</span> { 따봉[idx] } </h4>
      <p>2월 17일 발행</p>

      {/* 이렇게 하면 동일한 글도 모두 지워짐 ㅠ */}
      {/* <button onClick={() => {
        let copy = []
        for ( const 글 of 글제목){
          if (article === 글){
            continue
          } else {
            copy.push(글)
          }
        }
        글제목변경(copy)
      }}>delete</button> */}

      <button onClick={() => {
        let copy = [...글제목];
        copy.splice(idx, 1);
        글제목변경(copy)
      }}>delete</button>

    </div>
    )
  })
}
```