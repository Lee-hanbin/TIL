package time;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;

public class LocalDateTimeMain {

    public static void main(String[] args) {
        LocalDateTime nowDt = LocalDateTime.now();
        LocalDateTime ofDt = LocalDateTime.of(2016, 8, 16, 8, 10, 1);
        System.out.println("현재 날짜시간 = " + nowDt);
        System.out.println("지정 날짜시간 = " + ofDt);

        //날짜와 시간 분리
        LocalDate localDate = ofDt.toLocalDate();
        LocalTime localTime = ofDt.toLocalTime();
        System.out.println("localDate = " + localDate);
        System.out.println("localTime = " + localTime);

        //날짜와 시간 합체
        LocalDateTime localDateTime = LocalDateTime.of(localDate, localTime);
        System.out.println("localDateTime = " + localDateTime);

        //계산(불변)
        LocalDateTime ofDtPlus = ofDt.plusDays(1000);
        System.out.println("지정 날짜시간+1000d = " + ofDtPlus);
        LocalDateTime ofDtPlusYear = ofDt.plusYears(1);
        System.out.println("지정 날짜시간+1년 = " + ofDtPlusYear);

        //비교
        System.out.println("현재 날짜시간이 지정 날짜시간보다 이전인가? " + nowDt.isBefore(ofDt));
        System.out.println("현재 날짜시간이 지정 날짜시간보다 이후인가? " + nowDt.isAfter(ofDt));
        System.out.println("현재 날짜시간이 지정 날짜시간이 같은가? " + nowDt.isEqual(ofDt));

        /*isEqual() vs equals()
            isEqual() 는 단순히 비교 대상이 시간적으로 같으면 true 를 반환한다.
            객체가 다르고, 타임존이 달라도 시간적으로 같으면 true 를 반환한다.
            쉽게 이야기해서 시간을 계산해서 시간으로만 둘을 비교한다.

            예) 서울의 9시와 UTC의 0시는 시간적으로 같다. 이 둘을 비교하면 true 를 반환한다.
            equals() 객체의 타입, 타임존 등등 내부 데이터의 모든 구성요소가 같아야 true 를 반환한다.

            예) 서울의 9시와 UTC의 0시는 시간적으로 같다. 이 둘을 비교하면 타임존의 데이터가 다르기 때문에 false 를 반환한다
        */
    }
}
