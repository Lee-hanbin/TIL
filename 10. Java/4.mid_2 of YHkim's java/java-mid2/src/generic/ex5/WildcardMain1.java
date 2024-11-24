package generic.ex5;

import generic.animal.Animal;
import generic.animal.Cat;
import generic.animal.Dog;

public class WildcardMain1 {

    public static void main(String[] args) {
        Box<Object> objbox = new Box<>();
        Box<Dog> dogbox = new Box<>();
        Box<Cat> catbox = new Box<>();

        dogbox.set(new Dog("멍멍이", 100));

        WildcardEx.printGenericV1(dogbox);
        WildcardEx.printWildcardV1(dogbox);

        WildcardEx.printGenericV2(dogbox);
        WildcardEx.printWildcardV2(dogbox);

        Dog dog = WildcardEx.printAndReturnGenericV3(dogbox);

        catbox.set(new Cat("냐옹이", 200));
        Cat cat = WildcardEx.printAndReturnGenericV3(catbox);


        Animal animal = WildcardEx.printAndReturnWildcardV3(dogbox);
    }
}
