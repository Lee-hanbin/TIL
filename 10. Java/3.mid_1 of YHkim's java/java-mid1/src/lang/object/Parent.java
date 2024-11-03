package lang.object;


//부모가 없으면 '묵시적'으로 Object 클래스를 상속받는다.
//public class Parent extends Object{
public class Parent {

    public void parentMethod(){
        System.out.println("Parent.parentMethod");
    }
}
