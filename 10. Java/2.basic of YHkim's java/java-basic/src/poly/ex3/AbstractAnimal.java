package poly.ex3;

public abstract class AbstractAnimal {

    // 클래스 안에 추상 메서드가 하나라도 있으면
    // 클래스 자체를 추상 클래스로 만들어야만 함
    // why? 추상 메서드는 바디가 없기에 호출되면 비정상적인 클래스로 보인다.
    public abstract void sound();

    public void move(){
        System.out.println("동물이 움직입니다.");
    }
}
