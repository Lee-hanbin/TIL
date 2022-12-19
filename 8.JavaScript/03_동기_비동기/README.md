# 심화(중요)

# 동기와 비동기

## (1) Intro

ex) 카페

- 동기
    
    ⇒커피 주문 후 나올 때까지 기다려야함
    
- 비동기
    
    ⇒ 커피 주문 후 진동벨이 울리면 커피를 가져옴
    

ex) base.html에서 부트스트랩과 자바스크립트 적용하는 코드 적용

- 부트스트랩은 위에 적어주고 자바스크립트는 아래 적어주는 이유
    - 페이지의 이미지가 먼저 실행되고
    - 페이지의 조작은 그 이후에 일어나기 때문!!

## (2) 동기(`Synchronous`)

### 1. 정의

- 모든 일을 `순서대로 하나씩` 처리
- 순서대로 처리한다 == 이전 작업이 끝나면 다음 작업을 시작
- python 코드가 모두 동기식

### 2. 웹에서의 동기 경험

```jsx
<body>
  <button>버튼</button> 
  <script>
    const btn = document.querySelector('button')
    btn.addEventListener('click', () => {
      alert('you clicked me!')
      const pElem = document.createElement('p')
      pElem.innerText = 'p Element'
      document.body.appendChild(pElem)
    })
  </script>
</body>
```

## (3) 비동기(`Asynchronous`)

### 1. 정의

- 작업을 시작한 후 `결과를 기다리지 않고` 다음 작업을 처리하는 것(병렬적 수행)
- 시간이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리

### 2. 예시

```jsx
function slowRequest(callBack) {
  console.log('1. 오래 걸리는 작업 시작 ...')
  setTimeout(function () {  
    callBack()
  }, 3000)
}

function myCallBack() {
  console.log('2. 콜백함수 실행됨')
}

slowRequest(myCallBack)
console.log('3. 다른 작업 실행')
```

```jsx
// 답

1. 오래 걸리는 작업 시작 ...
3. 다른 작업 실행
2. 콜백함수 실행됨
```

⇒ JS는 처리가 바로 되지 않는 경우, 넘어가고 바로 처리되는 작업부터 실행

### 3. 비동기를 사용하는 이유

- `사용자 경험`
    - 동기식 처리는 특정 로직이 실행되는 동안 다른 로직 실행을 차단하기 때문에 마치 프로그램이 응답하지 않는 듯한 사용자 경험을 만들게 됨
    - 비동기로 처리한다면 먼저 처리되는 부분부터 보여줄 수 있으므로, 사용자 경험에 긍정적인 효과를 볼 수 있음
        
        ⇒ 많은 웹 기능은 비동기 로직을 사용해서 구현되어 있음
        
    
    ex)  아주 큰 데이터를 불러온 뒤 실행되는 앱이 있을 때, 동기로 처리한다면 데이터를 모두 불러온 뒤에야 앱의 실행 로직이 수행되므로 사용자들은 마치 앱이 멈춘 것과 같은 경험을 함
    

# JavaScript의 비동기 처리

## (1) Single Thread 언어, JavaScript

- 여러 작업을 동시에 처리하면 되지 않나?
    
    ⇒ JavaScript는 한 번에 하나의 일만 수행할 수 있는 Single Thread 언어로 동시에 여러 작업을 처리할 수 없음
    
    ```jsx
    // Thread
    - 작업을 처리할 때 실제로 작업을 수행하는 주체로,
     multi-thread라면 업무를 수행할 수 있는 주체가 여러 개라는 의미
    ```
    
- JavaScript는 하나의 작업을 요청한 순서대로 처리할 수 밖에 없는데 `어떻게 Single Thread인 JS가 비동기 처리`를 할 수 있지?

## (2) JavaScript Runtime

- JS 자체는 Single Thread이므로 비동기 처리를 할 수 있도록 도와주는 `환경이 필요`함
- 특정 언어가 동작할 수 있는 환경을 런타임이라고 함
- JS에서 비동기와 관련한 작업은 `브라우저 또는  Node 환경`에서 `처리`
- 브라우저 환경에서의 비동기 동작은 크게 아래의 요소들로 구성됨
    1. JavaScript Enginee Call  Stack
    2. Web API
    3. Task Queue
    4. Event Loop

## (3) 비동기 처리 동작 방식

- 브라우저 환경
    1. 모든 작업은 `Call Stack`(LIFO)으로 들어간 후 처리
    2. 오래 걸리는 작업이 Call Stack으로 들어오면 `Web API`로 보내서 처리
    3. Web API에서 처리가 끝난 작업들은 `Task Queue`(FIFO)에 순서대로 들어간다.
    4. `Event Loop`가 Call Stack이 비어 있는 것을 체크하고, Task Queue에서 가장 오래된 작업을 Call Stack으로 보냄
    
    ex) 
    
    ![1026_javascript.png](%E1%84%89%E1%85%B5%E1%86%B7%E1%84%92%E1%85%AA(%E1%84%8C%E1%85%AE%E1%86%BC%E1%84%8B%E1%85%AD)%206fd3b1878b3e456fb4df49214c7035d6/1026_javascript.png)
    
    1. Call Stack에 작업할 명령이 들어온다
    2. 바로 처리 가능하면 Output으로 바로 출력
        - 시간이 더 걸린다고 생각되면 Web API에 보내서 따로 작업을 처리하게 한다.
    3. Web API에서 해당 작업이 진행되는 동안 Call Stack은 새로운 작업들을 처리한다.
    4. Web API에서 작업이 끝나면 Task Queue에 넣는다.
    5. Call Stack이 모두 비게 되면, Task Queue에 있는 작업을 Call Stack에 넣어 처리한다.

# Axioss 기본 구조

## (1) Axios 라이브러리

- JavaScript의 HTTP 웹 통신을 위한 라이브러리
- 확장 가능하나 인터페이스와 쉽게 사용할 수 있는 비동기 통신 기능을 제공
- node 환경은 npm을 이용해서 설치 후 사용할 수 있고, broweser 환경은 CDN을 이용하여 사용 가능

## (2) Axios 기본 구조

### 1. Axios 실습

- python에서 `request` 역할
    
    ```jsx
    <script src="https://cdn.jsdeliver.net/npm/axios/dist/axios.min.js"></script>
    <script>
    	axios.get('요청할 URL')
    	.then(성공 시 콜백함수)
    	.catch(실패 시 콜백함수)
    ```
    
    - get, post 등 여러 method 사용가능
- 고양이 사진 가져오기
    - 파이썬
        
        ```python
        import requests 
        
        print('고양이는 야옹')
        
        cat_image_search_url = 'https://api.thecatapi.com/v1/images/search'
        response = requests.get(cat_image_search_url)
        
        if response.status_code == 200:
            print(response.json())
        else: 
            print('실패했다옹')
            
        print('야옹야옹')
        ```
        
        ![캡처.PNG](%E1%84%89%E1%85%B5%E1%86%B7%E1%84%92%E1%85%AA(%E1%84%8C%E1%85%AE%E1%86%BC%E1%84%8B%E1%85%AD)%206fd3b1878b3e456fb4df49214c7035d6/%25EC%25BA%25A1%25EC%25B2%2598.png)
        
    - JS
        
        ```jsx
        	<script>
            console.log('고양이는 야옹')
            const catImageSearchURL = 'https://api.thecatapi.com/v1/images/search'
        
            axios.get(catImageSearchURL)
              .then((response) =>{
                console.log(response.data)
              })
              .catch((error) => {
                console.log('실패했다옹')
              })
              console.log('야옹야옹')
        	</script>
        ```
        
        ![캡처.PNG](%E1%84%89%E1%85%B5%E1%86%B7%E1%84%92%E1%85%AA(%E1%84%8C%E1%85%AE%E1%86%BC%E1%84%8B%E1%85%AD)%206fd3b1878b3e456fb4df49214c7035d6/%25EC%25BA%25A1%25EC%25B2%2598%201.png)
        
        ```jsx
        
        	<script>
        		console.log('고양이는 야옹')
            const catImageSearchURL = 'https://api.thecatapi.com/v1/images/search'
        		const btn = document.querySelector('button')
        
            btn.addEventListener('click', function () {
        
              axios.get(catImageSearchURL)
                .then((response) =>{
                  // console.log(response.data[0].url)
                  imgElem = document.createElement('img')
                  imgElem.setAttribute('src', response.data[0].url)
                  document.body.appendChild(imgElem)
                }) 
                .catch((error) => {
                  console.log('실패했다옹')
                })
                console.log('야옹야옹')
            })
        	</script>
        ```
        
        ⇒ 버튼을 누르면 사진이 하나씩 늘어남 (먼저 로딩이 완료된 사진부터 첨부됨)
        
    
    ### 2. 정리
    
    - axios는 비동기로 데이터 통신을 가능하게 하는 라이브러리
    - 같은 방식으로 우리가 배운 Django REST API로 요청을 보내서 데이터를 받아온 후 처리할 수 있음

# Callback과 Promise

## (1) 비동기 처리의 단점

- 비동기 처리의 핵심은 Web API로 들어오는 순서가 아니라 `작업이 완료되는 순서에 따라 처리` 한다는 것!
    
    ⇒ 개발자 입장에서 코드의 실행 순서가 불명확하다는 단점이 있음
    
    ⇒ 실행 결과를 예상하면서 코드를 작성할 수 없음
    
    ⇒ 콜백함수 사용하여 처리 가능
    

## (2) Callback Function

`( 함수안에 함수안에 함수 … 라고 생각)`

### 1. 정의

- 특별한 함수가 아님! `다른 함수의 인자로 전달되는 함수`
- 비동기에만 사용되는 함수가 아니며 동기, 비동기 상관없이 사용 가능
- 시간이 걸리는 `비동기 작업이 완료된 후 실행할 작업을 명시하는 데 사용`되는 콜백 함수를 `비동기 콜백`이라 부름
- 예시
    - js
        
        ```jsx
        const btn = document.querySelector('button')
        btn.addEventListener('click' () => {
          alter('complated')
        })
        ```
        
        ⇒ Event Listener
        
    - django
        
        ```python
        from django.urls import path
        from . import views
        
        urlpatterns = [
        	path('index/', views.index)
        ]
        ```
        
        ⇒ View Function
        

### 2. 당위성

- 명시적인 호출이 아닌 특정한 조건 혹은 행동에 의해 호출되도록 작성 가능
- `요청오면 , 발생하면 , 데이터 받으면` 등의 조건으로 로직을 제어 가능
- 비동기 처리를 순차적으로 동작할 수 있게함
- 비동기 처리를 위해서는 콜백 함수의 형태가 반드시 필요

### 3. 콜백 지옥

- 콜백 함수는 연쇄적으로 발생하는 비동기 작업을 순차적으로 동작할 수 있게 함
- 보통 어떤 기능의 실행 결과를 받아서 다른 기능을 수행하기 위해 많이 사용
    
    ⇒ 비슷한 패턴이 계속 발생
    
- 비동기 처리를 위한 콜백을 작성할 때 마주하는 문제를 Callback Hell이라고 함
    
    ⇒ 코드 작성 형태가 피라미드와 같다고 하여 파멸의 피라미드라고도 부름
    

### 4. 정리

- 콜백 함수는 비동기 작업을 순차적으로 실행할 수 있게 하는 반드시 필요한 로직
- 비동기 코드를 작성하다 보면 콜백 함수로 인한 콜백 지옥은 반드시 나타나는 문제
    - 코드의 가독성 저하
    - 유지 보수가 어려움

## (3) Promise

`하나의 객체라고 생각!`

### 1. 정의

- `Callback Hell 문제를 해결`하기 위해 `등장`한 비동기 처리를 위한 객체
    
    (순서보장)
    
- 작업이 끝나면 실행 시켜줄게 ⇒ 약속
- `비동기 작업의 완료 또는 실패를 나타내는 객체`
- Promise 기반의 클라이언트가 바로 이전에 사용한 `Axios` 라이브러리
    - Promise based HTTP client for the browser and node.js
    - 성공에 대한 약속 then()
    - 실패에 대한 약속 catch()
- `.then(callback)`
    - 요청한 작업이 성공하면 callback() 실행
    - callback은 `이전 작업의 성공 결과를 인자로 전달 받음`
- `.catch(callback)`
    - then()이 하나라도 실패하면 callback 실행
    - callback은 이전 작업의 `실패 객체를 인자`로 전달 받음
- then과 catch 모두 항상 promise 객체를 반환
    
    ⇒ 계속해서 chanining을 할 수 있음
    
- axios로 처리한 비동기 로직이 항상 promise 객체를 반환
    
    ⇒ then을 계속 이어 나가면서 작성할 수 있음
    
    ![캡처.PNG](%E1%84%89%E1%85%B5%E1%86%B7%E1%84%92%E1%85%AA(%E1%84%8C%E1%85%AE%E1%86%BC%E1%84%8B%E1%85%AD)%206fd3b1878b3e456fb4df49214c7035d6/%25EC%25BA%25A1%25EC%25B2%2598%202.png)
    

### 2. 실습

```jsx
//기존의 콜백 함수 작성 방식

work1(function() {
	// 첫번째 작업
	work2(result1, function (result2) {
		// 두번째 작업
		work3(result2, function (result3) {
			console.log('최종 결과 : ' + result3)
		})
	})
})
```

```jsx
//Promise 방식

work1()
	.then((result1) => { 
		//work2
		return result2
	})
	.then((result2) => {
		//work3
		return result3
	})
	.catch((error) => {
		// error handling
	})
		
```

- promise 방식은 비동기  처리를 마치 우리가 일반적으로 위에서 아래로 적는 방식처럼 코드를 작성할 수 있음

### 3. Promise가 보장하는 것 ( vs 비동기 콜백)

- 비동기 콜백 작성 스타일과 달리 Promise가 보장하는 특징
    1. callback 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음
        - Promise callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출
    2. 비동기 작업이 성공하거나 실패한 뒤에 .then() 메서드를 이용하여 추가한 경우에도 1번과 똑같이 동작
    3. .then()을 여러 번 사용하여 여러 개의 callback 함수를 추가할 수 있음(Chaining)
        - 각각의 callback은 주어진 순서대로 하나하나 실행하게 됨
        - Chanining은 Promise의 가장 뛰어난 장점

### 4. 실습

```jsx
	dogBtn.addEventListener('click', function (event) {
      axios({
        method: 'get',
        url: dogImageSearchURL
      })
        .then((response) => {
          console.log(response.data.message)
          const imgSrc = response.data.message
          return imgSrc
        })
        .then((imgSrc) => {
          const imgTag = document.createElement('img')
          imgTag.setAttribute('src', imgSrc)
          document.body.appendChild(imgTag)
        })
        .catch((error) => {
          console.log(error)
        })
    })
```

![캡처.PNG](%E1%84%89%E1%85%B5%E1%86%B7%E1%84%92%E1%85%AA(%E1%84%8C%E1%85%AE%E1%86%BC%E1%84%8B%E1%85%AD)%206fd3b1878b3e456fb4df49214c7035d6/%25EC%25BA%25A1%25EC%25B2%2598%203.png)

⇒ then으로 Chanining하기 위해서는 위의 return 값이 아래의 argument로 들어가야 한다.

⇒ 둘 다 response로 해도 되지만, response로 하면 가독성이 떨어지므로 위 처럼 하나씩 지정해주자! 

[`https://axios-http.com/kr/docs/intro`](https://axios-http.com/kr/docs/intro) 의 `요청 config` 창에 들어가서 django와 연동할 때 필요한 양식이 정해져 있음 

# AJAX

`어떤 행위를 할때, 행위를 하고 페이지가 새로고침되지 않고 유지되게 하고싶음!!`

## (1) 정의

- 비동기 통신을 이용하면 화전 전체를 새로고침 하지 않아도 서버로 요청을 보내고, 데이터를 받아 화면의 일부분만 업데이트 가능
- 이러한 ‘비동기 통신 웹 개발 기술’을 Asynchronous Javascript And XML라 함

```jsx
// XML 언어 
⇒ HTML 작성 형식과 비슷하지만, 컴퓨터가 일을 더 해야함 (<p></p>처럼 호출이 2번 필요))
⇒ key와 value로 되어진 JSON을 이용하는 추세!
```

특징

1. 페이지 새로고침 없이 서버에 요청
2. 서버로부터 응답을 받아 작업을 수행

⇒ 비동기 웹 통신을 위한 라이브러리중 하나가 Axios

## (2) 비동기 적용하기

### 1. 사전 준비

- M:N 까지 진행한 프로젝트
- 가상 환경 생성 및 활성화, 패키지 설치

### 2. 팔로우(follow)

- 각각의 템플릿에서 script 코드를 작성하기 위한 block tag 영역 작성
- axios CDN 작성

```jsx
// 팔로우
1. form 에 대해서 서브밋에 대한 이벤트 달아줬어 
	=> form에 원래 있던 액션과 메소드 하지마! 내가 acxio로 해줄게
2. headers는 axios의 공식문서에서 확인해
3. axios의 usrl을 통해 데이터를 가져와
	=> form에서 id와 data-user-id를 통해 pk 가져와
4. redirect 대시 jsonResponse로 필요한 것 만 가져올거야
5. 이걸로 follow버튼을 선택해서 '팔로우' '언팔로우' 바꿔줘
6. follow 카운트도 가져와서 '팔로우 수' '팔로윙 수' 바꿔줘

-----------------------------------------------
// 좋아요 
1. 버튼 가져오기
2. 

--------------------------------------------------
//tip
1. 자스는 id로 구분
2. 장고는 pk로 구분
=> 자스의 id에 pk를 담아줌

------------------------------------------------
//로직

1. 새로고침되는걸 고치고 싶어
	=> 새로고침은 render로 받고, 그때그때 요청을 하기 때문
	=> event.preventDefault로 요청을 막고
	=> reder는 JsonResponse대체, 요청은 acxio로 받는다.
		 ( 필요한 데이터만 받아올 수 있음)
  => 
```

- AJAX로 csrftoken 보내는 법

[`https://docs.djangoproject.com/en/3.2/ref/csrf/#setting-the-token-on-the-ajax-request`](https://docs.djangoproject.com/en/3.2/ref/csrf/#setting-the-token-on-the-ajax-request)