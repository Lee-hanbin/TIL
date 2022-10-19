# Javascript 기초 문법

# 코드 작성법

## 1. 세미콜론

- 자바스크립트는 세미콜론을 선택적으로 사용 가능
- 세미콜론이 없으면 ASI에 의해 자동으로 세미콜론이 삽입됨
    - ASI ⇒ 자동 세미콜론 삽입 규칙

## 2. 들여쓰기와 코드 블럭

- python은 4칸 들여쓰기를 사용했으나, JS는 2칸 들여쓰기 사용
- `블록`은 if, for, 함수에서 중괄호 `{ }` 내부를 말함
    - pyhon은 들여쓰기를 이용해서 코드 블럭을 구분
    - JS는 중괄호 `{ }` 를 사용해 코드 블럭을 구분

## 3. 코드 스타일 가이드

- 코딩 스타일의 핵심은 합의된 원칙과 일관성
- 코드의 품질에 직결되는 중요한 요소
    - 코드의 가독성, 유지보수 또는 팀원과의 커뮤니케이션 등 개발 과정 전체에 영향을 끼침
- Python에도 PEP8이라는 코드 스타일 가이드가 있었듯, JavaScript에도 코드 스타일 가이드 존재
    
    ⇒ `Airbnb Style Guide` 를 기반으로 사용
    

## 4. 주석

- 한 줄 주석 (`//`)
- 여러 줄 (`/* */`)

# 변수와 식별자

## 1. 식별자 정의와 특징

- 식별자는 변수를 구분할 수 있는 변수명을 말한
- 식별자는 반드시 문자, `$` 또는 `_` 로 시작
- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작
- 예약어 사용 불가( for, if, …)
- 카멜 케이스
    - 변수, 객체, 함수에 사용
    
    ```jsx
    // 변수
    let dog
    let variableName
    
    // 객체
    const userInfo = { name: 'Tom', age:20 }
    
    // 함수
    function add() {}
    function getName() {}
    ```
    
- 파스칼 케이스
    - 클래스, 생성자에 사용
    
    ```jsx
    // 클래스
    class User{
    	constructor(options){
    		this.name = options.name
    	}
    }
    
    // 생성자 함수
    function User(options) {
    	this.name = options.name
    }
    ```
    
- 대문자 스네이크 케이스
    - 상수(Cont)에 사용
        - 개발자의 의도와 상관없이 변경될 가능성이 없는 값을 의미
    
    ```jsx
    // 값이 바뀌지 않을 상수
    const API_KEY = 'my-key'
    const PI = Math.PI
    
    // 재할당이 일어나지 않는 변수
    const NUMBERS = [1, 2, 3]
    ```
    

## 2. 변수 선언 키워드

- Python과 다르게 JavaScript는 변수를 선언하는 키워드가 정해져 있음
    
    ![변수키워드정리.PNG](Javascript%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%20%E1%84%86%E1%85%AE%E1%86%AB%E1%84%87%E1%85%A5%E1%86%B8%207a87a7583eee48bd95e417974cf91ac1/%25EB%25B3%2580%25EC%2588%2598%25ED%2582%25A4%25EC%259B%258C%25EB%2593%259C%25EC%25A0%2595%25EB%25A6%25AC.png)
    
    1. let
        - 블록 스코프 지역 변수를 선언 (추가로 동시에 값을 초기화)\
        - 재할당 가능 & 재설언 불가능
        
        ```jsx
        let number = 10 // 1. 선언 및 초기값 할당
        number = 20     // 2. 재할당
        
        let number = 10  // 1. 선언 및 초기값 할당
        let number = 20  // 2. 재선언 불가능
        ```
        
    2. const
        - 블록 스코프 읽기 전용 상수를 선언 (추가로 동시에 값을 초기화)
        - 재할당 불가능 & 재선언 불가능
        
        ```jsx
        const number = 10 // 1. 선언 및 초기값 할당
        number = 20       // 2. 재할당 불가능
        
        const number = 10   // 1. 선언 및 초기값 할당
        const number = 20   // 2. 재선언 불가능
        ```
        
    3. var
        - 변수를 선언 ( 추가로 동시에 값을 초기화)
        - 재할당 가능 & 재선언 가능
        - ES6 이전에 변수를 선언할 때 사용되던 키워드
        - `호이스팅` 되는 특성으로 인해 예기치 못한 문제 발생 가능
            - 쓰지마!
        - 함수 스코프를 가짐
        
        ```jsx
        # 함수 스코프
         - 함수의 중괄호 내부를 가리킴
         - 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능
        ```
        
        ![함수스코프.PNG](Javascript%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%20%E1%84%86%E1%85%AE%E1%86%AB%E1%84%87%E1%85%A5%E1%86%B8%207a87a7583eee48bd95e417974cf91ac1/%25ED%2595%25A8%25EC%2588%2598%25EC%258A%25A4%25EC%25BD%2594%25ED%2594%2584.png)
        
        - 호이스팅
            - 변수를 선언 이전에 참조할 수 있는 현상
            - var로 선언하면 변수는 선언 이전에 참조할 수 있으며, 이러한 현상을 호이스팅이라 함
            - 변수 선언 이전의 위치에서 접근 시 undefined를 반환
            
            ```jsx
            console.log(name)  // undefined => 선언 이전에 참조
            
            var name = '홍길동' // 선언
            ```
            

## 3. 선언, 할당, 초기화, 블록 스코프

- 선언 (Declaration)
    - 변수를 생성하는 행위 또는 시점
- 할당 (Assignment)
    - 선언된 변수에 값을 저장하는 행위 또는 시점
- 초기화(Initialization)
    - 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

```jsx
let foo    // 선언
console.log(foo)  // undefined

foo = 11   // 할당
console.log(foo)  // 11

let bar = 0   // 선언 + 할당
console.log(bar) // 0

```

- 블록 스코프
    - if, for, 함수 등의 중괄호 내부를 가리킴
    - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능
    
    ```jsx
    let x = 1
    if (x===1) {
    	let x = 2
    	console.log(x)   // 2
    }
    console.log(x)   // 1
    ```
    

# 데이터 타입

## 1. 정의

- JavaScript의 모든 값은 특정한 데이터 타입을 가짐
- 크게 `원시 타입`과 `참조 타입`으로 분류됨
    
    ![캡처.PNG](Javascript%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%20%E1%84%86%E1%85%AE%E1%86%AB%E1%84%87%E1%85%A5%E1%86%B8%207a87a7583eee48bd95e417974cf91ac1/%25EC%25BA%25A1%25EC%25B2%2598.png)
    

## 2. 원시 타입 (Primitive type)

### (1) Number

- 정수 또는 실수형 숫자를 표현하는 자료형
    
    ```jsx
    const a = 13
    const b = -5
    const c = 3. 14 // float - 숫자 표현
    const d = 2. 999e8 // 2.998 *10^8 = 299,800,000
    const e = Infinity
    const f = - Infinity
    const g = NaN  // Not a Number를 나타내는 값
    ```
    
- NaN
    - 숫자가 아님을 나타냄
    - Number.isNaN() 의 경우 주어진 값의 유형이 Number이고 값이 NaN이면 true 아니면 false

### (2) String

- 문자열을 표현하는 자료형
- 작은 따옴표 또는 큰 따옴표 모두 가능
    
    ```jsx
    const sentence1 = 'sdfsdfsdf`  // single quote
    const sentence2 = "sdasdaffd"  // double quote
    ```
    
- 곱셈, 나눗셈, 뺄셈은 안되지만 덧샘을 통해 문자열 붙일 수 있음
    
    ```jsx
    const fst = 'a'
    const snd = 'b'
    const full = fst + snd
    ```
    
- Quote를 사용하면 선언 시 줄 바꿈이 안됨
    - 대신 escape sequence를 사용할 수 있기 때문에 `\n` 을 사용해야 함
- Template Literal을 사용하면 줄바꿈이 되며, 문자열 사이에 변수도 삽입 가능
    
    ```jsx
    const age = 10
    const message = `홍길동은 ${age}세 입니다.`   // 숫자 1 옆에 backtick임!!!!
    ```
    

### (3) Empty Value

- 값이 존재하지 않음을 표현하는 값으로 JavaScript에서는 null과 underfined가 존재
- 동일한 역할을 하는 이 두개의 키워드가 존재하는 이유는 `단순한 JavaScript의 설계 실수`
- 큰 차이를 두지 말고 interchangeable 하게 사용할 수 있도록 권장함
1. null
    - null 값을 나타내는 특별한 키워드
    - 변수의 `값이 없음을 의도적으로 표현`할 때 사용하는 데이터 타입
        
        ```jsx
        let lastName = null
        console.log(lastName) // null - 의도적으로 값이 없음을 표현
        ```
        
2. undefined
    - 값이 정의되어 있지 않음을 표현하는 값
    - 변수 선언 이후 직접 값을 `할당하지 않으면` `자동으로 할당`됨
        
        ```jsx
        let firstName // 선언만하고 할당하지 않음
        console.log(firstName)  // undefined
        ```
        
3. 차이점
    - typeof 연산자를 통해 타입을 확인 했을 때 차이
        
        ```jsx
        typeof null      // 'object'
        typeof undefined // 'undefined'
        ```
        
        ⇒ null이 object 타입이 나오는 이유는 원시적인 실수
        

### (4) Boolean

- true 와 false
- 참과 거짓을 표현하는 값
- 조건문 또는 반복문에서 유용하게 사용
    - 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 자동 형변환 규칙에 따라 true 또는 false로 변환

![타입.PNG](Javascript%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%20%E1%84%86%E1%85%AE%E1%86%AB%E1%84%87%E1%85%A5%E1%86%B8%207a87a7583eee48bd95e417974cf91ac1/%25ED%2583%2580%25EC%259E%2585.png)

# 연산자

## 1. 할당 연산자

```jsx
lst c = 0

c += 10
console.log(c)  // 10

c -= 5
console.log(c)  // 5

c *= 10
console.log(c)  // 50

c++ // => c += 1권장
console.log(c)  // 51

c-- // => c -= 1 권장
console.log(c)  // 50
```

## 2. 비교 연산자

```jsx
3 > 2 // true
3 < 2 // false

'A' < 'B' // true
'Z' < 'a' // ture
'가' < '나' // true
```

## 3. 동등 연산자(`==`)

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 변환
- 비교할 때, `암묵적인 타입 변환` 을 통해 타입을 일치시킨 후 같은 값인지 비교
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
- 예상치 못한 결과가 발생할 수 있으므로 `특별한 경우를 제외`하고 `사용하지 않음`

```jsx
const a = 1
const b = '1'

console.log(a == b) //true
console.log(a == true) // true

// 자동 변환 예시
console.log(8*null) // 0, null은 0
console.log('5'-1)  // 4
```

## 4. 일치 연산자(`===`)

- 두 피연산자의 값과 타입이 모두 같은 경우 true를 반환

```jsx
const a = 1
const b = '1'

console.log(a === b) //false
console.log(a === Number(b)) // true
```

## 5. 논리 연산자

- and ⇒ `&&`
- or ⇒ `||`
- not ⇒ `!`

## 6.  삼항 연산자

- 3개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
- 가장 앞의 조건식이 참 ⇒ 앞의 값이 반환
- 가장 앞의 조건식이 거짓 ⇒ 뒤의 값이 반환

```jsx
true ? 1 : 2     //1
false ? 1 : 2    //2

const result = Math.PI > 4 ? 'Yep' : 'Nope'
console.log(result)    // Nope
```

# 조건문

## 1. 조건문의 종류와 특징

- if statement
    - 조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓을 판단
- switch statement
    - 조건 표현식의 결과값이 어느 값에 해당하는 지 판별 (case)
    - 주로 특정 변수의 값에 따라 조건을 분기할 때 활용
        - 조건이 많아질 경우 if문보다 가독성이 나을 수 있음

## 2. if statement

```jsx
const name = 'manager'

if (name === 'admin') {
	console.log('관리자님 환영합니다.')
} else if (name === 'manager){
	console.log('매니저님 환영합니다.')
} else {
	console.log(`${name}님 환영합니다.`)
}
```

## 3. switch statement (`break 조심!!`)

```jsx
const name = '길동이'

switch(name){
	case '길동이':{
		console.log('관리자님 환영합니다.')
		break
	}
	case 'manager'{
		console.log('매니저님 환영합니다.')
		break
	}
	default: {
		console.log(`${name}님 환영합니다.`)
	}
}
```

## 4. if / switch

- 조건이 많은 경우 switch문을 통해 가독성 향상을 기대
- 일반적으로 중첩 else if 문은 유지보수하기 힘들다는 문제 존재

# 반복문

## 1. 반복문 종류

- while
- for
- for … in
- for … of

## 2. Whie

```jsx
let i = 0

while (i<6) {
	console.log(i)
	i += 1
}
```

## 3. for

```jsx
for (let i = 0; i < 6; i++){
	console.log(i)
}
```

### (1) for in

- 객체의 속성을 순회할 떄 사용
- 배열도 순회 가능하지만 `인덱스 순으로 순환한다는 보장이 없으`므로 `권장 x`

```jsx
const fruits = { a: 'apple', b: 'banana' }

for (const key in fruits) {
	console.log(key) // a,b
	console.log(fruits[key]) //apple, banana
}
```

### (2) for of

- 반복 가능한 객체를 순회할 때 사용
- `반복 가능한 객체`의 종류 : `Array`, `Set`, `String`등

```jsx
const numbers = [0, 1, 2, 3]

for (const number of numbers) {
	console.log(number)  // 0, 1, 2, 3
}
```

### (3) 차이(`시험냄새가 나~ 서그래`)

- for in 은 속성 이름을 통해 반복 (객체에서 사용)
- for of 는 속성 값을 통해 반복 (나머지)  ← `객체에서 동작 x`

```jsx
const arr = [3, 5, 7]

for (const i in arr) {
	console.log(i)  // 0, 1, 2
}
for (const i of arr) {
	console.log(i)  // 3, 5, 7
}
```

### (4) for in 과 for of 에서의 `const`

- 일반적인 for문의 경우에는 최초 정의한 i를 재할당 하면서 사용하기 때문에 const를 사용 x
- for in 과 for of 의 경우는 재할당이 아니라, 매 반복 시 해당 변수를 새로 정의 ⇒ const 사용 o

# 함수

## 1. 개요

- 참조 타입 중 하나로써 function 타입에 속함
- JavaScript에서 함수를 정의하는 방법은 주로 2가지로 구분됨
    - 함수 선언식
    - 함수 표현식

## 2. 정의

### (1) 선언식

```jsx
function add(num1, num2) {
  return num1 + num2
}

console.log(add(2,7))
```

### (2) `표현식` ( 함수를 변수로 명명) ←————————- `이걸로 사용해!!`

```jsx
const sub = function (num1, num2) {
  return num1 - num2
}

console.log(sub(2, 7))
```

### (3) 기본 인자

```jsx
const greeting = function (name = 'Anoymous'){
  return `hi ${name}`
}

console.log(greeting())
```

⇒ 기본인자로 `name = 'Anoymous'`

### (4) 매개변수와 인자의 개수 불일치 허용

- 매개변수보다 인자의 개수가 다른 경우

```jsx
const noArgs = function(){
  return 0
}

console.log(noArgs(1, 2, 3))    // 0
console.log(noArgs(1, 2, 3, 4))  // 0

const twoArgs = function(ar1, ar2){
  return [ar1, ar2]
}
console.log(twoArgs(1, 2, 3))  // [1, 2]
console.log(twoArgs(1))  // [1, undefined]
```

### (5) Spread syntax

- 전개 구문
- 전개 구문을 사용하면 배열이나 문자열과 같이 `반복 가능한 객체`를 배열의 경우는 `요소`, `함수`의 경우는 `인자`로 `확장 가능`
    1. 배열과의 사용
    
    ```jsx
    let parts = ['so', 'ke']
    let lyrics = [ 'as', ...parts, 'fd', 'gh']
    console.log(lyrics)     //[ 'as', 'so', 'ke', 'fd', 'gh' ]
    ```
    
    1. 함수와의 사용
    - 정해지지 않은 수의 매개변수를 배열로 받음
    
    ```jsx
    const f = function (a, b, ...theArgs){
      return [a, b, theArgs]
    }
    
    console.log(f(1, 2, 3, 4, 5)) // [ 1, 2, [ 3, 4, 5 ] ]
    console.log(f(1, 2))          // [ 1, 2, [] ]
    ```
    

## 3. 선언식과 표현식

### (1) 호스팅식

- 선언식
    - 함수 선언식으로 정의한 함수는 var 로 정의한 변수처럼 호스팅이 발생
    - 즉, 함수 호출 이후에 선언해도 동작
    
    ```jsx
    console.log(add(2,7))  // 9
    
    function add(num1, num2) {
    	return num1 + num2
    }
    ```
    
- 표현식
    - 함수 표현식으로 선언한 함수는 함수 정의 전제 호출 시 에러 발생
    - 변수로 평가되어 변수의 scope 규칙을 따름
    
    ```jsx
    console.log(sub(2,7))  
    // ReferenceError: Cannot access 'sub' before initialization
    const sub = function (num1, num2) {
    	return num1 + num2
    }
    ```
    

# Arrow Function

## 1. 정의 ( Arrow Function 화살표함수)

- 함수를 비교적 간결하게 정의할 수 있는 문법
- function 키워드와 중괄호를 이용한 구문을 짧게 사용하기 위해 탄생
    1. function 키워드 생략가능
    2. 함수의 매개변수가 하나뿐이라면 `( )` 도 생략 가능
    3. 함수의 내용이 한 줄이라면  `{ }` 와 return 도 생략가능
- 화살표 함수는 항상 익명 함수
    - ==함수 표현식에서만 사용가능

## 2. 실습

```jsx
const greeting = function (name){
  return `hi ${name}`
}

// 1단계
const greeting = (name) => {
  return `hi ${name}`
}

// 2단계  <--- 권장 x
const greeting = name => {
  return `hi ${name}`
}

// 3단계
const greeting = name => `hi ${name}`
// 3단계도 이렇게 () 있는 것을 강조
const greeting = (name) => `hi ${name}`
```

## 3. 응용

```jsx
//1. 인자가 없다면? () or _로 표시 가능
let noArgs = () => 'No args'
noArgs = _ => 'No args'

//2-1 object 를 return 하면
let returnObject = () => { return { key: 'value'} } //return을 명시적으로 적어줌

//2-2 return 을 적지 않으려면 괄호를 붙여야 함
returnObject = () => ({ key: 'value'})
```

## 4. 즉시 실행 함수

- 선언과 동시에 실행되는 함수
- 함수 선언 끝에 `()` 를 추가하여 선언되자 마자 실행하는 형태
- `()` 에 값을 넣어 인자로 넘겨줄 수 있음
- 즉시 실행 함수는 선언과 동시에 실행되기 때문에 같은 함수를 다시 호출할 수 없음
- 이러한 특징을 살려 초기화 부분에 많이 사용
- 일회성 함수이므로 익명함수로 사용하는 것이 일반적

```jsx
(function(num) { return num ** 3})(2)  //6

(num => num **3)(2) //8
```

# Array와 Object

## 1. 개요

- JavaScript의 데이터 타입 중 참조 타입에 해당 하는 타입은 array와 object이며, 객체라고 말함
- 객체는 속성들의 모음
- (참고) 객체 안쪽의 속성들은 메모리에 할당 되어있고 해당 객체는 메모리의 시작 주소값을 가리키고 있는 형태로 이루어져 있다.

## 2. 배열(Array)

### (1) 정의

- 키와 속성들을 담고 있는 참조 타입의 객체
- 순서를 보장하는 특징이 있음
- 주로 대괄호를 이용하여 생성하고, 0을 포함한 `양의 정수 인덱스`로 특정 값에 접근 가능
- 배열의 길이는 array.length 형태로 접근 가능

```jsx
const numbers = [1, 2, 3, 4, 5]

console.log(numbers[0])         //1
console.log(numbers[-1])        //undefined
console.log(numbers.length)     //5
console.log(numbers[numbers.length-1]) //5
```

### (2) 배열 메서드 기초

![배열메서드.PNG](Javascript%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%20%E1%84%86%E1%85%AE%E1%86%AB%E1%84%87%E1%85%A5%E1%86%B8%207a87a7583eee48bd95e417974cf91ac1/%25EB%25B0%25B0%25EC%2597%25B4%25EB%25A9%2594%25EC%2584%259C%25EB%2593%259C.png)

- `array.reverse()`
    - 원본 배열 요소들의 순서를 반대로 정렬
- `array.push()`
    - 배열의 가장 뒤에 요소 추가
- `array.pop()`
    - 배열의 마지막 요소 제거
- `array.includes(value)`
    - 배열에 특정 값이 존재하는지 판별 후 `참, 거짓 반환`
- `array.indexOf(value)`
    - 배열에 특정 값이 존재하는지 확인 후 가장 첫 번째로 찾은요소의 인덱스 반환
    - 만약 해당 값이 없을 경우 -1 반환
- `array.join([separator])`
    - 배열의 모든 요소를 연결하여 반환
    - separator(구분자)는 선택적으로 지정 가능하며, 생략 시 쉼표를 기본 값으로 사용
    
    ```jsx
    const numbers = [1, 2, 3, 4, 5]
    let result
    
    result = numbers.join()
    console.log(result)     //1,2,3,4,5
    
    result = numbers.join('')
    console.log(result)     //12345
    
    result = numbers.join(' ')
    console.log(result)     //1 2 3 4 5
    
    result = numbers.join('-')
    console.log(result)     //1-2-3-4-5
    ```
    

### (3) 배열 메서드 심화

- `배열을 순회`하며 특정 로직을 수행하는 메서드
- 메서드 호출 시 인자로 `callback 함수`를 받는 것이 특징
    - callback 함수 : 어던 함수의 내부에서 실행될 목적으로 인자로 넘겨받는 함수

![배열메서드2.PNG](Javascript%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%20%E1%84%86%E1%85%AE%E1%86%AB%E1%84%87%E1%85%A5%E1%86%B8%207a87a7583eee48bd95e417974cf91ac1/%25EB%25B0%25B0%25EC%2597%25B4%25EB%25A9%2594%25EC%2584%259C%25EB%2593%259C2.png)

1. forEach
    - `array.forEach(callback(element[, index[, array]]))`
    - 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한 번씩 실행
        - element : 배열의 요소
        - index : 배열 요소의 인덱스
        - array : 배열 자체
    - 반환 값 없음
    - 예시
    
    ```jsx
    // 1.
    const colors = ['red', 'blue', 'green']
    
    const printClr = function (color) {
      console.log(color)
    }
    
    colors.forEach(printClr)
    
    // 2. 
    colors.forEach(function (color){
      console.log(color)
    })
    
    // 3-1.
    colors.forEach((color) => {
      console.log(color)
    })
    
    // 3-2
    color.forEach((color) => console.log(color))
    ```
    
2. map
    - `array.map(callback(element[. index[, array]]))`
    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
    - 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환
    - 기존 `배열 전체`를 `다른 형태`로 바꿀 때 유용
    
    ```jsx
    const numbers =[1, 2, 3, 4, 5]
    
    //1.
    const doubleEle = function (number) {
      return number * 2
    }
    
    const newArry = numbers.map(doubleEle)
    
    console.log(newArry)
    
    //2.
    const newArry = numbers.map(function (number) {
      return number * 2
    })
    
    //3-1. 
    const newArry = numbers.map((numbers) => {
      return number * 2
    })
    
    //3-2.
    const newArry = numbers.map((numbers) => number * 2)
    ```
    

1. filter (map + T/F)
    - `array.filter(callback(element[, index[, array]]))`
    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
    - 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열 반환
    - 기존 배열의 요소들을 필터링할 때 유용
    
    ```jsx
    const products = [
      { name: 'cucumber', type: 'vegetable' },
      { name: 'banana', type: 'fruit' },
      { name: 'carrot', type: 'vegetable'},
      { name: 'apple', type: 'fruit' },
    ]
    
    //1.
    const fruitFilter = function (product) {
      return product.type === 'fruit'
    }
    
    const newArry = products.filter(fruitFilter)
    console.log(newArry)
    
    //2. 
    const newArry = products.filter(function (product) {
      return product.type === 'fruit'
    })
    
    //3-1.
    const newArry = products.filter((product) => {
      return product.type === 'fruit'
    })
    
    //3-2
    const newArry = products.filter((product) => product.type === 'fruit')
    ```
    

1. reduce 
    - `array.reduce(callback(acc, element[, index[, array]])[, initialValue])`
    - 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한 번씩 실행해서, 하나의 값을 반환
    - 배열을 하나의 값으로 계산하는 동작이 필요할 때 사용(sum, avg …)
    - map, filter 등 여러 배열 메서드 동작을 대부분 대체할 수 있음
    - reduce 메서드의 주요 매개변수
        - acc
            - 이전 callback 함수의 반환 값이 누적되는 변수
        - initialValue(optional)
            - 최초 callback 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫 번째 값
    - reduce의 첫 번째 매개변수인 콜백함수의 첫 번째 매개변수(`acc`)는 누적된 값
    - reduce의 두 번째 매개변수인 `initialValue` 는 누적될 값의 초기값, 지정하지 않을 시 첫 번째 요소의 값이 됨
        
        ⇒ 빈 배열의 경우, initialValue를 제공하지 않으면 에러 발생
        
    - 예시
    
    ```jsx
    const numbers = [90, 80, 70, 100]
    
    // 총합
    // 1. 
    const sumNum = numbers.reduce(function (result, number){
      return result + number
    },0)
    
    console.log(sumNum)
    
    // 2.
    const sumNum = numbers.reduce((result, number) => {
      return result + number
    },0)
    
    // 3.
    const sumNum = numbers.reduce((result, number) => result + number,0)
    
    // 평균
    const avgNum = numbers.reduce((result, number) => result + number,0)/ numbers.length
    console.log(avgNum)
    ```
    
2. find
    - `array.find(callback(element[, index[, array]]))`
    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
    - 콜백 함수의 반환 값이 참이면, 조건을 만족하는  첫 번째 요소를 반환
    - 찾는 값이 배열에 없으면 undefined 반환
    - 예시
        
        ```jsx
        const avengers = [
          { name: 'Tony Stark', age: 45},
          { name: 'Steve Rogers', age: 32},
          { name: 'Thor', age: 40},
        ]
        
        const avenger = avengers.find((avenger) => avenger.name === 'Tony Stark')
        
        console.log(avenger)
        ```
        
3. some
    - `array.some(callback(element[, index[, array]]))`
    - 배열의 요소 중 `하나라도` 주어진 판별 `함수를 통과`하면  `참`을 반환
    - 모든 요소가 통과하지 못하면 거짓 반환
    - `빈 배열`은 항상 `false` 반환
    - 예시
        
        ```jsx
        const arr = [1, 2, 3, 4, 5]
        
        //1. 
        const result = arr.find(function (elem) {
          return elem % 2 === 0
        })
        
        //2.
        const result = arr.find((elem) => {
          return elem % 2 === 0
        })
        
        //3.
        const result = arr.find((elem) => elem % 2 === 0)
        ```
        
4. every
    - `array.every(callback(elementt[, index[, array]])`
    - 배열의 `모든 요소`가 주어진 판별 `함수를 통과`하면 `참`을 반환
    - 하나의 요소라도 통과하지 못하면 거짓 반환
    - `빈 배열`은 항상 `true` 반환
    - 예시
        
        ```jsx
        const arr = [1, 2, 3, 4, 5]
        
        //1. 
        const result = arr.every(function (elem) {
          return elem % 2 === 0
        })
        
        //2.
        const result = arr.evrey((elem) => {
          return elem % 2 === 0
        })
        
        //3.
        const result = arr.evrey((elem) => elem % 2 === 0)
        ```
        

### (4) 배열 순회 비교

![순회비교.PNG](Javascript%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%20%E1%84%86%E1%85%AE%E1%86%AB%E1%84%87%E1%85%A5%E1%86%B8%207a87a7583eee48bd95e417974cf91ac1/%25EC%2588%259C%25ED%259A%258C%25EB%25B9%2584%25EA%25B5%2590.png)

⇒ 기본적으로 forEach문을 사용

⇒ forEach((char, idx) 로 idx도 출력 가능

## 3. 객체(Object)

### (1) 개요

- 객체는 속성(property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현
- key는 문자열 타입만 가능
    - key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현
- value는 모든 타입(함수포함) 가능
- 객체 요소 접근 점(.) 또는 대괄호([ ])로 가능
    - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능
- 예시
    
    ```jsx
    const myInfo = {
      name: 'jack',
      phoneNumber: '123456',
      'samsung product': {
        buds: 'Buds pro',
        galaxy: 'S99',
      },
    }
    
    console.log(myInfo.name)        //jack
    console.log(myInfo['name'])     //jack
    
    console.log(myInfo['samsung product'])      //{ buds: 'Buds pro', galaxy: 'S99' }
    console.log(myInfo['samsung product'].galaxy)  // 599
    ```
    

### (2) 객체 관련 문법

- ES6에 새로 도입된 문법들로 객체 생성 및 조작에 유용하게 사용 가능
    1. 속성명 축약
    2. 메서드명 축약
    3. 계산된 속성명 사용하기
    4. 구조 분해 할당
    5. 객체 전개 구문

1. 속성명 축약
    - 객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 예시와 같이 축약 가능

1. 메서드명 축약
    - 메서드 선언 시 function 키워드 생략 가능
        
        ```jsx
        const obj = {
          name: 'jack',
          greeting(){
            console.log('hi!')
          }
        }
        
        console.log(obj.name)
        console.log(obj.greeting())
        ```
        
2. 계산된 속성 명 사용하기
    - 객체를 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성 가능
        
        ```jsx
        const key = 'country'
        const value = ['한국', '미국', '일본', '중국']
        
        const myObj = {
          [key]: value,
        }
        
        console.log(myObj)
        console.log(myObj.country)
        ```
        
3. 구조 분해 할당 ( `중요!!`)
    - 배열 도는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법
        
        ```jsx
        const userInformation = {
          name: 'ssafy kim',
          userId: 'ssafyStudent1234',
          phoneNumber: '010-1234-1234',
          email: 'ssafy@ssafy.com',
        }
        
        const name = userInformation.name
        const userId = userInformation.userId
        const phoneNumber = userInformation.phoneNumber
        const email = userInformation.email
        ```
        
        ```jsx
        const {name} = userInformation
        const {userId} = userInformation
        const {phoneNumber} = userInformation
        const {email} = userInformation
        ```
        
4. Spread syntax(`…`)
    - 배열과 마찬가지로 전개구문을 사용해 객체 내부에서 객체 전개 가능
    - 얕은 복사에 활용 가능
        
        ```jsx
        const obj = {b: 2, c: 3, d: 4}
        const newObj = {a: 1, ...obj, e: 5}
        
        console.log(newObj)  //  {a: 1, b: 2, c: 3, d: 4, e: 5}
        ```
        

### (3) JSON (JavaScript Object Notation)

- Key-Value 형태로 이루어진 자료 표기법
- JS의 Object와 유사한 구조를 가지고 있지만 Object는 그 자체로 타입이고, `JSON`은 형식이 있는 `문자열`
- 즉, JSON을 Object로 사용하기 위해서는 변환 작업이 필요
    
    ```jsx
    const jsonData = {
      coffee: 'Ame',
      iceCream: 'Mint Choco',
    }
    ```
    
    ```jsx
    	// Object -> json
    const objToJson = JSON.stringify(jsonData)
    
    console.log(objToJson)    // {"coffee":"Ame","iceCream":"Mint Choco"}
    console.log(typeof objToJson)   // string
    ```
    
    ```jsx
    // json -> Object
    const jsonToObj = JSON.parse(objToJson)
    
    console.log(jsonToObj)    // {"coffee":"Ame","iceCream":"Mint Choco"}
    console.log(typeof jsonToObj)   // object
    console.log(jsonToObj.coffee)   // Ame
    ```
    
    ⇒ Json을 Object로 바꿔서 데이터를 갖고 놀 수 있음