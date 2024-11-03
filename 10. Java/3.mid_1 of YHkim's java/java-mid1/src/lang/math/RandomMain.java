package lang.math;

import java.util.Random;

public class RandomMain {
    /*
        random.nextInt() : 랜덤 int 값을 반환한다.
        nextDouble() : 0.0d ~ 1.0d 사이의 랜덤 double 값을 반환한다.
        nextBoolean() : 랜덤 boolean 값을 반환한다.
        nextInt(int bound) : 0 ~ bound 미만의 숫자를 랜덤으로 반환한다. 예를 들어서 3을 입력하면 0, 1, 2 를 반환한다.
    */
    public static void main(String[] args) {
        Random random = new Random();
        //Random random = new Random(1); //seed가 같으면 Random의 결과가 같다.

        int rnadomInt = random.nextInt();
        System.out.println("rnadomInt = " + rnadomInt);

        double randomDouble = random.nextDouble();
        System.out.println("randomDouble = " + randomDouble);

        boolean randomBoolean = random.nextBoolean();
        System.out.println("randomBoolean = " + randomBoolean);

        //범위 조회
        int randomRange1 = random.nextInt(10);
        System.out.println("0 ~ 9: " + randomRange1);

        int randomRange2 = random.nextInt(10) + 1;
        System.out.println("1 ~ 10: " + randomRange2);
    }
}
