package lang.string.test;

public class TestString10 {
    /*
        split() 를 사용해서 fruits 를 분리하고, join() 을 사용해서 분리한 문자들을 하나로 합쳐라.
        실행 결과를 참고해라.
        apple
        banana
        mango
        joinedString = apple->banana->mango
    */
    public static void main(String[] args) {
        String fruits = "apple,banana,mango";
        // 코드 작성
        String[] temp = fruits.split(",");
        for (String s : temp){
            System.out.println(s);
        }
        String joinedString = String.join("->", temp);
        System.out.println("joinedString = " + joinedString);
    }
}
