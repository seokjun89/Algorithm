# 큰 수의 법칙
# N  M 개 더하기, 하나의 숫자가 K 번을 초과해서 더할 수 없음

# N M K 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N 개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n-1] # 가장 큰 값
second = data[n-2] # 두번째로 큰 값

result = 0

# 풀어보자

# 가장 큰 수가 더해지는 횟수
count = int(m/(k+1)) * k
count += m%(k+1)

result = 0
result += count * first
result += (m-count) * second

print(result)