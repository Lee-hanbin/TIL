package final1;

public class MemberMain {

    public static void main(String[] args) {
        Member member = new Member("myId", "Kim");
        member.print();
        member.changeData("myId2", "seo");
        member.print();
    }
}
