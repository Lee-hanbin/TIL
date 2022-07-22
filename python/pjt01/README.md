# Report of project_01

### 1. problem_a

- 문제
  
  샘플 영화 데이터(movie.json)이 주어졌을 때, 필요한 정보만 추출해 반환하는 함수 정의

- Code
  
  ```python
  def movie_info(movie):
      new_dict = {                   # movie.json에 해당 key에 value를 이용하여 새로운 dictinary를 생성합니다.
          'id' : movie.get('id'),
          'title' : movie.get('title'),
          'poster_path' : movie.get('poster_path'),
          'vote_average' : movie.get('vote_average'),
          'overview' : movie.get('overview'),
          'genre_ids' : movie.get('genre_ids')
      }
      return new_dict 
  ```

- 접근방법
  
  - example를 통해 접근 방법을 미리 익혔습니다.

- 과정 중 학습한 내용
  
  - import json을 불러와서 파일의 dictionary를 읽어오는 방법을 알 수 있었습니다.
  - get을 이용하여 dictionary에 해당 key에 따른 value값 도출하는 방법을 배웠습니다.
  - dictionary 실습을 통해 dictionary에 대한 이해도가 향상하였습니다.

- 어려웠던 부분
  
  - 평소에 dictionary에 대한 두려움이 있었기에 초반에 겁을 먹어 진행하는데 시간이 걸렸습니다.

### 2. problem_b

- 문제
  
  problem_a를 이용하여 'genre_ids' 를 이용하여 장르 번호가 아닌 장르 이름 리스트 'genre_names'로 바꿔 반환하는 함수 완성

- code
  
  ```python
  def movie_info(movie, genres):
      new_dict = {                                         # movie.json에 해당 key에 value를 이용하여 새로운 dictinary를 생성합니다.
          'id' : movie.get('id'),
          'title' : movie.get('title'),
          'poster_path' : movie.get('poster_path'),
          'vote_average' : movie.get('vote_average'),
          'overview' : movie.get('overview'),
          'genre_ids' : movie.get('genre_ids')
      }
      lst = movie.get('genre_ids')                         # '18과 80'을 list로 가져옵니다.
      lst_2 =[]
      for j in lst:                                        # 새로운 list에 '18과 80'에 해당하는 name을 할당합니다.
          for h in genres:
              if j == h.get('id'):
                  lst_2.append(h.get('name'))
      new_dict['genre_names'] = lst_2                      # new_dict에 key가 'genre_names'이고 value가 list인 값을 추가합니다. 
      new_dict.pop('genre_ids')                            # new_dict에서 genre_ids key 삭제합니다.
      return new_dict
  ```
  
  ```
  1. 새로운 dictionary 생성
  2. lst에 genre_ids의 value 값을 list로 입력받음
  3. 2중 for문을 통해 id와 genres의 id가 일치하는 경우 고려하여 새로운 list lst_2 생성
  4. 해당 list를 'genre_names'라는 key에 해당하는 value로 dictionary에 추가
  5. 'genre_ids' 삭제 
  ```

- 접근방법
  
  - 새로운 key를 어떻게 생성하여 어떻게 등록 할 것인지 고민
  
  - 기존에 있던 key를 어떻게 삭제할 것인지에 대한 고민

- 과정 중 학습한 내용
  
  - 기존에 있었던 dictionary에 새로운 key와 value를 어떻게 넣을 수 있는지 학습
    
    - dict['new key'] ='new value'
  
  - dictionary에 존재하는 key와 value를 삭제하는 방법에 대한 학습
    
    - dict.pop('key')

- 어려웠던 부분
  
  - 새로운 key를 생성하고 기존의 key를 삭제하는 방법에 대해 학습이 되어있지 않았기에 어려움이 있었습니다. 따라서 구글링을 통해 이를 찾아보고 해결할 수 있었습니다.

### 3. problem_c

- 문제
  
  movies.json에 평점이 높은 20개의 영화 데이터가 주어질 때, 이 중 서비스 구성에 필요한 정보만 추출해 반환하는 함수를 완성

- code
  
  ```python
  lst_final = []
      for dict_a in movies:                                               # movies의 list의 요소인 dictionary들을 for문으로 하나씩 읽어옵니다.
          new_dict = {                                       # movie.json에 해당 key에 value를 이용하여 새로운 dictinary를 생성합니다.
              'id' : dict_a.get('id'),               
              'title' : dict_a.get('title'),
              'poster_path' : dict_a.get('poster_path'),
              'vote_average' : dict_a.get('vote_average'),
              'overview' : dict_a.get('overview'),
              'genre_ids' : dict_a.get('genre_ids')
          }
          lst = dict_a.get('genre_ids')                      # 해당 dictionary의 id들을 list로 생성합니다. 
          lst_2 =[]
          for j in lst:                                      # 생성된 list의 요소인 id를 for문을 통해 하나씩 읽어옵니다.
              for h in genres:                               # genres.json 파일에 있는 list의 요소(dictionary) for문을 통해 하나씩 읽어옵니다.
                  if j == h.get('id'):                       # genres의 id와 일치하면 새로운 list lst_2에 해당 장르명을 추가합니다.
                      lst_2.append(h.get('name')
          new_dict['genre_names'] = lst_2                    # new_dict에 key가 'genre_names'이고 value가 list인 값을 추가합니다.                                  
          new_dict.pop('genre_ids')                          # new_dict에서 genre_ids key 삭제
          lst_final.append(new_dict)                         # 해당 dictionary를 출력할 list에 추가합니다.
      return lst_final
  ```
  
  ```
  1. for문에 moives의 요소를 dict_a에 하나식 할당 
  2. 새로운 dictionary 생성
  3. lst에 genre_ids의 value 값을 list로 입력받음
  4. 2중 for문을 통해 id와 genres의 id가 일치하는 경우 고려하여 새로운 list lst_2 생성
  5. 해당 list를 'genre_names'라는 key에 해당하는 value로 dictionary에 추가
  6. 'genre_ids' 삭제 
  7. 최종적으로 출력할 list에 해당 dictionary new_dict를 추가
  ```

```
- 접근방법

- 읽어온 list을 어떻게 순차적으로 진행할 지에 대한 고민

- list로 구성된 movies.json을 어떻게 읽어서 풀어 나갈지에 대한 고민

- 새로만든 dictionary를 어떻게 추합하여 생성할 지에 대한 고민



- 과정 중 학습한 내용

- for문을 통해 dictionary를 하나씩 관리할 수 있음을 알게 되었습니다.

- code를 작성하기 전에 반드시 읽어 올 파일 혹은 폴더의 상태를 살펴봐야 함을 인지하게 되었습니다.



- 어려웠던 부분

- 읽어 올 파일 혹은 폴더의 상태를 미리 숙지하지 않아 많은 시간을 소요하였습니다.

- 기존에 만든 함수를 활용하고자 노력하여 from 파일 import 함수를 통해 호출할 수 있음을 알게되었으나, 초기 함수를 호환을 고려하여 만들지 못했기에 활용할 수 없었습니다.



### 4. problem_d

- 문제

영화 세부 정보 중 수입 정보를 이용하여 모든 영화 중 가장 높은 수익을 낸 영화를 출력하는 알고리즘을 작성.



- code

```python
def max_revenue(movies):
    max_num = 0   
    for dict_a in movies:                                  # movies.json에 있는 list의 요소인 dictionary를 for문으로 dict 하나씩 읽어온다.
        j = str(dict_a.get('id'))                                           # movies에 있는 id를 하나씩 입력받는다.
        movies_json = open('data/movies/'+ j +'.json', encoding='utf-8')    # data/movies 하위에 id에 해당하는 파일은 연다
        movies_dict = json.load(movies_json)               # 해당 파일의 dictionary를 movies_dict로 입력 받는다. 
        if movies_dict.get('revenue') > max_num:           # 기존의 수익의 max값과 비교하여 더 큰 수익이면 갱신한다.
            max_num = movies_dict.get('revenue')
            max_id = j                                     # 갱신된 id를 저장한다.
    movies_json = open('data/movies/'+ max_id +'.json', encoding='utf-8')   # 최종적으로 가장 큰 수익의 id에 해당하는 파일을 연다.
    movies_dict_max = json.load(movies_json)               # 해당 파일의 dictionary를 입력 받는다. 
    max_title = movies_dict_max.get('title')               # 결과적으로 최대 수익의 dictionary의 제목을 입력받는다
    return max_title
```

```
1. 가장 큰 수입을 입력할 max_num 정의
2. for 문을 통하여 list인 movies의 요소 dictionary를 dict_a에 하나씩 할당
3. data/movies 안의 파일들은 movies.json의 id들과 동일함을 인지
4. dict_a에 대한 id들을 j에 할당하여 data/movies 안의 파일들을 하나씩 할당
5. 해당 파일들의 수입들을 비교하여 큰 값을 max_num에 갱신하고 max_id 또한 갱신
6. max_id에 대한 파일을 다시 할당하여 해당 title을 출력
```

- 접근방법
  
  - 반복문을 통해 어떻게 폴더 내부의 파일들을 오픈할 지에 대한 고민
  
  - max값을 어떻게 효율적으로 도출해낼지에 대한 고민

- 과정 중 학습한 내용
  
  - python에서 직관적으로 string에 대해 더하면 문자열이 합해짐에 대한 이해력 향상
  
  - open과 load를 이용하여 원하는 파일을 열 수 있는 능력익힘

- 어려웠던 부분
  
  - for문과 string을 통해 해당 폴더의 주소를 어떻게 완성할 지
  
  - 어떻게 data/movies내의 파일들을 하나씩 열람할 수 있을지
  
  - max값을 효율적으로 입력할 수 있는 지

### 5. problem_e

- 문제
  
  영화 세부 정보 중 개봉일 정보를 이용하여 모든 영화 중 12월에 개봉한 영화들의 제목 리스트를 출력하는 알고리즘을 작성

- code
  
  ```python
  def dec_movies(movies):
      lst_12 = []
      for dict_a in movies:                                                   # movies.json에 있는 list의 요소인 dictionary를 for문으로 dict 하나씩 읽어온다.
          j = str(dict_a.get('id'))                                           # movies에 있는 id를 하나씩 입력받는다.
          movies_json = open('data/movies/'+ j +'.json', encoding='utf-8')    # data/movies 하위에 id에 해당하는 파일은 연다
          movies_dict = json.load(movies_json)                                # 해당 파일의 dictionary를 movies_dict로 입력 받는다. 
          if movies_dict.get('release_date')[5:7] == '12':                    # 해당 dictionary의 출시 월이 12월인 경우의 제목을 lst_12라는 list에 추가한다.
              lst_12.append(movies_dict.get('title'))
      return lst_12                   
  ```
  
  ```
  1. list를 생성
  2. for을 통해 list인 movies의 요소 dictionary를 dict_a에 할당
  3. j에 dict_a의 문자열 id로 입력받음
  4. j에 입력된 id에 해당하는 data/movies의 하위파일을 입력 받는다
  5. 해당 파일들에서 출시월이 12월인 값들을 추출해 생성한 list에 추가한다.
  ```

- 접근방법
  
  - 출시일에서 날짜를 출력하는 방법을 고려해야 함

- 과정 중 학습한 내용
  
  - 

- 어려웠던 부분
  
  - 월을 입력받을 때 문자열로 받아야 함을 인지하지 못해 많은 시간이 걸렸습니다.
    
    



---

- 느낀점
  
  - 생소했던 dictionary와 json에 대해 공부할 수 있었던 좋은 기회였습니다.
  
  - 사소한 것도 하나하나 따져가며 고려해야함을 배웠습니다.
    
    
