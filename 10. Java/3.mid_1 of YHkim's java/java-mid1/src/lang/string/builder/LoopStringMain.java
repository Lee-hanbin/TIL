package lang.string.builder;

public class LoopStringMain {

    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();

        String result = "";

        for (int i = 0; i < 100000; i++) {
            result += "Hello Java ";
        }
    /* 위의 코드를 사실상 아래 코드로 실행시킨다.
        String result = "";
        for (int i = 0; i < 100000; i++) {
         result = new StringBuilder().append(result).append("Hello Java
        ").toString();
        }
    */
        long endTime = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println("time = " + (endTime - startTime) + "ms");   //11398ms
    }
}
