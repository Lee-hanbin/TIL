package lang.string.equals;

public class StringEqualsMain1 {

    public static void main(String[] args) {
        String str1 = new String("hello");
        String str2 = new String("hello");
        System.out.println("new String() == 비교: " + (str1 == str2));            //false
        System.out.println("new String() equals 비교: " + (str1.equals(str2)));   //true

        String str3 = "hello";
        String str4 = "hello";
        //문자열 리터럴을 사용하는 경우 자바는 메모리 효율성과 성능 최적화를 위해 '문자열 풀'을 사용
        //즉, 같은 문자열인 경우 새로운 메모리 공간을 만들지 않고 원래 있는 메모리 공간을 참조한다!
        System.out.println("리터럴 == 비교: " + (str3 == str4));                 //true
        System.out.println("리터럴 equals 비교: " + (str3.equals(str4)));        //true
    }
}
