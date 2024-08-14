package poly.ex4;

public abstract class AbstractAnimal {

    //모든 메서드가 추상 메스디인 추상 클래스를 '순수 추상 클래스'라고 한다.
    //사실상 자바에는 '인터페이스'라는 용어가 있기에 '순수 추상 클래스'라는 용어를 사용x
    public abstract void sound();

    public abstract void move();
}
