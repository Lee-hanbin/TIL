import json


def dec_movies(movies):
    lst_12 = []
    for dict_a in movies:                                                   # movies.json에 있는 list의 요소인 dictionary를 for문으로 dict 하나씩 읽어온다.
        j = str(dict_a.get('id'))                                           # movies에 있는 id를 하나씩 입력받는다.
        movies_json = open('data/movies/'+ j +'.json', encoding='utf-8')    # data/movies 하위에 id에 해당하는 파일은 연다
        movies_dict = json.load(movies_json)                                # 해당 파일의 dictionary를 movies_dict로 입력 받는다. 
        if movies_dict.get('release_date')[5:7] == '12':                    # 해당 dictionary의 출시 월이 12월인 경우의 제목을 lst_12라는 list에 추가한다.
            lst_12.append(movies_dict.get('title'))
    return lst_12                   
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
