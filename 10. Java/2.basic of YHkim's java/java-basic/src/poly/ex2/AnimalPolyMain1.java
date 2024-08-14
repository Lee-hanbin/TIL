package poly.ex2;

public class AnimalPolyMain1 {

    public static void main(String[] args) {

        //Overriding으로 해결 [ 다형적 참조 ]
        Animal dog = new Dog();
        Animal cat = new Cat();
        Animal caw = new Caw();

        soundAnimal(dog);
        soundAnimal(cat);
        soundAnimal(caw);
    }

    private static void soundAnimal(Animal animal){
        System.out.println("동물 소리 테스트 시작");
        animal.sound();
        System.out.println("동물 소리 테스트 종료");
    }
}
