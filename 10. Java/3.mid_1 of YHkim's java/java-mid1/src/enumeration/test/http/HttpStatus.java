package enumeration.test.http;
/*
    enumeration.test.http 패키지를 사용하자.
    HttpStatus 열거형을 만들어라.
    HTTP 상태 코드 정의

    OK
    code: 200
    message: "OK"

    BAD_REQUEST
    code: 400
    message: "Bad Request"

    NOT_FOUND
    code: 404
    message: "Not Found"

    INTERNAL_SERVER_ERROR
    code: 500
    message: "Internal Server Error"

    참고: HTTP 상태 코드는 200 ~ 299사이의 숫자를 성공으로 인정한다.
    다음 HttpStatus 열거형을 완성해라. HttpStatusMain 코드와 실행 결과를 참고하자.
*/
public enum HttpStatus {
    // 코드 작성
    OK(200, "OK"),
    BAD_REQUEST(400, "Bad Request"),
    NOT_FOUND(404, "Not Found"),
    INTERNAL_SERVER_ERROR(500, "Internal Server Error");

    private final int code;
    private final String message;

    HttpStatus(int code, String message) {
        this.code = code;
        this.message = message;
    }

    public static HttpStatus findByCode(int code) {
        for (HttpStatus status : values()) {
            if (status.getCode() == code) {
                return status;
            }
        }
        return null;
    }

    public int getCode() {
        return code;
    }

    public String getMessage() {
        return message;
    }

    public boolean isSuccess() {
        return 200 <= code && code < 300;
    }
}
