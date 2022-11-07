# hw

# JavaScript 기초

## 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

```jsx
1. JavaScript에서 함수는 변수에 할당, 인자로 전달할 수 있으나 함수의 결과값으로 반환 불가
2. 함수의 매개변수의 개수와 인자의 개수는 반드시 일치하지 않아도 동작
3. 배열에 새로운 요소를 추가하는 메서드는 append
4. JSON 데이터는 바로 객체처럼 key 접근이 가능.
5. 화살표 함수와 function 키워드로 선언한 함수는 차이가 없다.
```

```jsx
//답
1. false : 즉시 실행 함수의 경우를 제외하고는 모두 가능
2. true : 더 많으면 무시, 더 적으면 undefined
3. false : push
4. false : JSON을 Object로 변환 시켜줘야함 (stringify) <-> (perse)
5. false : this 키워드가 함수 내부에 존재한다면, 차이가 있다.
```

## 2. 다음의 Array Helper Method의 동작을 간략히 서술하시오.

- forEach
    
    ```
    - array.forEach(callback(element[, index[, array]]))
    - 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한 번씩 실행
        - element : 배열의 요소
        - index : 배열 요소의 인덱스
        - array : 배열 자체
    - 반환 값 없음
    ```
    
    ```jsx
    // ex
    const colors = ['red', 'blue', 'green']
    
    const printClr = function (color) {
      console.log(color)
    }
    
    colors.forEach(printClr)
    ```
    
    ⇒ `forEach` 함수에 `printClr` 라는 함수가 argument로 들어가 있음
    

- map
    
    ```
    - array.map(callback(element[, index[, array]]))
    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
    - 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환
    - 기존 `배열 전체`를 `다른 형태`로 바꿀 때 유용
    ```
    
    ```jsx
    const numbers =[1, 2, 3, 4, 5]
    
    const doubleEle = function (number) {
      return number * 2
    }
    const newArry = numbers.map(doubleEle) // [2, 4, 6, 8, 10]
    ```
    
- filter
    
    ```
    - array.filter(callback(element[, index[, array]]))
    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
    - 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열 반환
    - 기존 배열의 요소들을 필터링할 때 유용
    ```
    
    ```jsx
    const products = [
      { name: 'cucumber', type: 'vegetable' },
      { name: 'banana', type: 'fruit' },
      { name: 'carrot', type: 'vegetable'},
      { name: 'apple', type: 'fruit' },
    ]
    
    const fruitFilter = function (product) {
      return product.type === 'fruit'
    }
    const newArr = products.filter(fruitFilter)
    console.log(newArr)
    ```
    
- find
    
    ```
    - array.find(callback(element[, index[, array]]))
    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
    - 콜백 함수의 반환 값이 참이면, 조건을 만족하는  첫 번째 요소를 반환
    - 찾는 값이 배열에 없으면 undefined 반환
    ```
    
    ```jsx
    const avengers = [
      { name: 'Tony Stark', age: 45},
      { name: 'Steve Rogers', age: 32},
      { name: 'Thor', age: 40},
    ]
    
    const Tonyfinder = function (avenger) {
      return avenger.name == 'Tony Stark'
    }
    const a = avengers.find(Tonyfinder)
    // const avenger = avengers.find((avenger) => avenger.name === 'Tony Stark')
    
    console.log(a)
    ```
    
- every
    
    ```
    - array.every(callback(element[, index[, array]])
    - 배열의 `모든 요소`가 주어진 판별 `함수를 통과`하면 `참`을 반환
        ⇒ 수학 기호 중에 All이라고 생각
    - 하나의 요소라도 통과하지 못하면 거짓 반환
    - `빈 배열`은 항상 `true` 반환
    ```
    
    ```jsx
    const arr = [1, 2, 3, 4, 5]
    
    const c_f = function (i) {
      return i <6
    }
    const rst = arr.every(c_f)
    ```
    
- some
    
    ```
    - array.some(callback(element[, index[, array]]))
    - 배열의 요소 중 `하나라도` 주어진 판별 `함수를 통과`하면  `참`을 반환
        
        ⇒ 수학 기호 중에 exist라고 생각
        
    - 모든 요소가 통과하지 못하면 거짓 반환
    - `빈 배열`은 항상 `false` 반환
    ```
    
    ```jsx
    const arr = [1, 2, 3, 4, 5]
    
    const c_f = function (i) {
      return i <3
    }
    const rst = arr.some(c_f)
    console.log(rst)
    ```
    
- reduce
    
    ```
    - array.reduce(callback(acc, element[, index[, array]])[, initialValue])
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
    ```
    
    ```jsx
    const numbers = [90, 80, 70, 100]
    
    const c_f = function (a, num) {
      return a + num
    }
    const rst = numbers.reduce(c_f,0)
    console.log(rst)
    ```