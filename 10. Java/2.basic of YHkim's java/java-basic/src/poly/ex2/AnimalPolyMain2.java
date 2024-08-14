package poly.ex2;

public class AnimalPolyMain2 {

    public static void main(String[] args) {
/*
        Dog dog = new Dog();
        Cat cat = new Cat();
        Caw caw = new Caw();
*/

        Animal[] animalArr = {new Dog(), new Cat(), new Caw(), new Duck()};

        for (Animal animal : animalArr){
            //ctrl + alt + M : 메서드로 자동 생성
//            System.out.println("동물 소리 테스트 시작");
//            animal.sound();
//            System.out.println("동물 소리 테스트 종료");

            soundAnimal(animal);
        }
    }

    private static void soundAnimal(Animal animal) {
        System.out.println("동물 소리 테스트 시작");
        animal.sound();
        System.out.println("동물 소리 테스트 종료");
    }

}
