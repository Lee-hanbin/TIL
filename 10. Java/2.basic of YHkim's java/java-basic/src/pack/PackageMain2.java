package pack;

//import 사용해서 가독성 높임
//import pack.a.User;
//import pack.a.User2;
import pack.a.*;


public class PackageMain2 {

    public static void main(String[] args) {
        Data data = new Data();
        User user = new User(); //import 사용으로 패키지 명 생략 가능
        User2 user2 = new User2();
    }
}
