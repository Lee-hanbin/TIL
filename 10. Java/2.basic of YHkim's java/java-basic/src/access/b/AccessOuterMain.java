package access.b;

import access.a.AccessData;

public class AccessOuterMain {
    public static void main(String[] args) {
        AccessData data = new AccessData();

        //public 호출 가능
        data.publicFeild = 1;
        data.publicMethod();

        //다른 패키지 default 호출 불가능
//        data.defaultFeild = 2;
//        data.defaultMethod();

        //private 호출 불가
    //        data.privateFeild = 3;
    //        data.privateMethod();

        //public이라 innerAccess 메서드를 호출가능
        data.innerAccess();
    }
}
