# QuerySet API Advanced

## 사전 준비

1. 가상 환경 생성 및 활성화

2. 패키지 목록 설치

3. migrate 진행
   
   `$ python [manage.py](<http://manage.py/>) migrate`

4. sqlite3에서 csv 데이터 import 하기
   
   ```html
   $ sqlite3 db.sqlite3
   
   => sqlite > .mode csv
   => sqlite > .import users.csv users_user
   => .exit
   ```

5. 테이블 확인

6. shell_plus 실행
   
   `$ python [manage.py](<http://manage.py/>) shell_plus`

## CRUD 기본

- 모든 user 레코드 조회
  
  `User.objects.all()`

- user 레코드 생성
  
  ```powershell
  In [3]: User.objects.create(
     ...: first_name='길동',
     ...: last_name='홍',
     ...: age=100,
     ...: country='제주도',
     ...: phone='010-1234-4567',
     ...: balance=10000,
     ...: )
  ```

- 101번 userr 레코드 조회
  
  `User.objects.get(pk=101)`

- 101번 user 레코드의 last_name 을 김 으로 수정
  
  ```powershell
  user = User.objects.get(pk=101)
  user.last_name = '김'
  user.save()
  ```

- 101번 user 레코드 삭제
  
  ```powershell
  user = User.objects.get(pk=101)
  user.delete()
  ```

- 전체 인원 수 조회
  
  - `User.objects.count()`
  - `len(User.objects.all()`

## Sorting data

- 나이가 어린 순으로 이름과 나이 조회하기
  
  `User.objects.order_by('age')`
  
  ⇒ 단지 객체로 표시되기에 정렬이 잘 됐는지 알 수 없음
  
  `User.objects.order_by('age').values('first_name', 'age')`
  
  ⇒ `.values` 를 통해 이름과 나이만 출력
  
  ```powershell
  .order_by()
  - 기본적으로 오름차순 정렬
  - '-필드명'하면 내림차순 정렬
  - '?'하면 랜덤으로 정렬
  
  .value()
  - 모델 인스턴스가 아닌 딕셔너리 요소들을 가진 QuerySet을 반환
  - 필드를 지정하면 각 딕셔너리에는 지정한 필드에 대한 key와 value만을 출력
  - 입력하지 않을 경우 각 딕셔너리에는 레코드의 모든 필드에 대한 key와 value를 출력
  ```

- 이름과 나이를 나이가 많은 순서대로 조회하기
  
  `User.objects.order_by('-age').values('first_name', 'age')`

- 이름, 나이, 계좌 잔고를 나이가 어린순
  
  - 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회
  
  `User.objects.order_by('age', '-balance').values('first_name', 'age','balance)`

## Filtering data

- 중복없이 모든 지역 조회하기
  
  `User.objects.distinct().values('country')`

- 이름과 지역이 중복 없이 모든 이름과 지역 조회하기
  
  `User.objects.distinct().values('country').order_by('country')`

- 이름과 지역이 중복 없이 모든 이름과 지역 조회하기
  
  `User.objects.distinct().values('first_name', 'country')`

- 이름과 지역 중복 없이 지역 순으로 오름차순 정렬하여 모든 이름과 지역 조회하기
  
  `User.objects.distinct().values('first_name','country').order_by('country')`

- 나이가 30인 사람들의 이름 조회하기
  
  `User.objects.filter(age=30).values('first_name')`

- 나이가 30살 이상인 사람들의 이름과 나이 조회
  
  `User.objects.filter(age__gte=30).values('first_name','country')`
  
  ```powershell
  #Field lookups
  
  <https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups>
  ```

- 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌 잔고 조회하기
  
  `User.objects.filter(age__gte=30,balance__gt=500000).values('first_name','age', 'balance')`

- 이름에 ‘호’가 포함되는 사람들의 이름과 성 조회하기
  
  `User.objects.filter(first_name__contains='호').values('first_name', 'last_name')`

- 핸드폰 번호가 011로 시작하는 사람들의 이름과 핸드폰 번호 조회
  
  `User.objects.filter(phone__startswith='011').values('first_name','phone')`

- 이름이 ‘준’으로 끝나는 사람들의 이름 조회하기
  
  `User.objects.filter(first_name__endswith='준').values('first_name')`

- 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회하기
  
  `User.objects.filter(country__in=['강원도','경기도']).values('first_name', 'country')`

- 경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회하기
  
  `User.objects.exclude(country__in=['강원도','경기도']) .values('first_name', 'country')`

- 나이가 가장 어린 10명의 이름과 나이 조회하기
  
  `User.objects.order_by('age').values('first_name', 'age')[::10]`

- 나이가 30이거나 성이 김씨인 사람들 조회
  
  ```powershell
  from django.db.models import Q
  User.objects.filter(Q(age=30) | Q(last_name='김')).values('last_name')
  ```
  
  - `'Q' object` 사용 ⇒ Q 객체들끼리 연산

```
Tip
```

- print(User.objects.all().query)
  - sql 문으로 어떻게 넘어가는지 확인할 수 있음

## Aggregation(Grouping data)

### `aggregate()`

- 전체 queryset에 대한 값을 계산
- 특정 필드 전체의 합, 평균, 개수 등을 계산할 때 사용
- 딕셔너리를 반환

### 실습

- 나이가 30살 이상인 사람들의 평균 나이 조회하기
  
  ```powershell
  from django.db.models import Avg
  
  User.objects.filter(age__gte=30).aggregate(Avg('age'))
  ```

- 가장 높은 계좌 잔액 조회하기
  
  `User.objects.aggregate(Max('balance'))`

- 모든 계좌 잔액 총액 조회하기
  
  `User.objects.aggregate(Sum('balance'))`

### `annotate()`

- 쿼리의 각 항목에 대한 요약 값을 계산
- SQL의 GROUP BY에 해당
- ‘주석을 달다’ 라는 사전적 의미를 가지고 있음

### 실습

- 각 지역별로 몇 명씩 살고 있는지 조회하기
  
  ```powershell
  from django.db.models import Count
  
  User.objects.values('country').annotate((Count('country')))
  ```

- 각 지역별로 몇 명씩 살고 있는지 + 지역별 계좌 잔액 평균 조회하기
  
  `User.objects.values('country').annotate(Count('country'), avg_balance=Avg('balance'))`

- 각 성씨가 몇 명씩 있는지 조회하기
  
  `User.objects.values('last_name').annotate(Count('last_name'))`

### N:1 예시

- 만약 Comment-Article 관계가 N:1 인 경우 다음과 같은 참조도 가능
  
  ```powershell
  #예시
  
  Article.objects.annotate(
      numver_of_comment=Count('comment'),
      pub_date=Count('comment', filter=Q(comment__create__lte='200-01-01'))
  )
  ```
  
  - 전체 게시글을 조회하면서 annotate로 각 게시글의 댓글 개수와 2000-01-01보다 나중에 작선된 댓글의 개수를 함께 조회하는 것