# 1이 될 때까지

# N과 K가 주어질 때, N이 1이 될 때까지 1번 혹운 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 짜라
# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 단, 두번째 연산은 N이 K로 나눠떨어질때만 선택할 수 있다.
#  1. N에서 1을 뺀다.
#  2. N을 K로 나눈다.

n, k = map(int, input().split())

result = 0

while True:
    # N == K 로 나눠떨어지는 수가 될때까지 1 씩 빼기
    emp = (n//k) * k
    result += (n-emp)
    n = emp

    # N이 K값보다 작으면 반복문 탈출
    if n < k:
        break

    # K로 나누기
    result += 1
    n //= k

# K보다 작은 N 의 값에서 1을 제외한 숫자 더하기
result += (n-1)
print(result)