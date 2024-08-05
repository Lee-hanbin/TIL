package ref;

public class NullMain1 {

    public static void main(String[] args) {
        Data data = null;
        System.out.println("1. data = " + data);
        data = new Data();
        System.out.println("1. data = " + data);
        data = null;
        System.out.println("1. data = " + data);
    }
}
