# Vue

# Vue

## (1) Front-end 개발이란 무엇인가

### 1. 개요

- JavaScript를 활용한 Front-end 개발
- Back-end 개발은 Back-end 개발에 특화된 Django로 진행
- Front-end 개발은 `Vue.js` : JavaScript Front-end Framework

## (2) Front-end framework(FE)란 무엇인가

### 1. 개요

- Front-end 개발 : 사용자에게 보여주는 화면 만들기
- Web App(SPA)을 만들 때 사용하는 도구
    - SPA : Single Page Application

### 2. Web App 이란

- 웹 브라우저에서 실행되는 어플리케이션 소프트웨어
    
    ex) VINE 웹 사이트 ( [http://vibe.naver.com/today](http://vibe.naver.com/today) )
    
- 개발자 도구 > 디바이스 모드
- 웹 페이지가 그대로 보이는 것이 아닌 `디바이스에 설치된 App`처럼 보이는 것
- 웹 페이지가 디바이스에 맞는 적절한 UX/UI로 표현되는 형태

### 3. SPA(`Single Page Application`)

- Web App과 함께 자주 등장할 용어
- 이전까지는 사용자의 요청에 적절한 페이지 별 template를 반환
    
    ⇒ SPA는 서버에서 최초 1장의 HTML만 전달 받아 모든 요청에 대응하는 방식을 의미
    
    - 어떻게 한  페이지로 모든 요청에 대응?
        
        ⇒ Client Side Rendering (`CSR`) 방식으로 요청을 처리
        
        (tip : Server Side Rendering(SSR)은 기존의 요청 처리 방식을 말함)
        
        ![ssr.PNG](Vue%2090982275ee914a93b2b96d57f48b2e81/ssr.png)
        
        ![csr.PNG](Vue%2090982275ee914a93b2b96d57f48b2e81/csr.png)
        

### 4. CSR

- 최초 한 장의 HTML을 받아오는 것은 동일
    
    단, server로부터 최초로 받아오는 문서는 빈 html 문서
    
    ```python
    
    ```
    

- 각 요청에 대한 대응을 JavaScript를 사용하여 필요한 부분만 다시 렌더링
    1. 새로운 페이지를 서버에 `AJAX` 로 요청
    2. 서버는 화면을 그리기 위해 필요한 데이터를 JSON 방식으로 전달
    3. `JSON` 데이터를 JavaScript로 처리 & DOM 트리에 반영(렌더링)
    
    ```python
    
    ```
    

- CSR 방식을 사용하는 이유
    1. 모든 HTML 페이지를 서버로부터 받는 것은 아니기 때문
        - 클라이언트 : 서버 간 통신
            
            ⇒ `트래픽`이 `감소`
            
            ⇒ `응답 속도`가 `빨라`진다.
            
    2. 매번 새 문서를 받아 새로고침 하는 것이 아니라 필요한 부분만 고쳐 나가므로 각 요청이 끊김 없이 진행
        - SNS에서 추천을 누를 때 마다 첫 페이지로 돌아감 : `최악`
        - 요청이 자연스럽게 진행 : `UX 향상`
    3. BE와 FE의 작업 영역을 명확히 분리 가능
        - 각자 맡은 역할을 명확히 분리
            
            ⇒ 협업이 용이
            
- CSR의 한계
    1. 첫 구동 시 필요한 데이터가 많으면 많을수록 `최초 작동 시작`까지 `오랜 시간`이 `소요`
    2. Naver, Netflix, Disney+ 등 모바일에 설치된 `Web-App을 실행` 하게 되면 잠깐의 `로딩 시간`이 `필요`
    3. `검색 엔진 최적화` 가 어려움
        
        ⇒ 서버가 제공하는 것은 텅 빈 HTML 이므로 내용을 채우는 것은 AJAX 요청으로 얻은 JSON 데이터로 클라이언트(브라우저)가 진행
        
    4. 대체적으로 HTML에 작성된 내용을 기반으로 하는 검색 엔진에 빈 HTML을 공유하는 SPA 서비스가 노출되기는 어려움
- CSR vs SSR
    - CSR과 SSR은 공존할 수 있음
        - 내 서비스에 적합한 렌더링 방식을 적절하게 활용할 수 있어야 함
    - SPA 서비스에서도 SSR을 지원하는 Framework도 발전하고 있음
        
        ex) Vue의 Nuxt.js, React의 Next.js, Angular Universal … 
        

## (3) Vue를 배우는 이유

### 1. 이유

- 쉬움
- Vue는 타 framework에 비해 입문자가 시작하기에 좋은 Framework
- 왜 Vue는 상대적으로 낮은 진입 장벽을 가졌는가?
    - Angular보다 가볍고, 간편하게 사용할 수 있는 Framework로 만들어짐

### 2. 당위성

- Vue 구조는 매우 직관적
- FE Framework를 빠르게 쉽게 학습 및 활용 가능
- 다른 FE Frameowrk 학습 시 빠르게 적응 가능