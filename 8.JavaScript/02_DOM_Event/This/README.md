# This

# this

## (1) 개요

- 어떠한 object를 가리키는 키워드 ( python에서의 self)
- JS의 함수는 `호출될 때` this를 암묵적으로 `전달 받음`
    
    ⇒ 어디서 선언 됐는지 알 필요 없음!!
    
- JS에서의 this는 일반적인 프로그래밍 언어에서의 this와 조금 다르게 동작
- JS는 해당 `함수 호출 방식` 에 따라 this에 바인딩 되는 객체가 달라짐
- 함수를 선언할 때 this에 객체가 결정되는 것이 아니고, 함수 호출할 때 `함수가 어떻게 호출 되었는지에 따라 동적으로 결정`

## (2) this INDEX

1. 전역 문맥에서의 this
2. 함수 문맥에서의 this (`이게 중요`)
    - 단순 호출
    - Method(객체의 메서드로서)
    - Nested

## (3) 함수의 문맥에서의 this

- 브라우저의 전역 객체인 window를 가리킴
    - 전역 객체는 모든 객체의 유일한 최상위 객체를 의미
        
        `console.log(this)` (window)
        
- 함수의 this 키워드는 다른 언어와 조금 다르게 동작
    - this의 값은 `함수를 호출한 방법에 의해 결정`
    - 함수 내부에서 this의 값은 함수를 호출한 방법에 의해 좌우
1. 단순 호출
    - 전역 객체를 가리킴
    - 전역은 브라우저에서는 window, Node.js는 global을 의미
2. Method(Function in Onject, 객체의 메서드로서)
    - 메서드로 선언하고 호출한다면, 객체의 메서드이므로 해당 객체가 바인딩
        
        ```jsx
        const myObj = {
        	data: 1
        	myFunc() {
        		console.log(this) //myObj
        		console.log(this.data) // 1
        	}
        }
        
        myObj.myFunc() //myObj
        ```
        
        ⇒  `this가 누구를 가리키는 키워드 인지`를 확인!!
        
3. Nested (Function 키워드)
    - forEach의 콜백 함수에서의 this가 메서드의 객체를 가리키지 못하고 전역 객체 window를 가리킴
    - 단순 호출 방식으로 사용되었기 때문
    - 이를 해결하기 위해 등장한 함수 표현식이 바로 `화살표 함수`
    
    ```jsx
    const myObj = {
    	numbers: [1]
    	myFunc() {
    		console.log(this) //myObj
    		this.numbers.forEach(function (number) {  // 여기서 this는 myObj
    			console.log(number) // 1
    			console.log(this)  // 여기서의 this는 window를 가리켜
    													// why? 함수 방식으로 호출되었기 때문에
    														// => 단순 호출은 전역 객체를 가리킴
    		})
    	}
    }
    
    myObj.myFunc() //myObj
    ```
    
    ```jsx
    // 이런식으로 함수를 밖에서 호출할 수 있는 경우는 this가 전역
    const myObj = {
    	numbers: [1]
    	myFunc() {
    		console.log(this) //myObj
    		this.numbers.forEach( a )
    	}
    }
    
    const  a = function (number) {  // 여기서 this는 myObj
    			console.log(number) // 1
    			console.log(this)  // window
    }
    
    myObj.myFunc() //myObj
    ```
    
4. Nested (Nested 키워드)
    - 이전에 일반 function 키워드와 달리 메서드의 객체를 잘 가리킴
    - 화살표 함수에서 this는 자신을 감싼 정적 범위
    - 자동으로 `한 단계 상위의 scope의 context를 바인딩`
        
        ⇒ 따라서 함수 호출의 한 단계 상위는 `myObj`
        
    
    ```jsx
    const myObj = {
    	numbers: [1]
    	myFunc() {
    		console.log(this) //myObj
    		this.numbers.forEach( (number) => {  // 여기서 this는 myObj
    			console.log(number) // 1
    			console.log(this)  // 화살표 함수로 정의 하면 한단계 상위 가리킴 myObj
    		})
    	}
    }
    
    myObj.myFunc() //myObj
    ```
    

## (4) 화살표 함수

- `화살표 함수`는 호출의 위치와 상관없이 `상위 스코프`를 가리킴
- Lexical scope
    - 함수를 어디서 호출하는 지가 아니라 `어디에 선언` 하였는지에 따라 결정
    - Static scope 라고도 하며 대부분의 프로그래밍 언어에서 따르는 방식

⇒ 함수 내의 함수 상황에서 화살표 함수를 쓰는 것을 권장

## (5) this와 addEventListener

```jsx
이거 따로 보기
```