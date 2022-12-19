import json
from pprint import pprint


def movie_info(movies, genres):
    lst_final = []
    for dict_a in movies:                                               # movies의 list의 요소인 dictionary들을 for문으로 하나씩 읽어옵니다.
        new_dict = {                                                    # movie.json에 해당 key에 value를 이용하여 새로운 dictinary를 생성합니다.
            'id' : dict_a.get('id'),                                    
            'title' : dict_a.get('title'),
            'poster_path' : dict_a.get('poster_path'),
            'vote_average' : dict_a.get('vote_average'),
            'overview' : dict_a.get('overview'),
            'genre_ids' : dict_a.get('genre_ids')
        }
        lst = dict_a.get('genre_ids')                                   # 해당 dictionary의 id들을 list로 생성합니다. 
        lst_2 =[]
        for j in lst:                                                   # 생성된 list의 요소인 id를 for문을 통해 하나씩 읽어옵니다.
            for h in genres:                                            # genres.json 파일에 있는 list의 요소(dictionary) for문을 통해 하나씩 읽어옵니다.
                if j == h.get('id'):                                    # genres의 id와 일치하면 새로운 list lst_2에 해당 장르명을 추가합니다.
                    lst_2.append(h.get('name'))
        new_dict['genre_names'] = lst_2                                 # new_dict에 key가 'genre_names'이고 value가 list인 값을 추가합니다.                                  
        new_dict.pop('genre_ids')                                       # new_dict에서 genre_ids key 삭제
        lst_final.append(new_dict)                                      # 해당 dictionary를 출력할 list에 추가합니다.
    return lst_final
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
