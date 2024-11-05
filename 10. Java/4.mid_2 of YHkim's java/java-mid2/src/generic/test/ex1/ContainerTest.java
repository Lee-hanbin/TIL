package generic.test.ex1;
/*
* 다음 코드와 실행 결과를 참고해서 `Container` 클래스를 만들어라.
*`Container` 클래스는 제네릭을 사용해야 한다.
* */
public class ContainerTest {

    public static void main(String[] args) {
        Container<String> stringContainer = new Container<>();
        System.out.println("빈값 확인1: " + stringContainer.isEmpty());

        stringContainer.setItem("data1");
        System.out.println("저장 데이터: " + stringContainer.getItem());
        System.out.println("빈값 확인2: " + stringContainer.isEmpty());

        Container<Integer> integerContainer = new Container<>();
        integerContainer.setItem(10);
        System.out.println("저장 데이터: " + integerContainer.getItem());
    }
}
