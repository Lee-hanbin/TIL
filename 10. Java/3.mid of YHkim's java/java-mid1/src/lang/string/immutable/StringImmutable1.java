package lang.string.immutable;

public class StringImmutable1 {

    public static void main(String[] args) {
        String str = "hello";
        str.concat(" java");
        //만약 String 내부의 값을 변경할 수 있다면,
        // 기존에 문자열 풀에서 같은 문자를 참조하는 변수의 모든 문자가 함께 변경되어 버림
        //따라서 두 변수 모두 변하는 사이드 이펙트 발생할 수 있다.
        //다만, String 클래스는 불변으로 설정되어 있기에 이러한 문제가 발생하지 않는다.
        //그렇기에 결국 str의 값은 변하지 않는다.
        System.out.println("str = " + str); //hello
    }
}
