import json

def max_revenue(movies):
    max_num = 0   
    for dict_a in movies:                                                   # movies.json에 있는 list의 요소인 dictionary를 for문으로 dict 하나씩 읽어온다.
        j = str(dict_a.get('id'))                                           # movies에 있는 id를 하나씩 입력받는다.
        movies_json = open('data/movies/'+ j +'.json', encoding='utf-8')    # data/movies 하위에 id에 해당하는 파일은 연다
        movies_dict = json.load(movies_json)                                # 해당 파일의 dictionary를 movies_dict로 입력 받는다. 
        if movies_dict.get('revenue') > max_num:                            # 기존의 수익의 max값과 비교하여 더 큰 수익이면 갱신한다.
            max_num = movies_dict.get('revenue')
            max_id = j                                                      # 갱신된 id를 저장한다.
    movies_json = open('data/movies/'+ max_id +'.json', encoding='utf-8')   # 최종적으로 가장 큰 수익의 id에 해당하는 파일을 연다.
    movies_dict_max = json.load(movies_json)                                # 해당 파일의 dictionary를 입력 받는다. 
    max_title = movies_dict_max.get('title')                                # 결과적으로 최대 수익의 dictionary의 제목을 입력받는다
    return max_title
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
