# hw

# JavaScript 기초

## 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

```jsx
1. EventTarget.addEventListener(type, listener)에서 listener 위치에 콜백 함수를 정의한다.
	이때, 콜백 함수의 첫 번째 매개변수에는 발생한 이벤트에 대한 정보를 담고 있는 Event 객체가 전달된다.
2. event.preventDefault 메서드를 통해 이벤트의 기본 동작을 취소할 수 있다.
```

- 답
    
    ```jsx
    1. true
    2. true
    ```
    

## 2. DOM Event에는 다양한 종류의 Event가 존재한다. 아래 제시된 Event들이 각각 어떤 시점에 발생하는지 MDN 문서를 참고하여 간단하게 작성하시오.

```jsx
click, mouseover, mouseout, keydown, keyup, load, scroll, change, input
```

- 답
    1. `click`
        
        ```jsx
        포인팅 장치 버튼(모든 버튼; 주 버튼만 해당될 예정)이 엘리먼트에서 눌렸다가 놓였을 때.
        ```
        
    2. `mouseover`
        
        ```jsx
        포인팅 장치가 리스너가 등록된 엘리먼트나 그 자식 엘리먼트의 위로 이동했을 때.
        ```
        
    3. `mouseout`
        
        ```jsx
        포인팅 장치가 리스너가 등록된 엘리먼트 또는 그 자식 엘리먼트의 밖으로 이동했을 때.
        ```
        
    4. `keydown`
        
        ```jsx
        키가 눌렸을 때
        ```
        
    5. `keyup`
        
        ```jsx
        키 누름이 해제될 때
        ```
        
    6. `load`
        
        ```jsx
        - 진행이 성공했을 때.
        
        Ex) 이미지가 전부 로딩되었을 때
        ```
        
    7. `scroll`
        
        ```jsx
        다큐먼트 뷰나 엘리먼트가 스크롤되었을 때.
        ```
        
    8. `change`
        
        ```jsx
        - input, select, textarea 등 사용자 입력에 인해 요소의 값이 바뀌었을 때.
        
        - input 이벤트와 달리 요소 값이 변경 될 때마다 반드시 발생하는 것은 아님
        ```
        
    9. `input`
        
        ```jsx
        `<input>`, `<select>` 및 `<textarea>` 요소의 value 속성이 바뀔 때마다 발생
        ```
        

## 3. 다음은 버튼을 클릭했을 때, 콘솔창을 통해 메세지를 확인하는 코드이다. (a), (b), (c)에 들어갈 코드를 작성하시오.

```jsx
const button = document.__(a)__('button')

botton.__(b)__(__(c)__, function () {
	console.log('Button clicked!')
})
```

- 답
    
    ```jsx
    a : querySelector
    b : addEventListener
    c : 'click'
    ```