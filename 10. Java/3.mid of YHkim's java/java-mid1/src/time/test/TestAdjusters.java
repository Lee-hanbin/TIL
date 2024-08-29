package time.test;


import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.temporal.TemporalAdjusters;

public class TestAdjusters {

    /*
        입력 받은 월의 첫날 요일과 마지막날 요일을 구해라.
    */
    public static void main(String[] args) {
        int year = 2024;
        int month = 1;
        // 코드 작성

        LocalDate date = LocalDate.of(year, month, 1);
        DayOfWeek firstOfWeek = date.getDayOfWeek();
        DayOfWeek lastOfWeek = date.with(TemporalAdjusters.lastDayOfMonth()).getDayOfWeek();
        System.out.println("firstDayOfWeek = " + firstOfWeek);
        System.out.println("lastDayOfWeek = " + lastOfWeek);
    }
}
