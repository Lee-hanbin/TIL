package lang.wrapper;

public class AutoboxingMain1 {

    public static void main(String[] args) {
        //Primaitive -> Wrapper
        int value = 7;
        Integer boxedValue = Integer.valueOf(value);

        //Wrapper -> Primitive
        int unboxedValue = boxedValue.intValue();

        System.out.println("boxedValue = " + boxedValue);
        System.out.println("unboxedValue = " + unboxedValue);
    }
}
