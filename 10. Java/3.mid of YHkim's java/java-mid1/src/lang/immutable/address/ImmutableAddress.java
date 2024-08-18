package lang.immutable.address;

public class ImmutableAddress {

    // final을 사용하지 않아도 set이 없기에 변하지 않지만, 명시적으로 확실함
    private final String value;

    public ImmutableAddress(String value) {
        this.value = value;
    }

    public String getValue() {
        return value;
    }

    @Override
    public String toString() {
        return "ImmutableAddress{" +
                "value='" + value + '\'' +
                '}';
    }
}
