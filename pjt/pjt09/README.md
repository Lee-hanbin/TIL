# PJT09

# Vue를 활용한 SPA 구성

## 1. 프로젝트 목표

- 영화 정보를 제공하는 SPA 제작
- AJAX 통신과 JSON 구조에 대한 이해
- Vue CLI, Vue Router 플러그인 활용하기

## 2. 개발도구

- `Visual Studio Code`
- `Google Chrome`
- `Django 3.2+`
- `bootstrap 5`
- `Node.js LTS`
- `Vue.js 2.x`
- `css`

## 3. 사용 API

- TMDB API (필수)
    
    [https://developers.themoviedb.org/3/movies/get](https://developers.themoviedb.org/3/movies/get) top rated movies
    

## 4. 컴포넌트 구조

![캡처.PNG](PJT09%20871051b6a3f44e5abf07b65ce1f21de6/%25EC%25BA%25A1%25EC%25B2%2598.png)

## 5. 프로젝트 과정

### (1) INDEX

- 최고 평점 영화 출력
    - AJAX 통신을 이용하여 TMDB API로 부터 JSON 데이터를 받아와 출력.
- 최고 평점 영화 중 랜덤 영화 한 개 출력
    - 최고 평점 영화 목록 중 랜덤으로 한 개를 출력
- 보고 싶은 영화 등록 및 삭제하기
    1. 보고 싶은 영화 제목을 등록할 수 있는 From이 출력
    2. 등록된 영화 제목을 클릭하면 취소선이 그어짐

### (2) 과정

- 최고 평점 영화 출력
    - `store/index.js`
        - movieList 에 getMovie 함수를 이용하여 API의 최고 평점 영화를 가져오기
    - `router/index.js`
        - MovieView conpoent 의 경로를 설정 합니다.
    - `MovieView.vue`
        - `MovieCard.vue` 의 부모로서 Props를 이용해 영화에 대한 데이터를 하나씩 상속
    - `MovieCard.vue`
        - `MovieView.vue` 로 부터 상속 받은 데이터를 통해 이미지, 타이틀, 줄거리를 출력
- 최고 평점 영화 중 랜덤 영화 한 개 출력
    - `router/index.js`
        - RandomView conpoent 의 경로를 설정 합니다.
    - `RandomView.vue`
        - Pick 버튼을 클릭하면 random으로 영화 정보를 받아와 출력
- 보고 싶은 영화 등록 및 삭제하기
    - 

## 6. 리뷰

## (1) 힘들었던 부분

## (2) 느낀점