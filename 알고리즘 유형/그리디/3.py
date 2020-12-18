# 선택한 행의 가장 작은수를 뽑아야 하여 최종적으로는 가장 높은 숫자의 카드를 뽑기 위한 알고리즘
# 각 행마다 가장 작은 수를 찾아 그 수 중에 가장 큰 수를 찾으면 된다.

# N, M 을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0

# 한 줄씩 입력받아 확인

for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    # 가장 작은 수 중에 가장 큰 수 찾기
    result = max(result, min_value)

print(result)