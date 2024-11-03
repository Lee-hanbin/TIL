package generic.ex1;

public class BoxMain2 {

    public static void main(String[] args) {
        ObjectBox integerBox = new ObjectBox();
        integerBox.set(10);

//        Object object = objectBox.get();
//        Integer integer = (Integer) object;

        // ctrl + alt + n => 이때 object라는 변수에 커서를 놓고 해야함
        // 두 줄을 그래그 해서 하면 적용 x
        Integer integer = (Integer) integerBox.get(); //Object -> Integer 캐스팅
        System.out.println("integer = " + integer);

        ObjectBox stringBox = new ObjectBox();
        stringBox.set("hello");
        Object str = (String) stringBox.get(); //Object -> String 캐스팅
        System.out.println("str = " + str);


        //잘못된 값의 인수 전달시
        integerBox.set("문자100");
        Integer result = (Integer) integerBox.get(); //String -> Integer 캐스팅 예외
        System.out.println("result = " + result);
    }
}
