# ch 7 이진탐색

'''
@ 순차 탐색
 - 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데읻터를 하나씩 차례대로 확인하는 방법
 - 보통 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용
 - 데이터가 아무리 많아도 시간만 충분하다면 항상 원하는 원소를 찾을 수 있다.

@ 이진 탐색
 - 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘
 - 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징이 있음
 - 시작점, 끝점, 중간점을 잉용
 - 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾음
 - 재귀구현
def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)
 - 반복구현
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

@ 트리 자료구조
 - 데이터베이스는 내부적으로 대용량 데이터 처리에 적합한 트리 자료구조를 이용하여 항상 데이터가 정령되어 있음
 - 따라서 데이터베이스는 이진 탐색과 유사한 방법을 이용해 탐색을 항상 빠르게 수행하도록 설계 되어 있음
 - 정의
    1. 트리는 부모 노드와 자식 노드의 관계로 표현
    2. 트리의 최상단 노드를 루트 노드라고 함
    3. 트리의 최하단 노드를 단말(리프) 노드라고 함
    4. 트리에서 일부를 떼어내도 트리 구조이며 서브 트리라고 함
    5. 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다르기에 적합

@이진 탐색 트리
 - 트리 자료구조 중에서 가장 간단한 형태
 - 이진 탐색이 동작할 수 있도록 고안됨
 - 효율적인 탐색이 가능
 - 정의
    1. 부모 노드보다 왼쪽 자식 노드가 작다.
    2. 부모 노드보다 오른쪽 자식 노드가 크다.
 - tip
    1. 데이터의 개수가 1,000만 개를 넘어가거나 탐색 범위의 크기가 1,000억 이상이라면 이진 탐색 알고리즘을 의심!!
    2. input 받기
      - input_data = sys.sydin.readline().rstrip()
        print(input_data)
'''

'''
@ 실전 1) 부품 찾기

# 문제

'''

'''
@ 실전 2) 떡볶이 떡 만들기

#문제
'''

