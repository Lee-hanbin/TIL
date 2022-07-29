import requests
from pprint import pprint


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

    # print(movie_id)
    # dict_b = requests.get(url_2, movie_id = movie_id).json()
    # return dict_b[0]

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
