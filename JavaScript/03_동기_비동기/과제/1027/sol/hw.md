# hw

# JavaScript 심화

## 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

```jsx
1. Event Loop는 Call Stack이 비워지면 Task Queue의 함수를 Call Stack으로 할당하는 역할을 한다.
2. XMLHttpRequest(XHR)는 AJAX 요청 instance를 생성하는 Web API이다. XHR객체를 활용하여 브라우저와
	서버 간의 네트워크 요청을 전송할 수 있다.
3. axios는 XHR을 보내고 응답 결과를 Promise 객체로 반환해주는 라이브러리이다.
```

- 답
    
    ```jsx
    1. true
    2. true
    3. true
    ```
    

## 2. 아래의 코드가 실행되었을 때 Web API, Task Queue, Call Stack 그리고 Event Loop에서 어떤 동작이 일어나는지 서술하시오.

```jsx
console.log('Hello SSAFY!')

setTimeout(function () {
	console.log('I am from setTimeout')
}, 1000)

console.log('Bye SSAFY!')
```

- 답
    
    ```jsx
    'Hello SSAFY!'
    => 'Bye SSAFY!'
    => 'I am from setTimeout'
    
    1. Call Stack에 'Hello SSAFY!'가 쌓이고 바로 Output
    2. setTimeout 함수 실행 => Call stack에 'I am from setTimeout' 이 쌓임
    	=> 1000ms가 걸리므로 WebAPI로 보냄
    3. Call stack에 'Bye SSAFY!'가 쌓이고 바로 Output
    4. WebAPI에서 동작이 끝난 'I am from setTimeout'는 Task Queue에 들어가서 Call Stack이
    	비어있을 때, Call Stack에서 실행하여 바로 Output으로 나감
    ```