package enumeration.ex3;

public enum Grade {
    BASIC, GOLD, DIAMOND
}
/* 아래 코드를 위의 코드로 사용할 수 있음 [열거형 클래스]

public class Grade extends Enum {
    public static final Grade BASIC = new Grade();
    public static final Grade GOLD = new Grade();
    public static final Grade DIAMOND = new Grade();
    //private 생성자 추가
    private Grade() {}
}
*/
