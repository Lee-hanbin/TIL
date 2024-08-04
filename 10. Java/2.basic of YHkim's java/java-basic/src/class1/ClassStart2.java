package class1;

public class ClassStart2 { //빌드 : ctrl+shift+f10

    public static void main(String[] args) { // psvm
        String[] studentNames = {"학생1", "학생3", "학생4", "학생5"};
        int[] studentAges = {15, 17, 10, 16};
        int[] studentGrade = {90, 100, 80, 50};

        for (int i = 0; i < studentNames.length; i++) {
            System.out.println("이름:" + studentNames[i] + " 나이:" + studentAges[i] + " 성적:" + studentGrade[i] ); //sout
        }
    }

}
