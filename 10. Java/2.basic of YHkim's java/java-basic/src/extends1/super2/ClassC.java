package extends1.super2;

public class ClassC extends ClassB{


    //상속 관계를 사용하면 자식 클래스의 생성자에서 부모 클래스의 생성자를 반드시 호출해야 한다.
    public ClassC() {
        super(10, 20);
        System.out.println("ClassC 생성자");
    }
}
