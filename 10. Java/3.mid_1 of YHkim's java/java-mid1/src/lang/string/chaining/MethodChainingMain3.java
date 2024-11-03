package lang.string.chaining;

public class MethodChainingMain3 {

    public static void main(String[] args) {

        /*
            adder.add(1).add(2).add(3).getValue() //value=0
            x001.add(1).add(2).add(3).getValue() //value=0, x001.add(1)을 호출하면 그 결과로 x001을 반환한다.
            x001.add(2).add(3).getValue() //value=1, x001.add(2)을 호출하면 그 결과로 x001을 반환한다.
            x001.add(3).getValue() //value=3, x001.add(3)을 호출하면 그 결과로 x001을 반환한다.
            x001.getValue() //value=6
            6
        */

        ValueAdder adder = new ValueAdder();
        int result = adder.add(1).add(2).add(3).getValue();
        System.out.println("result = " + result);
    }
}
