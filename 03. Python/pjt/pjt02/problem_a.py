import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    url = 'https://api.themoviedb.org/3/movie/popular?api_key=b0aa983e176b4c8d5f9a1c93be84107b&language=en-US&page=1'

    dict_a = requests.get(url).json()
    lst_a = dict_a.get('results')
    return len(lst_a)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
