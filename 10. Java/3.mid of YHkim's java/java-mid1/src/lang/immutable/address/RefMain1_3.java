package lang.immutable.address;

public class RefMain1_3 {

    public static void main(String[] args) {
        Address a = new Address("서울");
        Address b = a;
        System.out.println("a = " + a);
        System.out.println("b = " + b);

        //실무에서 change라는 메서드의 구성을 모른 상태에서 컴파일 해보면
        //a의 값도 변경되었다는 사실을 알기위해 메서드를 찾아봐야함
        //따라서 이러한 공유를 막을 수는 없기에 불변 객체를 도입해야한다.
        change(b, "부산");
        System.out.println("a = " + a); //부산
        System.out.println("b = " + b); //부산
    }

    private static void change(Address address, String changeAddress) {
        System.out.println("주소 값을 변경합니다 -> " + changeAddress);
        address.setValue(changeAddress);
    }
}
