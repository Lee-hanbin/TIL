import requests
from pprint import pprint


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

#    return lst_a
    # lst_avg_menu = []
    # dict_top5 = {}
    # cnt = 0
    # for i in lst_a:  
    #   if cnt < 5:        
    #     dict_top5[i.get('vote_average')] = i.get('id')     # 첫 5개의 id를 set에 넣기
    #     lst_avg_menu.append(i.get('vote_average'))  # 첫 5개의 평점을 list에 넣기
    #     cnt += 1 
    #     continue
      
    #   lst_avg_menu.sort(reverse = True)                         # list를 내림차순 정렬
    #   top5_last_avg = lst_avg_menu[-1]  # 상위 5개의 영화 id 중 가장 낮은 평점
    #   print(lst_avg_menu)
    #   print(top5_last_avg)
      
    #   if top5_last_avg > i.get('vote_average'): #list의 마지막 평점이 새로 들어오는 평점보다 크면 지나감
    #     print(1)
    #     continue
    #   elif top5_last_avg == i.get('vote_average'): # list의 마지막 평점과 새로 들어오는 평점이 같으면 추가
    #     print(2)
    #     lst_avg_menu.append(i.get('vote_average'))
    #     dict_top5[i.get('vote_average')] = i.get('id') 
    #   else:                                       # 새로 들어오는 값이 top5의 값 보다 큰 경우
    #     check = 0           

    #     for j in range(len(lst_avg_menu)):               # 5개의 상위 영화에서 제일 낮은 평점의 영화가 새로운 영화와 동점인 경우를 체크
    #       if j == 0:
    #         continue
    #       elif lst_avg_menu[j] == lst_avg_menu[j-1]:
    #         check += 1

    #     if check == 0:                            # 동점인 경우가 없을 때 빼고 추가
    #       dict_top5.pop(top5_last_avg)  
    #       dict_top5[i.get('vote_average')] = i.get('id')
    #       lst_avg_menu[4] = i.get('vote_average')
    #     else:                                     # 동점인 경우가 있을 때 그냥 추가
    #       lst_avg_menu.append(i.get('vote_average'))
    #       dict_top5[i.get('vote_average')] = i.get('id') 

    # lst_sol = []
    # for k in dict_top5.keys():
    #   print(1)
    #   for r in lst_a:
    #     if k == r.get('id'): 
    #       lst_sol.append(r)

    # return lst_sol
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """
