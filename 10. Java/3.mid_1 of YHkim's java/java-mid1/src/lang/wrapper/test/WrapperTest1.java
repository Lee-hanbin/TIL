package lang.wrapper.test;

public class WrapperTest1 {
    /*
        문자로 입력된 str1 , str2 두 수의 합을 구하자
    */

    public static void main(String[] args) {
        String str1 = "10";
        String str2 = "20";
        // 코드 작성
        //int result = Integer.valueOf(str1) + Integer.valueOf(str2); //나
        int result = Integer.parseInt(str1) + Integer.parseInt(str2); //강사
        System.out.println("두 수의 합: " + result);
    }
}
