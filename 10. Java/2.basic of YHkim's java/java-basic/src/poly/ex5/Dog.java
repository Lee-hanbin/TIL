package poly.ex5;

// 인터페이스는 상속이라고 하지 않고 구현(implemnets)로 표현한다.
public class Dog implements InterfaceAnimal{

    @Override
    public void sound() {
        System.out.println("멍멍");
    }

    @Override
    public void move() {
        System.out.println("댕댕이 이동");
    }
}
