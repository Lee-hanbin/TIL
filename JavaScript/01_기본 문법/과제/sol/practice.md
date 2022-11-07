# practice

- pracice 1. 주어진 코드를 리팩토링하시오.
    1. 해당 코드를 template string 을 활용하여 리팩토링 하시오.
        
        ```jsx
        const name = 'Tom'
        console.log('Hi, my name is ' + name)
        ```
        
    - 답
        
        ```jsx
        const name = 'Tom'
        
        console.log(`Hi, my name is ${name}`)
        ```
        
    
    b. 해당 코드를 arrow function 으로 리팩토링하시오.
    
    ```jsx
    function add(x, y) {
      return x + y
    }
    
    function square(x) {
      return x ** 2
    }
    ```
    
    - 답
        
        ```jsx
        const add = (x, y) => x+y
        
        const squre = (x) => x**2
        ```
        
    
    c. 해당 코드의 메서드 introduce 를 function 키워드 없이 리팩토링하시오.
    
    ```jsx
    const tom = {
      name: 'Tom',
      introduce: function () {
        console.log('Hi, my name is' + this.name)
      }
    }
    ```
    
    - 답
        
        ```jsx
        const tom = {
              name: 'Tom',
              introduce: () => console.log('Hi, my name is' + name)
        }
        ```
        
        - 교재 답
            
            ```jsx
            const tom = {
                  name: 'Tom',
                  introduce() {
                    console.log('Hi, my name is' + this.name)
                  }
                }
            ```
            
    
    d. 해당 코드를 key, value를 한번씩만 작성하도록 리팩토링하시오.
    
    ```jsx
    const url = 'https://test.com'
    const data = { message: 'Hello World!' }
    
    const request = { url: url, data: data }
    ```
    
    - 답
        
        ```jsx
        const request = { url, data }
        ```
        
    
- practice 2. array helper methods를 활용해 주어진 문제를 해결하라
    
    ```jsx
    const users = [
          { name: 'Jack', age: 31, isMarried: true, balance: 100, },
          { name: 'Sarah', age: 22, isMarried: false, balance: 200, },
          { name: 'Ash', age: 25, isMarried: true, balance: 300, },
          { name: 'Robert', age: 27, isMarried: false, balance: 400, },
          { name: 'Tom', age: 35, isMarried: true, balance: 500, },
        ]
    ```
    
    1. forEach 메서드를 활용해 모든 사용자들의 이름을 출력하시오.
    - 답
        
        ```jsx
        //1
            const first = function(person) {
              console.log(person.name)
            }
            users.forEach(first)
        ```
        
    1. filter 메서드를 활용해 결혼한 사람들만 모아 marriedUsers 상수에 할당하시오.
    - 답
        
        ```jsx
        //2
            const second = function (person) {
              return person.isMarried
            }
            const merriedUsers = users.filter(f)
            console.log(second)
        ```
        
    1. find 메서드를 활용해 이름이 'Tom'인 사람만 tom 상수에 할당하시오.
    - 답
        
        ```jsx
        //3 
            const third = function (person) {
              return person.name === 'Tom'
            }
            const tom = users.find(third)
            console.log(tom)
        ```
        
    1. map 메서드를 활용해 모든 사용자에게 isAlive 키를 추가하고 true로 설정한 뒤, newUsers 상수에 할당하시오.
    - 답
        
        ```jsx
        //4
            const forth = function (person) {
              person.isAlive = true
              return person
            }
            const newUsers = users.map(forth)
            console.log(newUsers)
        ```
        
    1. reduce 메서드를 활용해 모든 사용자들의 계좌잔액을 totalBalance 상수에 할당하시오.
    - 답
        
        ```jsx
        //5
            const fifth = function (sol, person) {
              return sol + person.balance
            }
            const totalBalance = users.reduce(fifth,0)
            console.log(totalBalance)
        ```
        
- practice 3. 구조분해와 rest와 spread 연산자를 활용해 주어진 코드를 리팩토링하시오.
    1. 아래 코드를 object destructuring을 활용해 리팩토링 하시오.
        
        ```jsx
        //ㄱ
        const savedFile = {
          name: 'profile',
          extension: 'jpg',
          size: 29930
        }
        
        function fileSummary(file) {
          console.log(`The file ${file.name}.${file.extension} is size of ${file.size} bytes.`)
        }
        
        fileSummary(savedFile)
        ```
        
        ```jsx
        //ㄴ
        const data = {
          username: 'myName',
          password: 'myPassword',
          email: 'my@mail.com',
        }
        ```
        
        - 답
            
            ```jsx
            //ㄱ
            function fileSummary({name, extension, size}) {
              console.log(`The file ${name}.${extension} is size of ${size} bytes.`)
            }
            
            ```
            
            ```jsx
            //ㄴ
            const {username} = data
            const {password} = data
            const {email} = data
            ```
            
    2. Rest operator를 활용해 아래 코드를 리팩토링 하시오.
        
        ```jsx
        function addNumbers(a, b, c, d, e) {
          const numbers = [a, b, c, d, e];
          return numbers.reduce((sum, number) => {
            return sum + number
          }, 0)
        }
        
        console.log(addNumbers(1, 2, 3, 4, 5))
        ```
        
        ```jsx
        function addNumbers(...numbers) {
          // 화살표 함수로 함께 리팩토링
          return numbers.reduce((sum, number) => sum + number, 0)
        }
        
        console.log(addNumbers(1, 2, 3, 4, 5))
        ```
        
    3. Spread operator를 활용해 아래 코드를 리팩토링 하시오.
        
        ```jsx
        //ㄱ
        const defaultColors = ['red', 'green', 'blue'];
        const favoriteColors = ['navy', 'black', 'gold', 'white']
        const palette = defaultColors.concat(favoriteColors);
        ```
        
        ```jsx
        //ㄴ
        const info1 = { name: 'Tom', age: 30 }
        const info2 = { isMarried: true, balance: 3000 }
        const fullInfo = Object.assign(info1, info2)
        
        console.log(fullInfo)
        ```
        
        - 답
            
            ```jsx
            //ㄱ
            const pelette = [...defaultColors , ...favoriteColors ]
            ```
            
            ```jsx
            //ㄴ
            const fullInfo = { ...info1, ...info2 }
            ```
            
        
        ![concat.PNG](practice%20ac5e3264d47a4fa58b9b3821534b3e0a/concat.png)