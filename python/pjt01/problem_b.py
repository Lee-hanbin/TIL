import json
from pprint import pprint


def movie_info(movie, genres):
    new_dict = {                                                    # movie.json에 해당 key에 value를 이용하여 새로운 dictinary를 생성합니다.
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'poster_path' : movie.get('poster_path'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_ids' : movie.get('genre_ids')
    }
    lst = movie.get('genre_ids')                                    # '18과 80'을 list로 가져옵니다.
    lst_2 =[]
    for j in lst:                                                   # 새로운 list에 '18과 80'에 해당하는 name을 할당합니다.
        for h in genres:
            if j == h.get('id'):
                lst_2.append(h.get('name'))
    new_dict['genre_names'] = lst_2                                 # new_dict에 key가 'genre_names'이고 value가 list인 값을 추가합니다. 
    new_dict.pop('genre_ids')                                       # new_dict에서 genre_ids key 삭제합니다.
    return new_dict
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
