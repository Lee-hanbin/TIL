# 문제 1.

1. `True`
2. `False`
   - Web API에서 동작이 완료된 이후 Task queue로 이동하게 된다. 
   - 이후 call stack이 모두 비워지게 되면 Event Loop를 통해서 call stack으로 할당된다.



# 문제 2.

1.  - 동기 함수
      - JavaScript는 single threaded 프로그래밍 언어로 한 번에 한 가지 일 밖에 하지 못한다. 
      - 그래서 동기적으로 동작을 하면 해당 작업이 끝날때까지 다른 작업을 하지 못한다. 
      - 예를 들면 알림창을 띄워 사용자에게 확인 버튼을 누르는 요청을 보낼 때 JavaScript interpreter는 다른 작업을 수행하지 못하고 멈춘채로 사용자의 입력이 완료될 때 까지 기다리게 될 것이다.
   - 비동기 함수
     - JavaScript는 비동기 함수를 만나면 해당 동작을 Web API에서 처리할 수 있도록 실행 주체를 넘겨준다. 
     - 이렇게 실행 주체를 넘긴 다음에는 JavaScript는 동작이 완료될 때까지 기다리지 않고 바로 다음 코드를 실행한다.
     - Web API에서는 동작이 완료되었다면 해당 함수를 task queue로 할당하고 event loop는 현재 call stack을 바라보다가 call stack이 비워지면 비동기 함수의 콜백함수를 Web API에서 처리한 결과값과 함께 call stack으로 쌓아주고 JavaScript는 해당 call stack에 쌓인 콜백함수를 실행하게 된다.

   

## 문제 3.

- (a): `get`

  (b): `then`

  (c): `response.data`

  

