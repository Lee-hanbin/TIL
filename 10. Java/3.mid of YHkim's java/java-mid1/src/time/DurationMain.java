package time;

import java.time.Duration;
import java.time.LocalTime;

public class DurationMain {

    public static void main(String[] args) {
        //생성
        Duration duration = Duration.ofMinutes(30);
        System.out.println("duration = " + duration);

        LocalTime lt = LocalTime.of(1, 0);
        System.out.println("기준 시간 = " + lt);

        //계산에 사용
        LocalTime plusTime = lt.plus(duration);
        System.out.println("더한 시간 = " + plusTime);

        //시간 차이
        LocalTime start = LocalTime.of(9, 0);
        LocalTime end = LocalTime.of(10, 0);
        Duration between = Duration.between(start, end);
        System.out.println("차이: " + between.getSeconds() + "초");
        System.out.println("근무 시간: " + between.toHours() + "시간" + between.toMinutesPart() + "분");

    }
}
