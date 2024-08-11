package static2;

public class ValueDataMain {

    //main 이 정적(static) method 이기 떄문에 static method 만 사용가능
    public static void main(String[] args) {
        ValueData valueData = new ValueData();
        add(valueData);
    }

    //static method만 사용가능
    static void add(ValueData valueData) {
        valueData.value++;
        System.out.println("숫자 증가 value=" + valueData.value);
    }
}
