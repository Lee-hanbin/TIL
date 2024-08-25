package enumeration.ref1;

public class DiscountService {

    public int discount(ClassGrade classGrade, int price) {
//        int discountPercent = classGrade.getDiscountPercent(); //ctrl + alt + N 하면 1줄로 합쳐짐
//        return price * discountPercent / 100;
        return price * classGrade.getDiscountPercent() / 100;
    }
}
