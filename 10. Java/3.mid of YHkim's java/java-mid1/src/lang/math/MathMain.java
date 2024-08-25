package lang.math;

public class MathMain {
    /*
        1. 기본 연산 메서드
            abs(x) : 절대값
            max(a, b) : 최대값
            min(a, b) : 최소값
        2. 지수 및 로그 연산 메서드
            exp(x) : e^x 계산
            log(x) : 자연 로그
            log10(x) : 로그 10
            pow(a, b) : a의 b 제곱
        3. 반올림 및 정밀도 메서드
            ceil(x) : 올림
            floor(x) : 내림
            rint(x) : 가장 가까운 정수로 반올림
            round(x) : 반올림
        4. 삼각 함수 메서드
            sin(x) : 사인
            cos(x) : 코사인
            tan(x) : 탄젠트
        5. 기타 유용한 메서드
            sqrt(x) : 제곱근
            cbrt(x) : 세제곱근
            random() : 0.0과 1.0 사이의 무작위 값 생성
    */
    public static void main(String[] args) {
        //기본 연산 메서드
        System.out.println("max(10, 20): " + Math.max(10, 20));
        System.out.println("min(10, 20): " + Math.min(10, 20));
        System.out.println("abs(-10): " + Math.abs(-10));


        //반올림 및 정밀도 메서드
        // cf)  아주 정밀한 숫자와 반올림 계산이 필요하다면 BigDecimal 을 검색해보자.
        System.out.println("ceil(2.1): " + Math.ceil(2.1)); //올림
        System.out.println("floor(2.7): " + Math.floor(2.7)); //내림
        System.out.println("round(2.5): " + Math.round(2.5)); //반올림


        //기타 유용한 메서드
        System.out.println("sqrt(4): " + Math.sqrt(4));
        System.out.println("random(): " + Math.random());
    }
}
