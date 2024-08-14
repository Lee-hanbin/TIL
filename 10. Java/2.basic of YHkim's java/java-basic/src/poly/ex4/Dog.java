package poly.ex4;

public class Dog extends AbstractAnimal {

    //오버라이딩 하지 않으면 컴파일 오류!
    @Override
    public void sound(){
        System.out.println("멍멍");
    }

    @Override
    public void move() {
        System.out.println("댕댕이 이동");
    }
}
