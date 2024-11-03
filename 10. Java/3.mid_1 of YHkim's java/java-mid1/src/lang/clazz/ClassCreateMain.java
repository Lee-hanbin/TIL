package lang.clazz;

public class ClassCreateMain {
    /*
        getDeclaredConstructor().newInstance()
        getDeclaredConstructor() : 생성자를 선택한다.
        newInstance() : 선택된 생성자를 기반으로 인스턴스를 생성한다
    */
    public static void main(String[] args) throws Exception{
        //Class helloClass = Hello.class;
        Class helloClass = Class.forName("lang.clazz.Hello");
        Hello hello = (Hello) helloClass.getDeclaredConstructor().newInstance();
        String result = hello.hello();
        System.out.println("result = " + result);
    }
}
