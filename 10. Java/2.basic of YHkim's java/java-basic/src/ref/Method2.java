package ref;

public class Method2 {

    public static void main(String[] args) {

        Student student1 = createStudent("학생1", 15, 90);
        System.out.println("student1=" + student1);
        Student student2 = createStudent( "학생2", 16, 80);
        System.out.println("student2=" + student2);

        printStudent(student1);
        printStudent(student2);
//        initStudent(student1, "학생1", 15, 90)
    }

    static Student createStudent(String name, int age, int grade){
        Student student = new Student();
        System.out.println("student=" + student);
        student.name = name;
        student.age = age;
        student.grade = grade;
        return student;
    }

    static  void initStudent(Student student, String name, int age, int grade){
        student.name = name;
        student.age = age;
        student.grade = grade;
    }

    static void printStudent(Student student){
        System.out.println("이름: " + student.name + " 나이: " + student.age + " 성적: " + student.grade);
    }
}
