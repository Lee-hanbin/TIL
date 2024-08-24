package lang.string.builder;
/*
    String str = "A" + "B" + "C" + "D";
    String str = String("A") + String("B") + String("C") + String("D");
    String str = new String("AB") + String("C") + String("D");
    String str = new String("ABC") + String("D");
    String str = new String("ABCD");

    => String Class는 불변이기에 여러 연산작용을 할때, 과정에 있는 모든 클래스를 새로 생성해야한다
       이러한 작용은 비효율적인 방식이기에 StringBuilder를 사용하여 가변String을 만든다.
       단, 이 경우에는 사이드 이팩트 주의 (작업이 끝나면 불변String 타입으로 바꿔주면 됨)
* */
public class StringBuilderMain1_1 {

    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();

        sb.append("A");
        sb.append("B");
        sb.append("C");
        sb.append("D");
        System.out.println("sb = " + sb);

        sb.insert(4, "Java");
        System.out.println("insert = " + sb);

        sb.delete(4, 8);
        System.out.println("delete = " + sb);

        sb.reverse();
        System.out.println("reverse = " + sb);

        //StringBulder -> String
        String string = sb.toString();
        System.out.println("string = " + string);
    }
}
