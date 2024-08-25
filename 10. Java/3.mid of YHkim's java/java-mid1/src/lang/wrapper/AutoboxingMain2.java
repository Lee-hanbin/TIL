package lang.wrapper;

public class AutoboxingMain2 {

    public static void main(String[] args) {
        //Primaitive -> Wrapper
        int value = 7;
        Integer boxedValue = value; //오토 박싱(Auto-boxing

        //Wrapper -> Primitive
        int unboxedValue = boxedValue; // 오토 언박식(Auto-Unboxing)

        System.out.println("boxedValue = " + boxedValue);
        System.out.println("unboxedValue = " + unboxedValue);
    }
}
