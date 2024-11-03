package lang.wrapper;

public class WrapperVsPrimitive {

    /*
        사실상, 10억정도 해야 저정도 차이나는 것이기에 유지보수에 용이한 것을 골라서 사용하면됨
    */
    public static void main(String[] args) {
        int iterations = 1_000_000_000; // 반복 횟수 설정,  10억 (자바에서 _로 넣어서 구분자 인정해줌)
        long startTime, endTime;

        //기본형 long 사용
        long sumPrimitive = 0;
        startTime = System.currentTimeMillis();
        for (int i = 0; i < iterations; i++){
            sumPrimitive += i;
        }
        endTime = System.currentTimeMillis();
        System.out.println("sumPrimitive = " + sumPrimitive);
        System.out.println("기본 자료형 long 실행 시간: " + (endTime - startTime) + "ms"); //547ms


        //래퍼 클래스 Long 사용
        Long sumWrapper = 0L;   //래퍼 해줄때 L 붙여줘야함
        startTime = System.currentTimeMillis();
        for(int i = 0; i <iterations; i++) {
            sumWrapper += i; //오토 박싱 발생
        }
        endTime = System.currentTimeMillis();
        System.out.println("sumWrapper = " + sumWrapper);
        System.out.println("래퍼 클래스 Long 실행 시간: " + (endTime - startTime) + "ms"); //4884ms
    }
}
