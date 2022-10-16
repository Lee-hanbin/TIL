# SQL

22/10/04

# 데이터베이스

## 개요

- 서비스 혹은 애플리케이션들을 저장하는 곳
- 파일을 이용한 데이터 관리 → 스프레드 시트를 이용한 데이터 관리 → 관계형 데이터베이스(RDB)
- RDB는 각각의 데이터를 테이블에 기입

## 학습목표

- 데이터베이스를 사용하면 데이터를 안전하고 편리하고 빠르게 보관하고 사용 가능
- 거대하고 복잡한 데이터를 다루기 위해서는 고안된 도구 ⇒ 많은 기능을 제공
  - 기능이 많다 : 데이터 관련해서 할 수 있는 일들이 많다
  - 모든 기능을 학습하는 것은 불필요함 ⇒ 기초적인 부분에 집중
- DB 학습의 기초
  - 데이터베이스에 데이터를 어떻게 입력하고, 어떻게 출력하는지
- 즉, 데이터베이스에서의 CRUD와 여러 키워드를 위주로 학습

## 정의

- 체계화된 데이터의 모임
- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 검색, 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템
  - 내용을 고도로 구조화 함으로써 검색과 갱신의 효율화
  - 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 구조화하여 기억시켜 놓은 자료의 집합체
- 이러한 DB를 조작하는 프로그램 = DBMS(Database Management System)
- 웹 개발에서 대부분의 데이터베이스는 관계형 데이터베이스 관리 시스템(RDBMS)을 사용하여 SQL로 데이터와 프로그래밍을 구성

## RDB

### 개요

- Realational Database
- 데이터를 테이블, 행, 열 등으로 나누어 구조화 하는 방식
- 자료를 여러 테이블로 나누어서 관리하고, 이 테이블간 관계를 설정해 여러 데이터를 쉽게 조작할 수 있다는 장점이 있음
- SQL을 사용하여 데이터를 조회하고 조작

### 기본 구조

1. 스키마
2. 테이블 
   1. 필드
   2. 레코드
   3. 기본 키

### 장점

- 데이터를 직관적으로 표현
- 관련한 각 데이터에 쉽게 접근할 수 있음
- 대량의 데이터도 효율적으로 관리 가능

### RDBMS

- Relational Database Management System (관계형 데이트베이스 관리 시스템)
- 관계형 데이터베이스를 만들고 업데이트하고 관리하는 데 사용하는 프로그램
- `SQLite 사용`
  - 응용 프로그램에 파일 형식으로 넣어 사용하는 비교적 가벼운 데이터베이스에 사용
  - 대규모 동시 처리 작업에는 적합하지 않음
  - 다른 RDMBS에서 지원하는 SQL 기능을 지원하지 않을 수 있음

# SQL

## 개요

- Structured Query Language
- RDBMS의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어
- RDBMS에서 데이터베이스 스키마를 생성 및 수정할 수 있으며, 테이블에서의 자료 검색 및 관리도 할 수 있음
- 데이터베이스 객체에 대한 처리를 관리하거나 접근 권한을 설정하여 허가된 사용자만 RDBMS를 관리할 수 있도록 할 수 있음
- 많은 데이터베이스 관련 프로그램들이 SQL을 표준으로 채택하고 있음

## SQL Commands 종류

- 명령어는 특성에 따라 다음 세 가지 그룹을 분류
  1. DDL(Data Definition Language)
     1. 분류 : `데이터 정의 언어`
     2. 개념 : 
        - 관계형 데이터베이스 구조(`테이블, 스키마`)를 정의(`생성, 수정 및 삭제`)하기 위한 명령어
     3. SQL 키워드
        - `CREATE`, `DROP`, `ALTER`
  2. DML(Data Manipulation Language)
     1. 분류 : `데이터 조작 언어`
     2. 개념 :데이터를 조작(`추가, 조회, 변경, 삭제`)하기 위한 명령어
     3. SQL 키워드
        - `INSERT` , `SELECT` , `UPDATE` , `DELETE`
  3. DCL(Data Control Language
     - `파일로 존재하기 때문에 지원 X`

## SQL Syntax

- 예시
  
  ```sql
  -- SQL Syntax 예시
  
  SELECT column_name FROM table_name;
  ```
  
  - `대문자 처리`와 `;` 이 중요!!!

- 모든 SQL문은 SELECT, INSERT, UPDATE 등과 같은 키워드로 시작하고, 하나의 statement는 세미콜론(;)으로 끝남

- SQL 키워드는 대소문자를 구분하지 않음
  
  - 즉, SELECT와 select는 SQL 문에서 동일한 의미
  - 하지만 대문자로 작성하는 것을 권장

- SQL에 대한 세부적인 문법 사항들은 이어지는 DDL, DML을 진행하며 익혀볼 것

# DDL

## 사전 준비

1. 데이터베이스 mydb.sqlite3 파일생성
2. DDL.sql 파일 생성
3. vscode 실행 후 DDL.sql 화면에서 마우스 우측 버튼 클릭
   1. Use Database 선택
4. 데이터베이스 목록에서 mydb.sqlite3 선택

## 개요

- Data Definition Language
- SQL 데이터 정의 언어를 사용하여 데이터베이스 개체를 만드는 방법을 학습
- DDL은 `테이블 구조를 관리`
  - CREATE, ALTER, DROP

## CREATE TABLE

### CREATE TABLE statement

- Create new table in the database

```sql
CREATE TABLE table_name (
    column_1 data_type constrraints,
    column_2 data_type constrraints,
    column_3 data_type constrraints
);
```

### 실습

1. contacts 테이블 생성
   
   ```sql
   --DDL.sql
   
   CREATE TABLE contacts (
       name TEXT NOT NULL,
       age INTEGER NOT NULL,
       email TEXT NOT NULL UNIQUE
   );
   ```

2. Query 실행하기
   
   - 실행하고자 하는 명령문에 커서를 두고 마우스 우측 버튼
     - `Run Selected Query` 선택
   - 명령문을 모두 선택 할 필요 없으며, 실행하고자 하는 명령문 안에 커서가 올라가 있으면 가능

3. 테이블 및 스키마 확인
   
   - id 컬럼은 우리가 직접 기본 키 역할의 컬럼을 정의하지 않으면 자동으로 `rowid` 라는 컬럼으로 만들어짐
   - 

## SQLite Data Types

### 종류

1. NULL
2. INTEGER
3. REAL
4. TEXT
5. BLOB
6. NULL
- NULL value
- 정보가 없거나 알 수 없음을 의미
- `값이 따옴표 없이 NULL임`
2. INTEGER
- 정수
- 크기에 따라 0, 1, 2, 3, 4, 6, 8 바이트와 같은 가변 크기를 가짐
- `값에 둘러싸는 따옴표와 소수점 또는 지수가 없을 때`
3. REAL
- 실수
- 8바이트 부동 소수점을 사용하는 10진수 값이 있는 실수
- `값에 따옴표나 소수점, 지수가 없음`
4. TEXT
- 문자 데이터
- `값이 작은 따옴표나 큰따옴표로 묶임`
5. BLOB(Binary Large Object)
- 입력된 그대로 저장된 데이터 덩어리(대용 타입 없음)
- 바이너리 등 멀티미디어 파일
- ex) 이미지 데이터

### 특징

- SQLite는 다른 모든 SQL 데이터베이스 엔진의 정적이고 엄격한 타입이 아닌 `동적 타입 시스템` 을 사용
  
  - 컬럼에 선언된 데이터 타입에 의해서가 아니라 `컬럼에 저장된 값에 따라 데이터 타입이 결정`
    
      ⇒ 데이터 타입을 선언하지 않아도 만들어 질 수 있음 (값의 형식에 따라 달라지므로)

- 테이블을 생성할 때 컬럼에 대해 특정 데이터 타입을 선언하지 않아도 됨.
  
    ex)
  
  - 동일한 컬럼에 정수 1을 넣을 경우 INTEGER로 타입이 지정
  - 문자 ‘1’을 넣을 경우 TEXT 타입으로 지정

- SQLite의 동적 타입 시스템을 사용하면 기존의 엄격하게 타입이 지정된 데이터베이스에서는 불가능한 작업을 유연하게 수행할 수 있음

- 게다가 정적 타입 시스템이 지정된 데이터베이스에서 작동하는 SQL문이 SQLite에서 동일한 방식으로 작동한다는 점

- 다만, 다른 데이터베이스와의 호환성 문제로 `데이터 타입을 지정하는 것을 권장`

- 데이터 타입을 지정하게 되면 SQLite는 입력된 데이터의 타입을 지정된 데이터 타입으로 변환

### Type Affinity

- `타입 선호도`
- 특정 칼럼에 저장된 데이터에 권장되는 타입
- 데이터 타입 작성 시 SQLite의 5가지 데이터 타입이 아닌 다른 데이터 타입을 선언한다면, 내부적으로 각 타입의 지정된 선호도에 따라 5가지 선호도로 인식됨
  1. INTEGER
  2. TEXT
  3. BLOB
  4. REAL
  5. NUMERIC

![선호도.PNG](SQL_assets/63dd3ef248168cd0bc279af88e0d46550d66a75d.png)

- 존재 이유
  - 다른 데이터베이스 엔진 간의 `호환성` 을 최대화
  - 정적이고 엄격한 타입을 사용하는데 데이터베이스의 SQL 문을 SQLite에서도 작동하도록 하기 위함

## Constratints

### 개요

- `제약조건`
- 입력하는 자료에 대해 제약을 정함
- 제약에 맞지 않다면 입력이 거부됨
- 사용자가 원하는 조건의 데이터만 유지하기 위함
  - 즉, 데이터의 무결성을 유지하기 위한 보편적인 방법으로 테이블의 특정 컬럼에 설정하는 제약

### 데이터 무결성

- 데이터 베이스 내의 데이터에 대한 정확성, 일관성을 보장하기 위해 데이터 변경 혹은 수정 시 여러 제한을 두어 데이터의 정확성을 보증하는 것
  - `무결성 : 데이터의 정확성, 일관성`
- 데이터베이스에 저장된 데이터의 무결성을 보장하고 데이터베이스의 상태를 일관되게 유지하는 것이 목적

### 종류

1. NOT NULL
   
   - 컬럼이 NULL 값을 허용하지 않도록 지정
   - 기본적으로 테이블의 모든 컬럼은 NOT NULL 제약 조건을 명시적으로 사용하는 경우를 제외하고는 NULL 값을 허용함

2. UNIQUE
   
   - 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록함

3. PRIMARY KEY
   
   - 테이블에서 행의 고유성을 식별하는 데 사용되는 컬럼
   
   - 각 테이블에는 하나의 기본 키만 있음
   
   - 암시적으로 NOT NULL 제약 조건이 포함되어 있음
     
     ```sql
     -- 예시
     CREATE TABLE table_name(
         id INTEGER PRIMARY KEY,
         ..
     );
     ```
     
       `INTEGER 타입에만 사용가능 (INT BIGINT 등 불가!)`

4. AUTOINCREMENT
   
   - 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
   
   - INTEGER PRIMARY KEY 다음에 작성하면 해당 rowid를 다시 재사용하지 못하도록 함
     
     ```sql
     -- 예시
     CREATE TABLE table_name(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         ..
     );
     ```
   
   - Django에서 테이블 생성 시 id 컬럼에 기본적으로 사용하는 제약조건

### rowid 특징

- 테이블을 생성할 때마다 `rowid라는 암시적 자동 증가 컬럼`이 자동으로 생성

- 테이블의 행을 고유하게 식별하는 64비트 부호 있는 정수 값

- 테이블에 새 행을 삽입할 때마다 정수 값을 자동으로 할당
  
  - 값은 1에서 시작
  
  - 데이터 삽입 시에 rowid 또는 INTEGER PRIMARY KEY 컬럼에 명시적으로 값이 지정되지 않은 경우, SQLite는 테이블에서 가장 큰 rowid보다 하나 큰 다음 순차 정수를 자동으로 할당
    
      `(AUTOINCREMENT와 관계없이)`

- 만약 INTEGER PRIMARY KEY 키워드를 가진 컬럼을 직접 만들면 이 컬럼은 rowid 컬럼의 별칭(alias)이 됨
  
  - 즉, 새 컬럼 이름으로 rowid에 액세스 할 수 있으며 rowid 이름으로도 여전히 액세스 가능

- 데이터가 최대 값에 도달하고 새 행을 삽입하려고 하면 SQLite는 사용되지 않는 정수를 찾아 사용

- 만약 SQLite가 사용되지 않은 정수를 찾을 수 없으면 `SQLITE_FULL 에러`가 발생
  
  - 또한 일부 행을 삭제하고 새 행을 삽입하면 SQLite는 삭제된 행에서 rowid 값을 재사용하려고 시도

## ALTER TABLE

### 개요

- `Modify the structure of an existing table`
- 기존 테이블의 구조를 수정(변경)
- SQLite의 ALTER TABLE 문을 사용하면 기존 테이블을 다음과 같이 변경 가능
  1. `Rename` a `table`
  2. `Rename` a `column`
  3. `Add` a `new column` to a `table`
  4. `Delete` a `column`

### 1. ALTER TABLE RENAME

- `Rename a table`

- 작성 및 결과 확인
  
  ```sql
  --DDL.sql
  
  ALTER TABLE contacts RENAME TO new_contacts;
  ```
  
    `contacts 라는 테이블 이름을 new_contacts로 바꿈`

### 2. ALTER TABLE RENAME COLUMN

- `Rename a cloumn`

- 작성 및 결과 확인
  
  ```sql
  --DDL.sql
  
  ALTER TABLE new_contacts RENAME COLUMN name TO last_name;
  ```
  
    `new_contacts 라는 테이블에 name이라는 column을 last_name 이라는 column으로 바꿈`

### 3. ALTER TABLE ADD COLUMN

- `Add a new column to a table`

- 작성 및 결과 확인
  
  ```sql
  --DDL.sql
  
  ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL;
  ```
  
    `new_contacts라는 테이블에 adress 라는 column을 추가`

- 만약에 테이블에 기존 데이터가 있을 경우
  
    `Cannot add NOT NULL column with default value NULL` 에러 발생
  
    ⇒ 이전에 이미 저장된 데이터들은 새롭게 추가되는 컬럼에 값이 없기 때문에 NULL 작성
  
    ⇒ 그런데 새로 추가된 컬럼에 NOT NULL 제약조건이 있기 대문에 기본 값 없이는 추가될 수 없다는 에러가 발생함

- 해결방안
  
    `ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL DEFAULT 'no address';`
  
    ⇒ adress 컬럼이 추가되면서 기존에 있던 데이터들의 address 컬럼 값은 ‘no address’가 됨

### 4. ALTER TABLE DROP COLUMN

- `Delete a column`

- 작성 및 결과 확인
  
  ```sql
  --DDL.sql
  
  ALTER TABLE new_contacts DROP COLUMN address;
  ```
  
    `new_contacts라는 테이블에 adress 라는 column을 삭제`

## DROP TABLE

### 개요

- `Remove a table from the database`

- 데이터베이스에서 테이블을 제거
  
    `DROP TABLE table_name;`

- 존재하지 않는 테이블을 제거하면 SQLite에서 오류가 발생
  
    `no such table: table_name`

- 작성 및 결과 확인
  
  ```sql
  --DDL.sql
  
  DROP TABLE new_contacts;
  ```

### 특징

- 한 번에 하나의 테이블만 삭제할 수 있음
- 여러 테이블을 제거하려면 여러 DROP TABLE 문을 실행해야 함
- DROP TABLE 문은 `실행 취소하거나 복구할 수 없음`

# DML

## 개요

- Data Manipulation Langugage
- DML을 통해 데이터를 조작하기(CRUD)
- INSERT, SELECT, UPDATE, DELETE

## 사전 준비

- 공용 Gitlab으로 공유된 user.csv 파일 준비
- 테이블에 해당 csv 파일 데이터를 import 해서 사용할 예정

## sqlite3 사용하기

1. 시작하기
   
   ```sql
   #BASH
   
   $ sqlite3
   ```

2. 데이터베이스 파일 열기
   
   ```sql
   .open mydb.sqlite3
   ```

3. CSV 파일을 SQLite 테이블로 가져오기
   
   - DML.sql 파일 생성
   
   - 테이블 생성
     
     ```sql
     CREATE TABLE users (
     first_name TEXT NOT NULL,
     last_name TEXT NOT NULL,
     age INTEGER NOT NULL,
     country TEXT NOT NULL,
     phone TEXT NOT NULL,
     balance INTEGER NOT NULL
     );
     ```
   
   - 모드(`.mode`)를 csv로 설정
     
     ```sql
     sqlite3> .mode csv
     ```
   
   - `.import` 명령어를 사용하여 csv 데이터를 테이블로 가져오기
     
     ```sql
     sqlite> .import users.csv users
     ```
   
   - import된 데이터 확인하기
     
     `SQLITE EXPLORER의 users 테이블 ▶확인`

## Simple query

### 개요

- SELECT 문을 사용하여 간단하게 단일 테이블에서 데이터를 조회하기

### SELECT statement

`SELECT column1, column2 FROM table_name;`

- Query data from a table

- 특정 테이블에서 데이터를 `조회` 하기 위해 사용

- 문법 규칙
  
  ```sql
  1. SELECT 절에서 컬럼 또는 쉼표로 구분된 컴럼 목록을 지정
  2. FROM 절(clause)에서 데이터를 가져올 테이블을 지정
  ```

- SELECT 문은 SQLite에서 가장 복잡한 문

- 다양한 절과 함께 사용할 수 있으며 하나씩 학습할 예정
  
  - `ORDER BY`
  - `DISTINCT`
  - `WHERE`
  - `LIMIT`
  - `LIKE`
  - `GROUP BY`

### SELECT statement 실습

- 이름과 나이 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT first_name, age FROM users;
  ```

- 전체 데이터 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT rowid,* FROM users;
  ```
  
    `이때, rowid는 출력이 안되므로 따로 지정을 해줘야함`

## Sorting rows

### 개요

- `ORDER BY` 절을 사용하여 쿼리의 결과를 정렬

### ORDER BY clause

`SELECT select_list FROM table_name ORDER BY column_1 ASC, column_2 DESC;`

- Sort a result set of a query
- SELECT 문에 추가하여 결과를 정렬
- ORDER BY 절은 FROM 절 뒤에 위치함
- 하나 이상의 컬럼을 기준으로 결과를 오름차순, 내림차순으로 정렬할 수 있음
- 이를 위해 ORDER BY 절 다음에 ‘ASC’ 또는 ‘DESC’ 키워드를 사용
  - ASC: 오름차순(기본 값)
  - DESC: 내림차순

### ORDER BY clause 실습

- 이름과 나이를 나이가 어린 순서대로 조회
  
  ```sql
  -- DML.sql
  
  SELECT first_name, age FROM users ORDER BY age ASC;
  SELECT first_name, age FROM users ORDER BY age;
  ```
  
    `ASC 써도 되고 안 써도 되고`

- 이름과 나이를 나이가 많은 순서대로 조회
  
  ```sql
  -- DML.sql
  
  SELECT first_name, age FROM users ORDER BY age DESC;
  ```

- 이름, 나이, 계좌 잔고를 나이가 어린순으로, 만약 나이가 같으면 계좌 잔고가 많은 순으로 정렬해서 조회
  
  ```sql
  -- DML.sql
  
  SELECT first_name, age, balance FROM users ORDER BY age ASC, balance DESC;
  ```

`Sorting NULLs`

- NULL의 정렬 방식
- 정렬과 관련하여 SQLite는 NULL을 다른 값보다 작은 것으로 간주
- 즉, ASC를 사용하는 경우 결과의 시작 부분에 NULL이 표시
- DESC를 사용하는 경우 결과의 끝에 NULL이 표시

## Filtering data

### 개요

- 데이터를 필터링하여 중복 제거, 조건 설정 등 쿼리를 제어하기
- Clause
  - SELECT DISTINCT
  - WHERE
  - LIMIT
- Operator
  - LIKE
  - IN
  - BETWEEN

### SELECT DISTINCT clause

`SELECT DISTINCT select_list FROM table_name;`

- Remove duplicate rows in the result

- 조회 결과에서 중복된 행을 제거

- DISTINCT 절은 SELECT 에서 선택적으로 사용할 수 있는 절

- 문법 규칙
  
  ```sql
  1. DISTINCT 절은 SELECT 키워드 바로 뒤에 나타나야 함
  2. DISTINCT 키워드 뒤에 컬럼 또는 컬럼 목록을 작성
  ```

### SELECT DISTINCT 실습

- 모든 지역 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT country FROM users;
  ```

- 중복 없이 모든 지역 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT DISTINCT country FROM users;
  ```

- 지역 순으로 내림차순 정렬하여 중복 없이 모든 지역 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT DISTINCT country FROM users ORDER BY country;
  ```

- 이름과 지역이 중복 없이 모든 이름과 지역 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT DISTINCT first_name, country FROM users;
  ```

- 이름과 지역 중복 없이 지역 순으로 내림차순 정렬하여 모든 이름과 지역 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT DISTINCT first_name, country FROM users ORDER BY country DESC;
  ```

`NULL with DISTINCT`

- SQLite는 NULL 값을 중복으로 간주
- NULL 값이 있는 컬럼에 DISTINCT 절을 사용하면 SQLite는 NULL 값의 한 행을 유지

## WHERE clause

`SELECT column_list FROM table_name WHERE serach_condition;`

- Specify the search condition for rows returned by the query
- 조회 시 특정 검색 조건을 지정
- WHERE 절은 SELECT 문에서 선택적으로 사용할 수 있는 절
  - SELERCT 문 외에도 UPDATE 및 DELETE 문에서 WHERE 절을 사용할 수 있음
- FROM 절 뒤에 작성

### WHERE의 검색 조건 작성 형식

```sql
1. WHERE column_1 = 10
2. WHERE column_2 LIKE 'Ko%'
3. WHERE column_3 IN (1, 2)
4. WHERE column_4 BETWEEN 10 AND 20
```

### 비교연산자

- 두 표현식이 동일한지 테스트
  
    `=` , `<>` or `!=` , `<`, `>` , `<=` , `>=`

### 논리연산자

- 일부 표현식의 truth를 테스트할 수 있음
- 1, 0 또는 NULL 값을 반환
- SQLite는 Boolean 데이터 타입을 제공하지 않으므로 1은 TRUE를 의미하고 0은 False를 의미
- `ALL`, `AND`, `ANY` , `BETWEEN` , `IN`, `LIKE`, `NOT`, `OR` 등…

### WHERE 실습

- 나이가 30살 이상인 사람들의 이름, 나이, 계좌 잔고 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT  first_name, age, balance FROM users where age >= 30;
  ```

- 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름. 나이, 계좌 잔고 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT  first_name, age, balance FROM users where age >= 30 AND balance > 500000;
  ```

### `LIKE` Operator

- Query data based on pattern matching
- 패턴 일치를 기반으로 데이터를 조회
- SELECT, DELETE, UPDATE 문의 WHERE 절에서 사용
- 기본적으로 대소문자를 구분하지 않음
  - `‘A’ LIKE 'a'` 는 TRUE
- SQLite는 패턴 구성을 위한 두 개의 와일드 카드를 제공
  1. `%` (percent)
     - 0개 이상의 문자가 올 수 있음을 의미
  2. `_`(underscore)
     - 단일(1개) 문자가 있음을 의미

### `%` wildcard 예시

- ‘영%’ 패턴은 `영` 으로 시작하는 모든 문자열과 일치
  
    ex) `영, 영미, 영미리 ...`

- ‘%도’ 패턴은 `도` 로 끝나는 모든 문자열과 일치
  
    ex) `도, 수도, 경기도 ...`

- ‘%강원%’ 패턴은 `강원` 을 포함하는 모든 문자열의 일치
  
    ex) `강원, 강원도, 나는 강원도에 살아요 ...`

### `_` wildcard 예시

- ‘영_’ 패턴은 `영` 으로 시작하고 총 2자리인 문자열과 일치
  
    ex) `영미, 영수, 영호 ...`

- ‘_도’ 패턴은 `도` 로 끝나고 총 2자리인 문자열과 일치
  
    ex) `수도, 과도 ...`

![와일드카드PNG.PNG](SQL_assets/a9cda5dc57dabc5cc290a427a0ffb3c8bdaff9f6.png)

### LIKE 실습

- 이름에 ‘호’가 포함되는 사람들의 이름과 성 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT  first_name, last_name FROM users where first_name LIKE '%호%';
  ```

- 이름이 ‘준’으로 끝나는 사람들의 이름 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT  first_name FROM users where first_name LIKE '%준';
  ```

- 서울 지역 전화번호를 가진 사람들의 이름과 전화번호 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT  first_name, phone FROM users where phone LIKE '02-%';
  ```

- 나이가 20대인 사람들의 이름과 나이 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT  first_name, age FROM users where age LIKE '2_';
  ```

- 전화번호 중간 4자리가 51로 시작하는 사람들의 이름과 전화번호 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT  first_name, phone FROM users where phone LIKE '%-51__-%';
  ```

### `IN` operator

- Determine whether a value matches any value in a list of values
- 값이 값 목록 결과에 있는 값과 일치하는 확인
- 표현식이 값 목록의 값과 일치하는지 여부에 따라 true  또는 false를 반환
- IN 연산자의 결과를 부정하려면 `NOT IN` 연산자를 사용

### IN 실습

- 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT  first_name, country FROM users where country IN ('경기도', '강원도');
  ```

- 경기도 혹은 강원도에 살지 앟는 사람들의 이름과 지역 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT  first_name, country FROM users where country NOT IN ('경기도', '강원도');
  ```

### `BETWEEN` operator

`test_expression BETWEEN low_expression AND high_expression`

- Test whether a value is in range of values
- 값이 값 범위에 있는지 테스트
- 값이  지정된 범위에 있으면 true를 반환
- SELECT, DELETE 및 UPDATE 문의 WHERE 절에서 사용할 수 있음
- BETWEEN 연산자의 결과를 부정하려면 `NOT BETWEEN` 연산자를 사용

### BETWEEN 실습

- 나이가 20살 이상, 30살 이하인 사람들의 이름과 나이 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT  first_name, age FROM users where age BETWEEN 20 AND 30;
  ```

- 나이가 20살 미만, 30살 초과인 사람들의 이름과 나이 조회
  
  ```sql
  -- DML.sql
  
  SELECT  first_name, age FROM users where age NOT BETWEEN 20 AND 30;
  ```

## `LIMIT` clause

`SELECT column_list FROM table_name LIMIT row_count;`

- Constrain the number of rows returned by a query
- 쿼리에서 반환되는 행 수를 제한
- SELECT 문에서 선택적으로 사용할 수 있는 절
- row_count는 반환되는 행 수를 지정하는 양의 정수를 의미

### LIMIT 실습

- 첫 번째부터 열 번째 데이터까지 rowid와 이름 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT  rowid, age FROM users LIMIT 10;
  ```

- 계좌 잔고가 가장 적은 10명의 이름과 계좌 잔고 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT  first_name, balance FROM users ORDER BY balance LIMIT 10 ;
  ```

- 나이가 가장 어린 5명의 이름과 나이 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT first_name, age FROM users ORDER BY age LIMIT 5;
  ```

`OFFSET` keyword

- LIMIT 절을 사용하면 첫 번째 데이터부터 지정한 수 만큼의 데이터를 받아올 수 있지만, OFFSET과 함께 사용하면 특정 지정된 위치에서부터 데이터를 조회할 수 있음

### OFFSET 실습

- 11번째부터 20번째 데이터의 rowid와 이름 조회하기
  
  ```sql
  -- DML.sql
  
  SELECT rowid, first_name FROM users LIMIT 10 OFFSET 10;
  ```

## Grouping data

### `GROUP BY` clause

`SELECT column_1, aggregate_function(column_2) FROM table_name GROUP BY column_1, column_2;`

- Make a set of summary rows from a set of rows
- 특정 그룹으로 묶인 결과를 생성
- 선택된 컬럼 값을 기준으로 데이터들의 공통 값을 묶어서 결과로 나타냄
- SELECT 문에서 선택적으로 사용 가능한 절
- SELECT 문의 FROM 절 뒤에 작성
  - WHERE 절이 포함된 경우 WHERE 절 뒤에 작성해야 함
- 각 그룹에 대해 MIN, MAX, SUM, COUNT 또는 AVG와 같은 집계 함수를 적용하여 각 그룹에 대한 추가적인 정보를 제공할 수 있음

### Aggregate

- 집계 함수
- 값 집합의 최대값, 최소값, 평균, 합계 및 개수를 계산
- 값 집합에 대한 계산을 수행하고 단일 값을 반환
  - 여러 행으로부터 하나의 결과 값을 반환하는 함수
- SELECT 문의 GROUP BY 절과 함께 종종 사용됨
- 제공하는 함수 목록
  - `AVG()`, `COUNT()` , `MAX()` , `MIN()`, `SUM()`
- `AVG()` ,`MAX()` , `MIN()`, `SUM()` 은 숫자를 기준으로 계산하기에 반드시 `INTEGER` 만 가능

### Aggregate function 예시

- users 테이블의 전체 행 수 조회
  
  ```sql
  -- DML.sql 
  
  SELECT COUNT(*) FROM users;
  ```

- 나이가 30살 이상인 사람들의 평균 나이 조회하기
  
  ```sql
  -- DML.sql 
  
  SELECT AVG(*) FROM users WHERE age >= 30;
  ```

### GROUP BY 연습

- 각 지역별로 몇 명씩 살고 있는지 조회하기
  
  - ‘각 지역별’은 지역 별로 그룹을 나눌 필요가 있음을 의미
  
  - country 컬럼으로 그룹화
    
    ```sql
    -- DML.sql 
    
    SELECT country FROM users GROUP BY country;
    ```

- 마지막으로 몇 명씩 사는지 계산 하기 위해서 그룹별로 포함되는 데이터의 수를 구함

- Aggregation Function의 COUNT를 사용
  
  ```sql
  -- DML.sql 
  
  SELECT country, COUNT(*) FROM users GROUP BY country;
  ```
  
    `COUNT` ⇒ 어떤 컬럼을 넣어도 상관 X

### GROUP BY 실습

- 각 성씨가 몇 명씩 있는지 조회하기
  
  ```sql
  -- DML.sql 
  
  SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
  ```

- 각 성씨가 몇 명씩 있는지 조회2
  
  - `AS 키워드` 를 사용해 컬럼명을 임시로 변경하여 조회 가능
    
    ```sql
    -- DML.sql 
    
    SELECT last_name, COUNT(*) AS number_of_name FROM users GROUP BY last_name;
    ```

- 인원이 가장 많은 성씨 순으로 조회하기
  
  ```sql
  -- DML.sql 
  
  SELECT last_name, COUNT(*) FROM users GROUP BY last_name ORDER BY COUNT(*) DESC;
  ```

- 각 지역별 평균 나이 조회하기
  
  ```sql
  -- DML.sql 
  
  SELECT country, AVG(age) FROM users GROUP BY country;
  ```

## Changing data

### 개요

- 데이터를 삽입, 수정, 삭제하기
  - `INSERT`, `UPDATE`, `DELETE`

### 사전 준비

```sql
-- DML.sql 

CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);
```

### `INSERT` statement

`INSERT INTOtable_name (column1, column2, ….) VALUES (value1, value2m ….);`

- Insert new rows into a table

- 새 행을 테이블에 삽입

- 문법 규칙
  
  ```sql
  1. 먼저 INSERT INTO 키워드 뒤에 데이터를 삽입할 테이블의 이름을 지정
  2. 테이블 이름 뒤에 쉼표로 구분된 컬럼 목록을 추가
      -> 컬럼 목록은 선택 사항이나, 컬럼 목록을 포함하는 것을 권장
  3. VALUES 키워드 뒤에 쉼표로 구분된 값 목록을 추가
      -> 만약 컬럼 목록을 생략하는 경우 값 목록의 모든 컬럼에 대한 값을 지정해야 함
    -> 값 목록의 값 개수는 컬럼 개수와 동일해야 함
  ```

### INSERT 실습

- 단일 행 삽입하기
  
  ```sql
  -- DML.sql
  
  INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '서울');
  -- INSERT INTO classmates VALUES ('홍길동', 23, '서울');
  ```

- 여러 행 삽입하기
  
  ```sql
  -- DML.sql
  
  INSERT INTO classmates 
  VALUES ('이한빈', 30, '서울'),
               ('김효미', 28, '건입'),
               ('정유정', 27, '인천'),
               ('김경림', 27, '구디'),
               ('이창준', 30, '강남');
  ```

### `UPDATE` statement

`UPDATE table_name SET column_1 = new_value_1, column_2 = new_value_@ WHERE search_condition;`

- Update existing rows in a table

- 테이블에 있는 기존 행의 데이터를 업데이트

- 문법 규칙
  
  ```sql
  1. UPDATE 절 이후에 업데이트할 테이블을 지정
  2. SET 절에서 테이블의 각 컬럼에 대해 새 값을 설정
  3. WHERE 절의 조건을 사용하여 업데이트할 행을 지정
      -> WHERE 절은 선택 사항이며, 생략 시 UPDATE 문은 테이블의 모든 행에 있는 데이터 업데이트
  4. 선택적으로 ORDER BY 및 LIMIT 절을 사용하여 업데이트할 행 수를 지정 할 수도 있음
  ```

### UPDATE 실습

- 2번 데이터의 이름을 ‘김철수한무두루미’, 주소를’제주도’로 수정
  
  ```sql
  -- DML.sql
  
  UPDATE classmates
  SET name = '김철수한무두루미',
          address = '제주도'
  WHERE rowid = 2;
  ```

### `DELETE` statement

`DELETE FROM table_name WHERE search_condition;`

- Delete rows from a table

- 테이블에서 행을 제거

- 테이블의 한 행, 여러 행 및 모든 행을 삭제 가능

- 문법 규칙
  
  ```sql
  1. DELETE FROM 키워드 뒤에 행을 제거하려는 테이블의 이름을 지정
  2. WHERE 절에 검색 조건을 추가하여 제가할 행을 식별
      -> WHERE 절은 선택 사항이며, 생량 시 DELETE 문은 테이블의 모든 행을 삭제
  3. 선택적으로 ORDER BY 및 LIMIT 절을 사용하여 삭제할 행 수를 지정 할 수도 있음
  ```

### DELETE 연습

- 5번 데이터 삭제하기
  
  ```sql
  -- DML.sql
  
  DELETE FROM classmates WHERE rowid = 5;
  ```

- 삭제 된 것 확인하기
  
  ```sql
  -- DML.sql
  
  SELECT rowid, * FROM classmates;
  ```

### DELETE 실습

- 이름에 ‘영’이 포함되는 데이터 삭제하기
  
  ```sql
  -- DML.sql
  
  DELETE FROM classmates WHERE name LIKE '%길%';
  ```

- 테이블의 모든 데이터 삭제하기
  
  ```sql
  -- DML.sql
  
  DELETE FROM classmates;
  ```