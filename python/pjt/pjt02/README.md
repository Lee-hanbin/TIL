# Report of project_01

### 1. problem_a

- 문제
  
  인기 영화 목록을 응답 받아 개수로 출력

- Code
  
  ```python
  def popular_count():
      pass 
      # 여기에 코드를 작성합니다.  
      url = 'https://api.themoviedb.org/3/movie/popular?api_key=b0aa983e176b4c8d5f9a1c93be84107b&language=en-US&page=1'
  
      dict_a = requests.get(url).json()
      lst_a = dict_a.get('results')
      return len(lst_a)
  ```
  ```
  1. json을 받아오고 싶은 URL을 url변수에 할당한다.
  2. dict_a 변수에 URL의 json를 할당한다.
  3. lst_a 변수에 dict_a의 key가 `results`인 인기 영화 목록 list를 할당한다.
  4. 인기 영화의 개수를 반환한다.
  ```

- 접근방법
  
  - example의 문제를 보며 requests로 url의 json를 dictionary로 가져올 수 있었다.

- 과정 중 학습한 내용
  
  - API 키를 받아서 url을 읽어서 json으로 dictionary를 가져오는 방법을 알 수 있었습니다.

- 어려웠던 부분
  
  - example 문제와 비슷한 유형이었기에 큰 어려움은 없었습니다.

### 2. problem_b

- 문제

  인기 영화 목록 중 평점이 8점 이상인 영화 목록을 출력합니다.

- Code
  
  ```python
  def vote_average_movies():
      pass 
      # 여기에 코드를 작성합니다.  
      url = 'https://api.themoviedb.org/3/movie/popular?api_key=b0aa983e176b4c8d5f9a1c93be84107b&language=en-US&page=1'
  
      lst_hot = []
      dict_a = requests.get(url).json()
      lst_a = dict_a.get('results')
      for i in lst_a:
        if i.get('vote_average') >= 8:
            lst_hot.append(i)
  
      return lst_hot
  ```
  ```
  1. json을 받아오고 싶은 URL을 url변수에 할당한다.
  2. dict_a 변수에 URL의 json를 할당한다.
  3. lst_a 변수에 dict_a의 key가 `results`인 인기 영화 목록 list를 할당한다.
  4. for문을 통해 dictionary인 lst_a의 요소들을 i에 할당합니다. 
  5. key가 'vote_average'인 영화평점을 비교해서 8점 이상인 목록들을 lst_hot에 추가합니다
  ```
- 접근방법

  - url을 타고 들어가 json의 형태를 보고 list와 dictionary를 구분하여 접근하였습니다.

- 과정 중 학습한 내용

  - api 키를 받아서 json파일을 직접적으로 보고 원하는 출력물만 도출 할 수 있었습니다.

- 어려웠던 부분

  - json파일이 dictionary와 list로 엉켜있어서 구분하는데 어려움이 있었습니다.

### 3. problem_c

- 문제
  인기 영화 목록을 평점이 높은 순으로 5개의 영화 데이터 목록 출력합니다.

- Code
  
  ```python
  def ranking():
      pass 
      # 여기에 코드를 작성합니다.  
  
      url = 'https://api.themoviedb.org/3/movie/popular?api_key=b0aa983e176b4c8d5f9a1c93be84107b&language=en-US&page=1'
      dict_a = requests.get(url).json()
      lst_a = dict_a.get('results')
  
      lst_a.sort(key = lambda x : x.get('vote_average'), reverse = True)
      lst_sol = []
      for i in range(5):
        lst_sol.append(lst_a[i])
  
      return lst_sol
  ```
  ```
  1. json을 받아오고 싶은 URL을 url변수에 할당한다.
  2. dict_a 변수에 URL의 json를 할당한다.
  3. lst_a 변수에 dict_a의 key가 `results`인 인기 영화 목록 list를 할당한다.
  4. sort함수의 key parameter를 이용하여 lambda를 통해 dictionary의 'vote_average'를 기준으로 정렬합니다.
  5. sort함수의 reverse parameter를 이용하여 내림차순으로 정렬합니다.
  6. 정렬 되어 있는 list의 상위 5개의 dictionary를 append로 추가하여 출력합니다.
  ```
- 접근방법

  - 정렬의 기준이 리스트 안의 딕셔너리의 값이기 때문에 딕셔너리의 id와 평점을 가져와서 딕셔너리를 만들고 리스트로 평점을 가져와 정렬을 해서 가져오려고 했습니다. 또한, 5번째와 6번째의 값이 같거나 4번째와 5번쨰의 값이 같을 때 새로운 값이 들어올 때 어떤식으로 작동할지를 고려하려고 했으나, 코드가 길어지고 너무 복잡해서 포기했습니다..
  - sort함수의 parameter를 이용하여 dictionary의 키를 갖고 정렬을 했습니다.

- 과정 중 학습한 내용

  - sort의 reverse parameter만 알고 있었는데, key parameter를 알 수 있었습니다.

- 어려웠던 부분

  - 동일한 점수를 디테일하게 처리하고 싶었으나, 구현하는데 실패했습니다.
  - set도 써 보고 dictionary도 써 봤지만, list로 평점을 받아서 정렬한 후 해당 id를 통해 값을 도출하는 것이 코드가 길어지다보니 오류가 많이 발생하여 힘들었습니다.

### 4. problem_d

- 문제
  제공된 영화 제목('기생충','그래비티','검색할 수 없는 영화')을 검색하여 추천 영화 목록을 출력합니다.
- Code
  
  ```python
  def recommendation(title):
      pass 
      # 여기에 코드를 작성합니다.  
      query = title
      url_1 = f'https://api.themoviedb.org/3/search/movie?api_key=b0aa983e176b4c8d5f9a1c93be84107b&language=en-US&page=1&include_adult=false&query={query}'
      dict_a = requests.get(url_1).json()
      lst_sol = []
      if len(dict_a.get('results')) == 0:
          return None
      else:
          lst_a = dict_a.get('results')    
          movie_id = lst_a[0].get('id')
          url_2 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=b0aa983e176b4c8d5f9a1c93be84107b&language=ko-KR&page=1'
          dict_b = requests.get(url_2).json()
          lst_b = dict_b.get('results')            
          for i in lst_b:
              lst_sol.append(i.get('title'))
          return lst_sol
  ```
  ```
  1. query에 title값을 할당 받아 영화 Search Movies에서 영화 목록에 맞는 영화 목록을 리스트를 받습니다.
  2. 해당 영화 목록 리스트에 첫번째 영화의 id를 movie_id 변수에 할당받습니다.
  3. 해당 id를 통해 Get Recommendations에서 추천 영화 목록을 list로 입력받습니다.
  4. for문을 통해 list의 요소들을 i로 할당받아 영화 제목들만 리스트 lst_sol에 추가합니다.
  5. if문을 통해 dict_a의 키가 results인 리스트의 크기가 0이면 None을 반환합니다. 
  ```
- 접근방법

  - Search Movies와 Get Recommendations에 직접 들어가서 require에 해당하는 요소들을 살펴보고 url을 읽어올때 참고해서 할당해줬습니다.
  - if문을 통해 title과 동일한 영화 정보가 없는 경우를 나눠줬습니다.

- 과정 중 학습한 내용

  - url을 읽어올때 parameter를 조정하여 원하는 값을 출력할 수 있음을 배울 수 잇었습니다.

- 어려웠던 부분

  - url의 parameter를 조정해본적이 없어서 많이 헤맸습니다.
  - 영화 정보가 없는 경우를 조건문으로 해결할 때 조건을 어떻게 줘야 할지 몰라 힘들었습니다.

### 5. problem_e

- 문제
  제공된 영화 제목('기생충', '검색할 수 없는 영화')을 검색하여 해당 영화의 출연진(cast) 그리고 스태프(crew) 중 연출진 목록만을 출력합니다.

- Code
  
  ```python
  def credits(title):
      pass 
      # 여기에 코드를 작성합니다.  
      query = title
      url_1 = f'https://api.themoviedb.org/3/search/movie?api_key=b0aa983e176b4c8d5f9a1c93be84107b&language=en-US&page=1&include_adult=false&query={query}'
      dict_a = requests.get(url_1).json()
      if len(dict_a.get('results')) == 0:
          return None
      else:
          lst_a = dict_a.get('results')    
          movie_id = lst_a[0].get('id')
          url_2 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=b0aa983e176b4c8d5f9a1c93be84107b&language=en-US'
          dict_b = requests.get(url_2).json()
          lst_b = dict_b.get('cast')    
          lst_c = dict_b.get('crew')    
  
          dict_sol = {}
          lst_b_sol = []
          lst_c_sol = []
          for i in lst_b:
              if i.get('cast_id') < 10:
                  lst_b_sol.append(i.get('original_name'))
          for j in lst_c:
              if j.get('department') == 'Directing':
                  lst_c_sol.append(j.get('original_name'))
          dict_sol['cast'] = lst_b_sol
          dict_sol['crew'] = lst_c_sol
          return dict_sol
  ```
  ```
  1. problem_d와 같이 영화 목록 리스트를 입력받습니다.
  2. if문을 통해 json의 키가 results인 리스트의 크기가 0이면 None을 반환합니다. 
  3. results의 크기가 0이 아니면 첫번째 영화의 id를 할당받습니다.
  4. id에 해당하는 영화에 대한 출연진과 스태프 목록을 Get Credits에서 각각 list로 할당 받습니다. 
  5. for문을 통해 출연진의 id가 10미만인 이름과 스태프의 부서가 Directing인 이름을 리스트로 할당 받습니다.
  6. 해당 list를 value로 갖는 딕셔너리를 반환합니다.
  ```
- 접근방법

  - problem_d의 방법을 이용하여 json을 불러와서 파일을 확인하고 cast와 crew의 형태를 확인해서 접근하였습니다.

- 어려웠던 부분

  - problem_d와 비슷해서 어려움 없이 해결할 수 있었습니다.

---

- 느낀점
  
  - 아직 url, json과 친하지 않아서 받아들이기에 힘었지만, 익숙해 지고 나니 쉽게 받아들여졌습니다.
  - 처음 구상한 방법으로 코드를 구현하려고 하다보니 자신만의 틀에 갇혀 시간을 많이 소비하게 되었습니다. 앞으로는 조금 더 먼 곳에서 바러보면서 코딩을 해야겠다고 느꼈습니다.
  
