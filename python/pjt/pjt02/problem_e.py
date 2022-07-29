import requests
from pprint import pprint


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
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
