package construct.ex;

public class Book {

    String title;
    String author;
    int page;

    Book(){
        this("", "", 0);
    }


    Book(String title, String author){
        this(title, author, 0);
    }

    //이 생성자는 위의 생성자들이 오버로딩 할 수 있는 베이이스가 된다! 따라서 this()문법 불가능
    Book(String title, String author, int page){
        this.title = title;
        this.author = author;
        this.page = page;
    }


    void displayInfo(){
        System.out.println("제목: " + title + ", 저자: " + author + ", 페이지: " + page );
    }

}
