package poly.ex4;

public class Duck extends AbstractAnimal {

    @Override
    public void sound() {
        System.out.println("꽉꽉");
    }

    @Override
    public void move() {
        System.out.println("오리궁딩이 이동");
    }
}
