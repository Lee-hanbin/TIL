package lang.immutable.address;

public class RefMain2 {

    public static void main(String[] args) {
        ImmutableAddress a = new ImmutableAddress("서울");
        ImmutableAddress b = a; //참조값 대입을 막을 수 있느 방법이 없다. (문법상 문제x)
        System.out.println("a = " + a);
        System.out.println("b = " + b);

        //b.setValue("부산"); //컴파일 오류 발생
        //불변이라는 단순한 제약을 사용해서 사이드 이펙트라는 큰 문제를 막을 수 있다.
        b = new ImmutableAddress("부산");
        System.out.println("부산");
        System.out.println("a = " + a);
        System.out.println("b = " + b);
    }
}
