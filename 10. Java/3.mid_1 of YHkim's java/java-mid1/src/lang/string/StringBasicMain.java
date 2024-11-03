package lang.string;

public class StringBasicMain {

    public static void main(String[] args) {
        //int, double, boolean 은 소문자 시작 => 기본형
        //String은 대문자 시작 => 객체
        String str1 = "hello";
        String str2 = new String("hello");

        System.out.println("str1 = " + str1);
        System.out.println("str2 = " + str2);
    }
}
