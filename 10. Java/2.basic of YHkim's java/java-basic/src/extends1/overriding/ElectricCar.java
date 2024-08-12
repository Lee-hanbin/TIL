package extends1.overriding;


public class ElectricCar extends Car {  // extends Car를 적으면 Car 클래스의 속성을 물려받음

    @Override //부모 메서드와 동일한 메서드는 오버라이딩 가능
    public void move(){
        System.out.println("전기차를 빠르게 이동합니다.");
    }

    public void charge(){
        System.out.println("충전합니다.");
    }
}
