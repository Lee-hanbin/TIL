package access;

/*
*       private : 모든 외부 호출을 막는다.
*       default(package-private) : 같은 패키지안에서 호출은 허용 (접근 제어자 안 적었을때 기본값)
*       protected : 같은 패키지안에서 호출은 허용한다. 패키지가 달라도 상속 관계의 호출은 허용
*       public  : 모든 외부 호출을 허용한다.
*/
public class Speaker {
    //int volume;

    //private를 붙여서 클래스 내부에서만 이용 가능하게 함
    private int volume;

    Speaker(int volume){
        this.volume = volume;
    }

    void volumeUp(){
        if(volume >= 100){
            System.out.println("음량을 증가할 수 없습니다. 최대 음량입니다.");
        } else {
            volume += 10;
            System.out.println("음량을 10 증가합니다.");
        }
    }

    void volumeDown(){
        volume -= 10;
        System.out.println("volumeDown 호출");
    }

    void showVolume(){
        System.out.println("현재 음량:" + volume);
    }

}
