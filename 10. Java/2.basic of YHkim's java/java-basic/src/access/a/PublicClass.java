package access.a;


//public class 만 유일한 것임! 단, public class의 이름은 .java 파일의 이름과 같아야함
//하나의 .java 파일에는 여러개의 class 존재 가능
public class PublicClass {
    public static void main(String[] args) {
        PublicClass publicClass = new PublicClass();
        DefaultClass1 class1 = new DefaultClass1();
        DefaultClass2 class2 = new DefaultClass2();
    }
}

class DefaultClass1{

}

class DefaultClass2{

}
