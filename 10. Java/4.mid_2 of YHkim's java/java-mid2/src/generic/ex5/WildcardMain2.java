package generic.ex5;

import generic.animal.Animal;
import generic.animal.Cat;
import generic.animal.Dog;

public class WildcardMain2 {

    public static void main(String[] args) {
        Box<Object> objbox = new Box<>();
        Box<Animal> animalBox = new Box<>();
        Box<Dog> dogbox = new Box<>();
        Box<Cat> catbox = new Box<>();

        //Animal 포함 상위 타입 전달 가능
        writeBox(objbox);
        writeBox(animalBox);
        //writeBox(dogbox); //하한이 Animal
        //writeBox(catbox); //하한이 Animal

        Animal animal = animalBox.get();
        System.out.println("animal = " + animal);
    }

    static void writeBox(Box<? super Animal> box) {
        box.set(new Dog("멍멍이", 100));
    }
}
