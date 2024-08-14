package poly.ex5;

// 인터페이스는 상속이라고 하지 않고 구현(implemnets)로 표현한다.
public class Cat implements InterfaceAnimal{

    @Override
    public void sound() {
        System.out.println("냐옹");
    }

    @Override
    public void move() {
        System.out.println("냐옹이 이동");
    }
}
