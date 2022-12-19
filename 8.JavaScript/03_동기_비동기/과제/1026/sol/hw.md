# hw

# JavaScript 심화

## 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

```jsx
1. JavaScript는 single threaded 언어로 한 번에 한 가지 일 밖에 처리하지 못한다.
2. setTimeout은 브라우저의 Web API를 사용하는 함수로, Web API에서 동작이 완료되면 
	Call Stack에 바로 할당된다.
```

- 답
    
    ```jsx
    1. true
    2. false: Queue로 갔다가 Stack으로 할당된다.
    ```
    

## 2. JavaScript에서 동기와 비동기 함수의 차이점을 서술하시오.

- 답
    
    ```jsx
    동기 : 
    	- 모든 일을 순서대로 하나씩 처리
    	- 순서대로 처리한다 == 이전 작업이 끝나야 다음 작업을 시작
    
    비동기 :
    	- 작업을 시작한 후, 결과를 기다리지 않고 다음 작업을 처리하는 것 (병렬적 수행)
    	- 시간이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리
    ```
    
    - 교재 답
        
        ```jsx
        - 동기 함수
          - JavaScript는 single threaded 프로그래밍 언어로 한 번에 한 가지 일 밖에 하지 못한다.
          - 그래서 동기적으로 동작을 하면 해당 작업이 끝날때까지 다른 작업을 하지 못한다.
          - 예를 들면 알림창을 띄워 사용자에게 확인 버튼을 누르는 요청을 보낼 때 JavaScript interpreter는 다른 작업을 수행하지 못하고 멈춘채로 사용자의 입력이 완료될 때 까지 기다리게 될 것이다.
        - 비동기 함수
          - JavaScript는 비동기 함수를 만나면 해당 동작을 Web API에서 처리할 수 있도록 실행 주체를 넘겨준다.
          - 이렇게 실행 주체를 넘긴 다음에는 JavaScript는 동작이 완료될 때까지 기다리지 않고 바로 다음 코드를 실행한다.
          - Web API에서는 동작이 완료되었다면 해당 함수를 task queue로 할당하고 event loop는 현재 call stack을 바라보다가 call stack이 비워지면 비동기 함수의 콜백함수를 Web API에서 처리한 결과값과 함께 call stack으로 쌓아주고 JavaScript는 해당 call stack에 쌓인 콜백함수를 실행하게 된다.
        ```
        

### 3. 다음은 axios를 사용하여 API 서버로 요청을 보내고, 정상적으로 응답이 왔을 때 응답 데이터를 출력하는 코드이다. (a), (b), (c)에 들어갈 코드를 작성하시오.

```jsx
axios.__(a)__('https://api.example.com/data')
	.__(b)__(function (response) {
		console.log(__(c)__)
	})
```

- 답
    
    ```jsx
    a : get
    b : then
    c : response.data
    ```