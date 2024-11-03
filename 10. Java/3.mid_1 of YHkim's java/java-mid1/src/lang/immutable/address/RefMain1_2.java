package lang.immutable.address;

public class RefMain1_2 {

    public static void main(String[] args) {
        //사이드 이펙트는 막을 수 있었으나, 객체의 공유를 막을 수 있는 방법이 없다.
        Address a = new Address("서울");
        Address b = new Address("서울");
        System.out.println("a = " + a);
        System.out.println("b = " + b);

        b.setValue("부산");
        System.out.println("부산 -> b");
        System.out.println("a = " + a);
        System.out.println("b = " + b);
    }
}
