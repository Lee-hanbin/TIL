package construct;

public class MemberConstruct {

    String name;
    int age;
    int grade;

    //추가(오버로딩과 this)
    MemberConstruct(String name, int age){
        //this는 생성자 코드의 첫줄에만 가능하다.
        this(name, age, 50);
//        this.name  = name;
//        this.age = age;
//        this.grade = 50;
    }

    //생성자 : 생성자 이름은 class 이름과 동일하게 써야함!
    MemberConstruct(String name, int age, int grade){
        System.out.println("생성자 호출 name=" + name + ",age=" + age + ",grade=" + grade);
        this.name = name;
        this.age = age;
        this.grade = grade;

    }
}
