## 문제 1.

- True
- True
- True



## 문제 2.

```
Hello SSAFY!가 출력된다

setTimeout 함수가 실행된다. 
해당 함수는 non-blocking 하기 때문에 바로 모든 동작을 Web API에게 위임한다.

Bye SSAFY!가 출력된다.

Web API는 비동기적으로 1초를 카운트한다.
1초 후 setTimeout 함수 내의 callback 함수를 task queue로 옮긴다.
Event loop에서 console.log('Bye SSAFY!') 까지 동작이 끝나고
call stack이 비워지게 되면 task queue에 있는 함수를 call stack으로 옮긴다.
JS는 call stack에 실행할 함수가 생겼기 때문에 해당 함수를 실행하고 'I am from setTimeout'을 출력하고 동작을 종료한다.
```
