package lang.math.test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class LottoGeneratorMain {
    /*
        로또 번호를 자동으로 만들어주는 자동 생성기를 만들자
        로또 번호는 1~45 사이의 숫자를 6개 뽑아야 한다.
        각 숫자는 중복되면 안된다.
        실행할 때 마다 결과가 달라야 한다
    */
    //강사님 풀이
    public static void main(String[] args) {
        LottoGenerator generator = new LottoGenerator();
        int[] lottoNumbers = generator.generate();

        // 생성된 로또 번호 출력
        System.out.print("로또 번호: ");
        for (int lottoNumber : lottoNumbers) {
            System.out.print(lottoNumber + " ");
        }
    }
}
