# 거스름돈 문제
# 거슬러줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수 구하기

n = 3740
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)