package construct;

public class MemberThis {
    String nameField;

    void initMember(String nameParameter){
        nameField = nameParameter;
//        this.nameField = nameParameter; //this는 단순히 구분해줄 뿐이기 때문에 굳이 사용할 필요 x
    }
}
