package lang.object.tostring;

public class ToStringMain1 {

    public static void main(String[] args) {
        Object object = new Object();
        String string = object.toString();

        //toString() 반환값 출력
        System.out.println(string); //java.lang.Object@b4c966a

        //object 직접 출력
        System.out.println(object); //java.lang.Object@b4c966a (같음!)
        //Object 가 제공하는 toString() 메서드는 기본적으로 패키지를 포함한 객체의 이름과 객체의 참조값(해시
        //코드)를 16진수로 제공한다.
    }
}
