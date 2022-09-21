# ch 6 정렬

'''
@정렬
 - 데이터를 특정한 기준에 따라서 순서대로 나열
 - 정렬 알고리즘을 이용하여 정렬을 하면 이진탐색이 가능
 - 선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬만 언급
 - 정렬부터 공부하면 '알고리즘의 효율성'을 쉽게 이해할 수 있음

@선택정렬
 - 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고
 - 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복
ex)
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

@선택정렬의 시간 복잡도
 - 선택 정렬은 N-1번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야함.
 - 따라서 연산 횟수는 N + (N-1) + ... + 2 = N(N+1)/2
 - O(N^2)
 - 2중 for문을 썼으니 N^2이라고 간단하게 생각 가능

@삽입 정렬
 - 데이터를 하나식 확인하며, 각 데이터를 적절한 위치에 삽입
 - 선택정렬에 비해 구현 난이도가 높은 편
 - 삽입 정렬은 필요할 때만 위치를 바꾸므로 거의 정렬 상태가 되었을 때 유리
ex)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1)
        if array[j] < array[j-1]
            array[j], array[j-1] = array[j-1], array[j]
        else:
        break

@삽입정렬의 시간 복잡도
 - 삽입 정렬의 시간 복잡도는 O(N^2)
 - 2중 for문을 사용했기 때문
 - 단, 삽입 정렬은 거의 정렬되어 있는 상태에서는 매우 빠르게 동작
 - 최선의 경우 O(N) <-- 심지어 퀵 정렬보다 강력한 상황도 발생

@ 퀵 정렬
 - 가장 많이 사용되는 정렬 방법 ( 병합 정렬도 많이 이용 )
 - 두 정렬은 대부분의 프로그래밍 언어의 근간이 되는 알고리즘
 - 퀵정렬은 기준을 선정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식
 - '피벗'이 사용됨
 - 큰 수와 작은 수를 나누는 기준이 피벗

@ 퀵 정렬 방법
 1. 리스트의 첫번 째 요소를 피벗으로 둔다.
 2. 두번 째 요소를 시작으로 왼쪽 시작, 마지막 요소를 시작으로 오른쪽 시작하여 투포인트
 3. 왼쪽은 피벗보다 큰 데이터를 찾고, 오른쪽은 피벗보다 작은 데이터를 찾는다.
 4. 만약 왼쪽은 피벗보다 크고 오른쪽은 피벗보다 작으면 두 값을 서로 변경한다.
 5. 서로 마주보게 되면 피벗값보다 작은 숫자와 피벗을 서로 변경한다.
 6. 그 피벗값을 기준으로 왼쪽과 오른쪽을 각각 정렬한다.
 7. 현재 리스트가 1개가 될 때까지 반복

ex)
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

    def quick_sort(array, start, end):
        if start >= end:                # 원소가 1개인 경우 종료
            return
        pivot = start                   # 피벗은 첫 번째 원소
        left = start + 1
        right = end
        while left <= right:
            # 피벗보다 큰 데이터를 찾을 때까지 반복
            while left <= end and array[left] <= array[pivot]:
                left += 1
            # 피벗보다 큰 데이터를 찾을 때까지 반복
            while left > right:
                right -= 1
            # 엇갈렸다면 작은 데이터와 피벗을 교체
            if left > right:
                array[right], array[pivot] = array[pivot], array[rihgt]
            # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            else:
                array[left], array[right] = array[right], array[left]
        # 분할 이후 왼쪽 부분과 오른쪽 부분
        quick_sort(array, start, right-1)
        quick_sort(array, right + 1, end)

    quick_sort(array, 0, len(array) - 1)

@퀵 정렬의 시간 복잡도
 - 퀵 정렬의 시간 복잡도는 O(nlogn)

@계수 정렬
 - 특정한 조건이 부합할 때,
'''