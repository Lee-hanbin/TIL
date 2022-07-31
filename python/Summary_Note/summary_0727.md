# OOP(Object-Oriented Programming)

## 1. 정의

- 컴퓨터 프로그래밍의 패러다임 중 하나로 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 열 개의 독립된 단위

- '객체'들의 모임으로 파악하고자 하는 것
  
  - **객체**
    
    - 정보를 주고 받고 데이터를 처리할 수 있음.
    
    - **정보(변수)** + **행동(함수)**  
    
    - **꾸러미**라고 생각!
  
  c.f) 절차지향 프로그래밍
  
  - 1개의 정보에 각종 행동을 연결시켜 놓음
    
    - 한 곳의 내용을 바꾸면 다른 곳에 영향을 줄 수 있음

- **필요한 이유**
  
  - 복잡한 현실 세계에서 모든 것을 디테일하게 알고 사용할 수 없기 때문에 
    
    추상화를 통하여 복잡한 것을 숨기고 필요한 것만 보여 준다.

- **장점**
  
  - 클래스 단위로 모듈화 시켜 개발 할 수 있음
    
    - 많은 인원이 참여하는 대규모 소프트웨어 개발에 적합
  
  - 필요한 부분만 수정하기 쉽기 때문에 프로그램의 유지보수가 원활

- **단점**
  
  - 설계 시 많은 노력과 시간이 필요
    
    - 다양한 객체들의 상호 작용 구조를 만들기 위해 많은 시간과 노력이 필요
  
  - 실행 속도가 상대적으로 느림 ( 사람이 편한 만큼 컴퓨터가 힘듦)

## 2. OOP 기초

##### (1) 객체

- **클래스에서 정의한 것을 토대로 메모리(실제 저장공간)에 할당된 것**으로 프로그램에서 사용되는 데이터 또는 식별자에 의해 참조되는 공간을 의미
  
  ex) 변수, 자료 구조, 함수 

- `속성`과 `행동` 으로 구성된 모든 것

- 특징
  
  - **타입** : 어떤 연산자와 조작이 가능한가
  
  - **속성** : 어떤 상태(데이터)를 가지는가?
  
  - **조작법** : 어떤 행위(함수)를 할 수 있는가?
  
  - 객체 = 속성(Attribute) + 기능(Method)

##### (2) 객체와 클래스 문법

- 기본문법
  
  - 클래스 정의    : `class MyClass:`  **(class가 소문자!)**
  
  - 인스턴스 생성 : `my_instance = MyClass`
  
  - 메서드 호출   : `my_instance.my_method()`
  
  - 속성               :  `my_instance.my_attribute`

## 3. OPP 속성

##### (1) 속성

- 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미

- 클래스 변수 / 인스턴스 변수가 존재

##### (2) 인스턴스 변수

- 정의
  
  - 인스턴스가 개인적으로 가지고 있는 속성
  
  - 각 인스턴스들의 고유한 변수

- 생성자 메서드에서 **self.< name >** 으로 정의 

- 인스턴스가 생성된 이후 **< instance >. < name >** 으로 접근 및 할당

##### (3) 클래스 변수

- 한 클래스의 모든 인스턴스가 공유하는 값

- 같은 클래스의 인스턴스들은 같은 값을 갖게 됨

- 클래스 선언 내부에서 정의
  
  ```
  - 즉, 클래스 상자 내부에 인스턴스라는 작은 상자들이 있을 때, 
   클래스 상자에서 정의된 변수는 작은 상자들이 모두 공유한다는 의미
  ```
  
  ex) `클래스명`+`.`+`클래스 변수이름` 으로 접근 및 할당해야함

## 4.  OOP 메서드

##### (1) 인스턴스 메서드

- 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메서드

- 호출 시 , 첫번째 인자로 인스턴스 자기자신인`self`가 전달됨
  
  - 꼭 self로 적지 않아도 되지만, 암묵적인 규칙

- **생산자 메서드**
  
  - 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
  
  ```python
  def __init__ (self, *args):
      pass:
  ```

- **매직 메서드**
  
  - 던더 (Double underscore) `__`
  
  - 특수한 동작을 위해 만들어진 메서드로, 스페션 메서드 or 매직 메서드로 불림
  
  - 특정 상황에 자동으로 불리는 메서드
    
    ex) `__str__(self)` : `print` 함수가 호출될 때 자동으로 호출

- **소멸자 메서드**
  
  - 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메서드
  
  ```python
  class Hobby:
      def __del__(self):
          pass
  ho1 = Hobby()
  del ho1
  ```

##### (2) 클래스 메서드

- 클래스가 사용할 메서드

- `@classmethod` 데코레이터를 사용하여 정의

- 호출 시, 첫번쟤 인자로 클래스인 `cls`가 전달됨
  
  ```python
  class Hobby:
      count = 0 # 클래스 변수
      def __init__(self, name):
          self.name = name
          Person.count += 1
  
      @classmethod
      def num_of_population(cls):
          print(f'인구수는 {cls.count}입니다.')
  
  ho1 = Hobby('농구')
  ho2 = Hobby('축구')
  print(Hobby.count)            #2
  
  Person.num_of_population()    #인구수는 2입니다.
  ```

##### (3) 데코레이터

- 정의
  
  - 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
  
  - `@데코레이터(함수명)` 형태로 함수 위에 작성
  
  - 순서대로 적용 되기 때문에 작성 순서가 중요
  
  ```python
  # 데코레이터 없이 함수 꾸미기
  def hello():
      print("hello")
  
  def add_print(original):
      def wrapper():
          print("함수 시작")
          original()
          print("함수 끝")
      return wrapper
  
  hello()
  # 함수를 인자로 하는 함수는 함수(함수)
  add_print(hello)()
  # "함수 시작"
  # "hello"
  # "함수 끝"
  
  print_hello = add_print(hello)
  print_hello()
  ```
  
  ```python
  # 데코코레이터를 활용하면 쉽게 여러 함수를 원하는대로 변경 가
  def add_print(original):
      def wrapper():
          print("함수 시작")
          original()
          print("함수 끝")
      return wrapper
  
  @add_print
  def print_hello():
      print("hello")
  
  print_hello()
  ```

##### (4) 스태틱 메서드

- 정의

- 인스턴스 변수, 클래스 변수 아무것도 사용하지 않을 경우 사용.
  
  - 즉, 객체 상태나 클래스 상태를 수정할 수 없음

- `@staticmethod` 데코레이터를 사용하여 정의
  
  - 일반 함수처럼 동작하지만, 클래스의 이름공간에 귀속됨
    
    - 주로 해당 클래스로 한정하는 용도로 사용

##### (5)  인스턴스와 클래스 간의 이름공간(namespace)

- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성

- 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성

- 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색

## 5. 객체 지향의 핵심개념

##### (1) 추상화

- 정의

- 현실 세계를 프로그램 설계에 반영.
  
  (즉, 복잡한 것은 숨기고, 필요한 것만 들어내기)

##### (2) 상속

- 정의

- 두 클래스 사이 부모-자식 관계를 정립
  
  - 자식 class는 부모 class에게 정보,행동을 받아서 사용가능

- 클래스는 상속이 가능함
  
  - 모든 파이썬 클래스는 객체를 상속 받음

- 예시

- `class ChildClass(ParentClass):`

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):                              # 이부분이 중복되므로
        print(f'반갑습니다. {self.name}입니다.')   # 부모 클래스에게 정의

class Professor(Person):                         
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

p1 = Professor('박교수', 34, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

p1.talk()
s1.talk()
```

- 상속 관련 함수와 메서드
  
  - `isinstance( object, classinfo )`
    
    - classinfo의 instance거나 subclass인 경우 True
  
  - `issubclass( class, classinfo )`
    
    - class가 classinfo의 subclass이면 True
  
  - `super`
    
    - 자식클래스에서 부모클래스를 사용하고 싶을 경우
    
    - `super()__init__(*arg)` : **self를 적지 않음을 주의!!!**
    
    ```python
    class Person:
        def __init__(self, name, age, number, email):
            self.name = name
            self.age = age
            self.number = number
            self.email = email
    
    class Student(Person):
        def __init__(self, name, age, number, email, student_id):
            super().__init__(name, age, number, email)
            self.student_id = student_id
    ```

- 다중 상속
  
  - 두 개 이상의 클래스를 상속 받는 경우
  
  - 상속받은 모든 클래스의 요소를 활용 가능
  
  - 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정
    
    **주의!**
    
    ```python
    class Person:
        def __init__(self, name):
            self.name = name
        def greeting(self):
            return f'안녕, 난 {self.name}이야'
    
    class M(Person):
        gen = 'XX'
        def talk(self):
            return '날씬'
    
    class D(Person):
        gen = 'XY'
        def talk(self):
            return '뚱뚱'
    
    class family(D, M):
        def Kim(slef):
            return 'sumi'
        def Lee(self):
            return 'hanbin'
    
    baby = family('응애')
    print(baby.gen)        #XY
    # family 클래스에 두 부모 클래스가 존재하고  각 클래스에 gen이라는   
    # 클래스 변수가 존재한다. 하지만, D라는 부모 클래스가 먼저 매개변수로 
    # 정의 되어 있으므로 'XY'가 출력된다.
    ```

- **mro 메서드**
  
  - 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
  
  - `클래스명.mro()` 
    
    `인스턴스 => 클래스` 에서 `인스턴스 => 자식 클래스 => 부모 클래스`



##### (3) 다양성

- 정의
  
  - 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음
  
  - 서로 다른 클래스에 속해 있는 객체들이 동일한 메세지에 대해 다른 방식으로 응답할 수 있음

- 메서드 오버라이딩
  
  - 메서드 덮어쓰기
  
  - 클래스 상속 시, 부모 클래스에서 정의한 메서드를 자식 클래스에서 변경
  
  - 부모 클래스의 메서드 이름과 기본 기능은 그대로 사용하나 특정 기능을 바꾸고 싶을 때 사용
    
    즉, 이름 납두고 내용만 변경하고 싶을 때 사용
    
    

##### (4) 캡슐화

- 정의
  
  - 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 엑세스 차단
    
    ex) 주민등록 번호

- 접근제어자 종류
  
  - Public Access Modifier
    
    - 언더바(`_`) 없이 사작
    
    - 대부분 public변수
  
  - Protected Access Modifier
    
    - 언더바(`_`) 한 개로 시작
    
    - 암묵적으로 부모 클래스 내부와 자식 클래스에서만 호출가능
    
    - `print(p1_age)`하면 출력은 되지만, 지양해야함
  
  - Private Access Modifier
    
    - 언더바(`__`) 두 개로 시작
    
    - 실제로 호출 및 조회를 막는 것
    
    - `print(p1_age)`하면 error 발생

- `getter method`
  
  - 변수가 값을 읽는 메서드
  
  - `@property` 데코레이터 사용

- `setter method`
  
  - 변수가 값을 설정하는 성격의 메서드
  
  - `@변수.setter` 사용
