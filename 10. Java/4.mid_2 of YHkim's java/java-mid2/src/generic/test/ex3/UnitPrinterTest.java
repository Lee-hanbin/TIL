package generic.test.ex3;

import generic.test.ex3.unit.Marine;
import generic.test.ex3.unit.Zealot;
import generic.test.ex3.unit.Zergling;

/*
    앞서 문제에서 만든 `Shuttle` 을 활용한다.
    다음 코드와 실행 결과를 참고해서 `UnitPrinter` 클래스를 만들어라.
    `UnitPrinter` 클래스의 조건은 다음과 같다.
    `UnitPrinter.printV1()` 은 제네릭 메서드로 구현해야 한다.
    `UnitPrinter.printV2()` 는 와일드카드로 구현해야 한다.
    이 두 메서드는 셔틀에 들어있는 유닛의 정보를 출력한다.
 */
public class UnitPrinterTest {

    public static void main(String[] args) {
        Shuttle<Marine> shuttle1 = new Shuttle<>();
        shuttle1.in(new Marine("마린", 40));

        Shuttle<Zergling> shuttle3 = new Shuttle<>();
        shuttle3.in(new Zergling("저글링", 30));

        Shuttle<Zealot> shuttle2 = new Shuttle<>();
        shuttle2.in(new Zealot("질럿", 100));

        UnitPrinter.printV1(shuttle1);
        UnitPrinter.printV2(shuttle1);
    }
}
