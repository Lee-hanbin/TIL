package generic.test.ex3.unit;

/*
다음 코드와 실행 결과를 참고해서 `UnitUtil` 클래스를 만들어라.
`UnitUtil.maxHp()` 메서드의 조건은 다음과 같다.
두 유닛을 입력 받아서 체력이 높은 유닛을 반환한다. 체력이 같은 경우 둘 중 아무나 반환해도 된다.
제네릭 메서드를 사용해야 한다.
입력하는 유닛의 타입과 반환하는 유닛의 타입이 같아야 한다.
 */
public class BioUnit {

    private String name;
    private int hp;

    public BioUnit(String name, int hp) {
        this.name = name;
        this.hp = hp;
    }


    public String getName() {
        return name;
    }

    public int getHp() {
        return hp;
    }

    @Override
    public String toString() {
        return "BioUnit{" +
                "name='" + name + '\'' +
                ", hp=" + hp +
                '}';
    }
}
