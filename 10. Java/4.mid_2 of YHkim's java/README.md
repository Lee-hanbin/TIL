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
  - 제네릭 클래스, 제네릭 인터페이스를 모두 함쳐서 제네릭 타입이라 함
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
  
### 문제점 및 해결
- 문제점
  - 타입 안정성x 문제
    - A 타입에 B 타입의 정보를 전달하는 문제 발생
    - 다형성을 입힌 C타입을 사용했을 때, 반환하기 때문에 다운 캐스팅 필요
    - 실수로 B타입을 입력했는데, A 타입을 반환해야하는 상황이면 캐스팅 예외가 발생
  - 제네릭 도입 문제
    - 제네릭에서 타입 매개변수를 사용하면 어떤 타입이든 들어올 수 있다.
    - 어떤 타입이든 수용할 수 있는 Object로 가정하고, Object의 기능만 사용가능
- 해결
  - 제네릭에 `타입 매개변수 상한`을 사용해서 타입 안정성을 지키면서 상위 타입의 원하는 기능까지 사용!
    => 코드 재사용과  타입 안전성이라는 두 마리 토끼를 동시에 잡음!

### Generic Method
- 정의
  ```Java
  //ex
  <T> T genericMethod(T t)
  ```
- 타입 인자 전달
  `GenericMethod.<Integer>genericMethod(i)`

- 제네릭 메서드는 클래스 전체가 아니라 특정 메서드 단위로 제네릭을 도입할 때 사용
- 제네릭 메서드를 정의할 때는 메서드의 반환 타입 왼쪽에 다이아몬드를 사용해서 `<T>`와 같이 타입 매개변수를 적어준다.
- 제네릭 메서드는 메서드를 실제 호출하는 시점에 다이아몬드를 사용해서 `<Integer>`와 같이 타입을 정하고 호출한다.
- 제네릭 메서드의 행심은 메서드를 호출하는 시점에 타입 인자를 전달해서 타입을 지정하는 것이다. 따라서 타입을 지정하면서 메서드를 호출한다.
  ```Java
  class Box<T> { //제네릭 타입
    static <V> V staticMethod2(V t) {} //static 메서드에 제네릭 메서드 도입
    <Z> Z instanceMethod2(Z z) {} //인스턴스 메서드에 제네릭 메서드 도입 가능
  }
  ```
  => 제네릭 타입은 static 메서드에 타입 매개변수를 사용할 수 없다. 제네릭 타입은 객체를 생성하는 시점에 타입이 정해진다. 하지만 static 메서드는 인스턴스 단위가 아니라 클래스 단위로 작동하기 때문에 제네릭 타입과는 무관하다. 따라서 static 메서드에 제네릭을 도입하려면 제네릭 메서드를 사용해야 한다.
  ```Java
  class Box<T> {
    T instanceMethod(T t) {} //가능
    static T staticMethod1(T t) {} //제네릭 타입의 T 사용 불가능
  }
  ```
- `제네릭 타입`보다 `제네릭 메서드`가 항상 우선순위가 높다.

### Wildcard
- `*`, `?` 와 같이 하나 이상의 문자들을 상징하는데 여기서 와일드 카드는 여러 타입이 들어올 수 있다는 뜻이다.
- 제네릭 타입을 조금 더 편리하게 사용할 수 있게 한다.
- 와일드카드는 제네릭 타입이나, 제네릭 메서드를 선언하는 것이 아니라, 이미 만들어진 제네릭 타입을 활용할 때, 사용한다.
- 예시
  ```Java
    //GenericMethod
  static <T extends Animal> T printGenericV3(Box<T> box) {
        T t = box.get();
        System.out.println("이름 = " + t.getName());
        return t;
    }

    //Wildcard - Animal 클래스의 모든 자식 가능
    static Animal printWildcardV3(Box<? extends Animal> box) {
        Animal animal = box.get();
        System.out.println("이름 = " + animal.getName());
        return animal;
    }
  ```


### Type eraser
- eraser는 지우개라는 뜻
- 제네릭은 자바 컴파일 단계에서만 사용되고, 컴파일 이후에는 제네릭 정보가 삭제된다. 즉, 제네릭에 사용된 타입 매개변수가 모두 사라지는 것이다. 
  ```
  컴파일 전인 .java에는 제네릭의 타입 매개변수가 존재하지만, 컴파일 이후인 자바 바이트코드 .class 에는 타입 매개변수가 존재하지 않는다.
  ```
- 자바의 제네릭 타입은 컴파일 시저멩만 존재하고, 런타임 시에는 제네릭 정보가 지워지는데, 이것을 타입 이레이저라 하낟.