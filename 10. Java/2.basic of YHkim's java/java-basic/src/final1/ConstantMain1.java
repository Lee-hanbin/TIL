package final1;

public class ConstantMain1 {

    public static void main(String[] args) {
        System.out.println("프로그램 최대 참여자 수 " + Constance.MAX_USERS);
        int currentUserCount = 999;
        proccess(currentUserCount++);
        proccess(currentUserCount++);
        proccess(currentUserCount++);
    }
    private static void proccess(int currentUserCount){
        System.out.println("참여자 수:" + currentUserCount);
        if (currentUserCount > Constance.MAX_USERS){
            System.out.println("대기자로 등록합니다.");
        } else {
            System.out.println("게임에 참가합니다.");
        }
    }

}
