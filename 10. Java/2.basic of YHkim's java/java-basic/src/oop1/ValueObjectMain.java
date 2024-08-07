package oop1;

public class ValueObjectMain {

    public static void main(String[] args) {
        ValueData valueData = new ValueData();

        valueData.add();
        valueData.add();
        valueData.add();
        System.out.println("최종 숫자=" + valueData.value);
    }
}
