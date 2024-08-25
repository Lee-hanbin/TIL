package lang.math.test;

import java.util.*;
import java.lang.*;

public class Lotto {
    /*
        로또 번호를 자동으로 만들어주는 자동 생성기를 만들자
        로또 번호는 1~45 사이의 숫자를 6개 뽑아야 한다.
        각 숫자는 중복되면 안된다.
        실행할 때 마다 결과가 달라야 한다
    */
    public static void main(String[] args) {
        Random random = new Random();
        int lottoNum = random.nextInt(45) + 1;
        Integer[] lottoBox = {lottoNum};
        int i = 1;

        while (i < 6){
            Boolean chk = true;
            lottoNum = random.nextInt(45) + 1;
            for (int number : lottoBox) {
                if (number == lottoNum) {
                    chk = false;
                    break;
                }
            }
            if (chk) {
                List<Integer> temp = new ArrayList(Arrays.asList(lottoBox));
                temp.add(lottoNum);
                lottoBox = temp.toArray(lottoBox);
                i++;
            }
        }
        System.out.println(Arrays.toString(lottoBox));
    }
}
