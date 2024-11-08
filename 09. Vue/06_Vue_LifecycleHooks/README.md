# Lifecycle Hooks

# LifeCycle Hooks

## (1) 정의

- 각 Vue 인스턴스는 `생성`과 `소멸`의 과정 중 `단계별 초기화 과정`을 거침
    - Vue 인스턴스가 생성된 경우, 인스턴스를 DOM에 마운트하는 경우, 데이터가 변경되어 DOM을 업데이트하는 경우 등…
- 각 단계가 트리거가 되어 특정 로직을 실행할 수 있음
    
    ![Lc.PNG](Lifecycle%20Hooks%20e41c9a9904254e11b6345fd0c93e99e8/Lc.png)
    

## (2) 종류

### 1. Created

- Vue instance가 생성된 후 호출됨
- data, computed 등의 설정이 완료된 상태
- `서버에서 받은 데이터`를 vue instance의 `data에 할당하는 로직`을 `구현`하기 적합
    
    ⇒ 장고와 소통을 할 때,  acxio요청을 보내면 첫 요청을 기반으로 페이지가 생성됨
    
- 단, `mount 되지 않아` 요소에 접근할 수 없음
- JavaScript에서 학습한 Dog API 활용 실습의 경우 버튼을 누르면 강아지 사진을 보여줌
- 버튼을 누르지 않아도 `첫 실행 시` 기본 `사진이 출력`되도록 하고 싶으면 `created 함수`에 강아지 사진을 가져오는 `함수를 추가`!
    
    ```jsx
    //components/DogComponent.vue
    
    export default {
    	...
    	created() {
    		this.getDogImage()
    	},
    ```
    

### 2.mounted

- Vue instance가 요소에 mount된 후 호출됨
- mount된 요소를 조작할 수 있음
    
    ```jsx
    //components/DogComponent.vue
    export  default {
    	...
    	mounted() {
        const button = document.querySelector('button')
        button.innerText = '멍멍'
      },
    ```
    
- created의 경우, mount 되기 전이기 때문에 DOM에 접근할 수 없으므로 동작하지 않음

### 3. updated

- 데이터가 변경되어 DOM에 변화를 줄 때 호출됨
    
    ```jsx
    //components/DogComponent.vue
    export  default {
    	...
    	updated() {
        console.log('새로운 멍멍이!')
      }
    ```
    

## (3) 특징

- instance마다 각각의 Lifecycle을 가지고 있음
    
    ```jsx
    export default {
      ...
      },
      created() {
        this.getDogImage()
        console.log('Child created!')
      },
      mounted() {
        const button = document.querySelector('button')
        button.innerText = '멍멍'
        console.log('Child mounted!')
      },
      updated() {
        console.log('새로운 멍멍이!')
        console.log('Child updated!')
      }
    }
    ```
    
- Lifecycle Hooks는 컴포넌트별로 정의할 수있음
    
    ![순서.PNG](Lifecycle%20Hooks%20e41c9a9904254e11b6345fd0c93e99e8/%25EC%2588%259C%25EC%2584%259C.png)
    
    - 순서
        
        ⇒ App.vue 생성
        
        ⇒ ChildComponent 생성
        
        ⇒ ChildComponent 부착
        
        ⇒ App.vue 부착
        
        ⇒ ChildComponent 업데이트 순으로 동작
        
- 부모 컴퍼넌트의 mounted hook이 실행 되었다고 해서 자식이 mount 된 것이 아님
- 부모 컴퍼넌트가 updated hook이 실행 되었다고 해서 자식이 update된 것이 아님
    
    ⇒ 부착 여부가 부모-자식 관계에 따라 순서를 가지고 있지 않은 것
    

⇒ `instance마다 각각의 Lifecycle을 가지고 있기 때문`