package lang.object.equals;

import java.util.Objects;

public class UserV2 {
    private String id;

    public UserV2(String id) {
        this.id = id;
    }
/*
    @Override
    public boolean equals(Object obj){
        // equals() 는 Object 타입을 매개변수로 사용한다.
        // 따라서 객체의 특정 값을 사용하려면 다운캐스팅이 필요하다.
        UserV2 user = (UserV2) obj;
        return id.equals(user.id);
    }*/

    //제너레이터를 통한 equals()
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        UserV2 userV2 = (UserV2) o;
        return Objects.equals(id, userV2.id);
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(id);
    }
}
