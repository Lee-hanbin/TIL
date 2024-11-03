package time;

import java.time.LocalDate;

public class LocalDateMain {

    public static void main(String[] args) {
        LocalDate nowDate = LocalDate.now();
        LocalDate ofDate = LocalDate.of(2013, 11, 21);
        System.out.println("nowDate = " + nowDate);
        System.out.println("ofDate = " + ofDate);

        //계산(불변)
        LocalDate plusDays = ofDate.plusDays(10);
        System.out.println("지정 날짜+10d = " + plusDays);
    }
}
