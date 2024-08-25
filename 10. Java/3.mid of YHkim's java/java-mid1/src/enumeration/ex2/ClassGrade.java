package enumeration.ex2;

/* [타입 안전 열거형 패턴]
    타입 안정성 향상: 정해진 객체만 사용할 수 있기 때문에, 잘못된 값을 입력하는 문제를 근본적으로 방지할 수 있다.
    데이터 일관성: 정해진 객체만 사용하므로 데이터의 일관성이 보장된다.
*/
public class ClassGrade {
    public static final ClassGrade BASIC = new ClassGrade();
    public static final ClassGrade GOLD = new ClassGrade();
    public static final ClassGrade DIAMOND = new ClassGrade();

    //private 생성자 추가
    private ClassGrade() {}
}
