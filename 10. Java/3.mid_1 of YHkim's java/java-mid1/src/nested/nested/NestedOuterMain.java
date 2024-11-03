package nested.nested;

public class NestedOuterMain {

    public static void main(String[] args) {
        NestedOuter Outer = new NestedOuter();
        NestedOuter.Nested nested = new NestedOuter.Nested();
        nested.print();

        System.out.println("nestedClass = " + nested.getClass());

    }
}
