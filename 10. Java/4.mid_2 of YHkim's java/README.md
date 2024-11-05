# Structure of Java Program - Mid2
  ## 1. Generic
  - BoxMain1 처럼 각각의 타입별로 IntegerBox, StringBox와 같은 클래스를 모두 정의
     - 코드 재사용 x
     - 타입 안정성 o
   - BoxMain2 처럼 ObjectBox를 사용해서 다형성으로 하나의 클래스만 정의
     - 코드 재사용 o
     - 타입 안정성 x
  ### 용어
- Generic : 타입에 속한 것이 아니라 일반적으로, 범용적으로 사용할 수 있음을 의미
- Generic Type 
  - 클래스나 인터페이스를 정의할 때 타입 매개변수를 사용하는 것을 말함
  - 제네릭 클래스, 제네릭 인터페이스를 모두 함쳐서 ㅔ네릭 타입이라 함
    ```Java
    //ex)
      class GenericBox<T> { private T t}
    //이때, GenericBox<T> 를 Generic Type이라 함
    ```
  - Tyle Parameter
    - 제네릭 타입이나 메서드에서 사용되는 변수로, 실제 타입으로 대체됨
    ```Java
    //ex)
    GenericBox<T>
    //이때, T를 Type Parameter(타입 매개변수)
    ```
  - Type Argument
    - 제네릭 타입을 사용할 때 제공되는 실제 타입
    ```Java
    //ex)
    GenericBox<Integer>
    //이때, Integer를 Type Argument(타입인자)
    ```
  