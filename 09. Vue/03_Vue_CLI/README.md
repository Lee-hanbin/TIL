# Vue CLI

- 목차

# Vue CLI

## (1) 정의

- Vue 개발을 위한 표준 도구
- 프로젝트의 구성을 도와주는 역할
- 확장 플러그인, GUI, Babel등 다양한 tool 제공

## (2) Vue CLI Quick Start

- 설치
    
    `$ npm install -g @vue/cli`
    
    ⇒ -g는 전역이므로 아무 위치에서 설치해도 된다.
    
- 프로젝트 생성
    
    `$ vue create vue-cli`
    
    ![프로젝트설치.PNG](Vue%20CLI%2073225c46417948b5a42fc8192f812918/%25ED%2594%2584%25EB%25A1%259C%25EC%25A0%259D%25ED%258A%25B8%25EC%2584%25A4%25EC%25B9%2598.png)
    
    ⇒ Vue 2 선택 
    
    ![플젝생성완료.PNG](Vue%20CLI%2073225c46417948b5a42fc8192f812918/%25ED%2594%258C%25EC%25A0%259D%25EC%2583%259D%25EC%2584%25B1%25EC%2599%2584%25EB%25A3%258C.png)
    
    ⇒ 성공
    
- 출력된 명령어 실행
    - 프로젝트 디렉토리 이동
        
        `$ cd {프로젝트명}`
        
    - 프로젝트 실행
        
        `$ npm run serve`
        
        ![runserve.PNG](Vue%20CLI%2073225c46417948b5a42fc8192f812918/runserve.png)
        
        ⇒ Network는 다른 곳에서 모바일로 접속 가능하게 만듦
        
    - node_modules 가 존재하지 않을 때
        
        `$ npm install` : node_modules 폴더 생성됨
        

## (3) Vue CLI 프로젝트 구조

`주의` 자동으로 git에 기동되므로 깃에 올릴 때는 `.git` 을 지우고 올리기

### 1. Babel

- JavaScript의 Compiler
- 호환성의 문제를 해결해주는 번역기의 역할

### 2. Webpack

- static module bundler
- 모듈 간의 의존성 문제를 해결하기 위한 도구
- 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함
- Module
    
    ```python
    - 개발하는 애플리케이션의 크기가 커지고 복잡해지면 파일 하나에 모든 기능을 담기 어려워짐
     => 자연스럽개 파일을 여러 개로 분리하여 관리를 하게 됨
     => 분리된 파일 각각이 모듈
    - 모듈은 대개 기능 단위로 분리
     => 클래스 하나 혹은 특정 목적을 가진 복수의 함수로 구성된 라이브러리 하나로 구성
    - ex)
     ESM(ECMA Script Module), AMD, CommonJS, UMD
    ```
    
    ⇒ 모듈이 많이 생기면서 모듈 간의 의존성 문제가 생김 (오류가 생겼을 때 찾기 어려움)
    
    ⇒ 이러한 의존성 문제를 해결하기 위해 Webpack이 등장
    
- Bundler
    
    ```python
    - 모듈 의존성 문제를 해결해주는 작업이 Bundling
    - Bundling 해주는 도구가 Bundler이며 Webpack은 수많은 Bundler 중에 하나
    - 모듈들을 하나로 묶어주고 묶인 파일은 하나(혹은 여러개)로 만들어짐
    - Bundling된 결과물은 개별 모듈의 실행 순서에 영향을 받지 않고 동작함
    - snowpack, parcel, rollup.js 등의 webpack 이외에도 다양한 모듈 번들러 존재
    ```
    
    ⇒ `Vue CLI는 이러한 Babel, Webpack에 대한 초기 설정이 자동으로 되어 있음`
    

### 3. package.json

- 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션을 포함

### 4. package-lock.json

- node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
- 협업 및 배포 환경에서 정확히 동일한 종속성을 설치하도록 보장하는 표현
- 사용 할 패키지의 버전을 고정
- 개발 과정 간의 의존성 패키지 충돌 방지
- `python`의 `requirements.txt` 역할

### 5. `public` folder의 index.html

- Vue 앱의 뼈대가 되는 html 파일
- Vue 앱과 연결될 요소가 있음

### 6. `src` folder

- src/assets
    - 정적 파일을 저장하는 디렉토리
- scr/components
    - 하위 컴포넌트들이 위치
- scr/App.vue
    - 최상위 컴포넌트
    - public/index.html과 연결됨
- src/main.js (별도 수정x)
    - webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry point
    - public/index.html과 src/App.vue를 연결시키는 작업이 이루어지는 곳
    - Vue 전역에서 활용 할 모듈을 등록할 수 있는 파일

## (4) Component

### 1. 개요

- UI를 독립적이고 재사용 가능한 조각들로 나눈 것
    - 즉, 기능별로 분화한 코드 조각
- CS에서는 `다시 사용`할 수 있는 `범용성`을 위해 개발된 소프트웨어 구성 요소를 의미
- 하나의 app을 구성할 때 `중첩된` 컴포넌트들의 tree로 구성하는 것이 보편적임
    - Web시간에 배운 HTML 요소들의 중첩을 떠올려 보자
        - Body tag를 root node로 하는 tree 구조
        - 마찬가지로, Vue에서는 src/App.vue를 root node로 하는 tree의 구조를 가짐
- 컴포넌트는 유지보수를 쉽게 만들어 줄 뿐만 아니라 재사용성의 측면에서도 매우 강력한 기능을 제공
    
    ![component.PNG](Vue%20CLI%2073225c46417948b5a42fc8192f812918/component.png)
    
    ⇒ Component는 `반복되는 구조`를 `미리 만들어` 놓고 함수를 호출하듯이 `사용` 하는 것!
    

### 2. Component based architecture 특징

- 관리가 용이
    - 유지/보수 비용 감소
- 재사용성
- 확장 가능
- 캡슐화
- 독립적

### 3. component in Vue

- Vue에서 말하는 comonent
    
    ⇒ 이름이 있는 재사용 가능한 Vue instance
    
- Vue instance
    
    ⇒ `new Vue( )`로 만든 인스턴스
    

## (5) SFC

### 1. 정의

- `Single File Component`
- 하나의 .vue 파일이 하나의 Vue instance이고, 하나의 컴포넌트이다.
- Vue instance에서는 HTML, CSS, JavaScript 코드를 한번에 관리
    
    ⇒ Vue instance를 기능 단위로 작성하는 것이 핵심
    

## (6) Vue Component

### 1 . 구조

- 템플릿(HTML)
    - HTML의 body 부분
    - 눈으로 보여지는 요소 작성
    - 다른 컴포넌트를 HTML 요소처럼 추가 가능
- 스크립트(JavaScript)
    - JavaScript 코드가 작성되는 곳
    - 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성됨
    
    `이전에는 const app = new Vue() 를 만드어 줬으나 이제는 파일 자체가 component 이므로 따로 정의 x` 
    
- 스타일(CSS)
    - CSS가 작성되면 컴포넌트의 스타일 담당

### 2. 구조 정리

- 컴포넌트들이 tree 구조를 이루어 하나의 페이지를 만듦
- root에 해당하는 최상단의 component가 `App.vue`
- App.vue를 index.html과 연결

⇒ index.html 파일 하나만을 rendering

⇒ SPA

## (7) Vue Component 실습

### MyComponent.vue

1. MyComponent.vue 생성
    - src/components 에 생성
    - `vue` + `tap` ⇒ 기본 틀 생성
2.  Script에 이름 등록
    
    ```python
    <script>
    export default {
      name: 'MyComponent',
    }
    </script>
    ```
    
1. template에 요소 추가
    
    ```python
    <template>
      <div>
        
      </div>
    </template>
    ```
    
    ⇒ 꼭 div가 아니어도 되지만, `최상위 태그`는 `꼭!` 지정해줘야 함
    

### Component 등록 3단계 ( django : url → view → template 처럼 암기!!)

1. 불러오기
2. 등록하기
3. 보여주기
- `App.vue`

```html
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- 3. 보여주기 --> 
    <MyComponent/>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>
```

```jsx
<script>
import HelloWorld from './components/HelloWorld.vue'

// 1. 불러오기 (아래처럼 사용하자!) @이면 .vue 파일표시르 안 써줘됨!!
// import MyComponent from './components/MyComponent.vue'
import MyComponent from '@/components/MyComponent'

export default {
  name: 'App',
  components: {
    HelloWorld,
    // 2. 등록하기
    MyComponent,
  }
}
</script>
```

```css
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
```

### 자식 컴포넌트 작성

1. 자식 관계를 표현하기 위해 기존 Mycomponent에 간단한 border를 추가
    
    ```jsx
    <template>
      <!-- div의 border class 생성 -->
      <div class="border">
        <h1>이건 이한빈 MyComponent 다! </h1>
      </div>
    </template>
    
    <script>
    export default {
      name: 'MyComponent',
    }
    </script>
    
    <style>
      /* border */
      .border {
        border: solid;
      }
    </style>
    ```
    
    ![테두리 생성.PNG](Vue%20CLI%2073225c46417948b5a42fc8192f812918/%25ED%2585%258C%25EB%2591%2590%25EB%25A6%25AC_%25EC%2583%259D%25EC%2584%25B1.png)
    
2. src/components에 MyComponentItem.vue 생성
    - 생성 3단계 진행
    
    ```jsx
    <template>
      <div>
        <h3>나는 MyComponent의 하위 컴포넌트!</h3>
      </div>
    </template>
    
    <script>
    export default {
      name: 'MyComponentItem',
    }
    </script>
    
    <style>
    
    </style>
    ```
    
3. MyComponent에 등록
    - 등록 3단계 진행
    
    ```jsx
    <template>
      <!-- div의 border class 생성 -->
      <div class="border">
        <h1>이건 이한빈 MyComponent 다! </h1>
    		<!-- 3. 보여주기 -->
        <MyComponentItem/>
      </div>
    </template>
    
    <script>
    // 1. 불러오기
    import MyComponentItem from '@/components/MyComponentItem'
    
    export default {
      name: 'MyComponent',
      components:{
        // 2. 등록하기
        MyComponentItem,
      }
    }
    </script>
    
    <style>
      /* border */
      .border {
        border: solid;
      }
    </style>
    ```
    
4.  component의 재사용성
    
    ```jsx
    <template>
      <!-- div의 border class 생성 -->
      <div class="border">
        <h1>이건 이한빈 MyComponent 다! </h1>
        <MyComponentItem/>
        <MyComponentItem/>
        <MyComponentItem/>
      </div>
    </template>
    ```
    
    ![재사용.PNG](Vue%20CLI%2073225c46417948b5a42fc8192f812918/%25EC%259E%25AC%25EC%2582%25AC%25EC%259A%25A9.png)
    
    ⇒ 3번째 단계인 `보여주기`만 하여 필요한 부분을 간단하게 반복가능