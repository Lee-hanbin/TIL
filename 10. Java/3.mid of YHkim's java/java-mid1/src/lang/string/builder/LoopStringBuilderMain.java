package lang.string.builder;

public class LoopStringBuilderMain {

    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();

        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < 100000 ; i++) {
            sb.append("Hello Java ");
        }
        String result = sb.toString();

        long endTime = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println("time = " + (endTime - startTime) + "ms"); //14ms
    }
}
