package lang.immutable.test;

/*
*  MyDate 클래스는 불변이 아니어서 공유 참조시 사이드 이펙트가 발생한다.
*  이를 불변 클래스로 만들어라.
*  새로운 불변 클래스는 ImmutableMyDate 로 이름 지으면 된다.
*  새로운 실행 클래스는 ImmutableMyDateMain 으로 이름 지으면 된다.
*/

public class MyDate {
    private int year;
    private int month;
    private int day;

    public MyDate(int year, int month, int day) {
        this.year = year;
        this.month = month;
        this.day = day;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public void setMonth(int month) {
        this.month = month;
    }

    public void setDay(int day) {
        this.day = day;
    }

    @Override
    public String toString() {
        return year + "-" + month + "-" + day;
    }
}
