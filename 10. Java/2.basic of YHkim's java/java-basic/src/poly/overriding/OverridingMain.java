package poly.overriding;

public class OverridingMain {

    public static void main(String[] args) {

        //자식 변수가 자식 인스턴스 참조
        Child child = new Child();
        System.out.println("Child -> Child");
        System.out.println("value = " + child.value);
        child.method();

        //부모 변수가 부모 인스턴스 참조
        Parent parent = new Parent();
        System.out.println("Parent -> Parent");
        System.out.println("value = " + parent.value);
        parent.method();

        //부모 변수가 자식 인스턴스 참조(다형성 참조)
        Parent poly = new Child();
        System.out.println("Parent -> Child");
        System.out.println("value = " + poly.value);    //변수는 오버라이딩x
        poly.method();  //메서드 오버라이딩
        //메서드를 부를때는 오버라이딩 여부를 먼저 판단! child의 method가 overriding을 지정했으므로
    }
}
