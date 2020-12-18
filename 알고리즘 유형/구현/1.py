# 왕실의 나이트 - 체스 나이트 말의 이동할 수 있는 경우의 수

# a1 ~ h8 까지의 좌표가 주어짐 8*8

# 현재 나이트의 위치를 입력받는다.
input_data = input()
row = int(input_data[1]) # 행
column = int(ord(input_data[0]) - ord('a')) + 1  # 문자를 아스키코드로 변환하여 1기준으로 바꿔줌

# 나이트가 이동 할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

# 8가지 방향에 대해 각 위치로 이동 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 좌표내 이동 할 수 있게 조건 추가
    if next_row >= 1 and next_column >= 1 and next_row <= 8 and next_column <= 8:
        result += 1

print(result)