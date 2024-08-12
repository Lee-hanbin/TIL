package extends1.super2;

public class ClassB extends ClassA{

    public ClassB(int a) {
//        super();    //기본 생성자 생략 가능
        this(a, 0); //this를 써 주더라도 한번은 super를 호출해야함 -> tihs는 아래 ClassB( a, b)이므로 super() 호출함
        System.out.println("ClassB 생성자 a=" + a);
    }

    public ClassB(int a, int b) {
        super();    //기본 생성자 생략 가능
        System.out.println("ClassB 생성자 a=" + a + " b=" + b);
    }
}
