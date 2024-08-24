package lang.string.test;

public class TestString6 {
    /*
        str 에서 key 로 주어지는 문자를 찾고, 찾은 문자의 수를 출력해라.
        indexOf() 를 반복문과 함께 풀면 된다.
    */
    public static void main(String[] args) {
        String str = "start hello java, hello spring, hello jpa";
        String key = "hello";

        int count = 0;
        // 코드 작성
        for ( int i = 0; i < str.length() - key.length(); i++) {

            if (str.substring(i, i + key.length()).equals(key))
            {
                count++;
            }
        }

        System.out.println("count = " + count);

    }
}
