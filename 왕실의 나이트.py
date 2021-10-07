#왕실의 나이트
# 1. 8 * 8 matrix 를 생성한다
# 2. 이동할 수 있는 벡터를 설정한다. 
# 3. 나이트가 이동할 수 있는 경우의 수는 총 2가지, 벡터의 방향을 8가지로 설정해보자

# 총 이동할 수 있는 경우의 수:
# L, R, U, D, LU, LD, RU, RD
# chr -> 숫자를 문자로 바꾸는 용도, ord -> 문자를 숫자로 바꾸는 용도
loc = input()
count = 0
x = ord(loc[0])
y = int(loc[1])
dx = [-1,1,-1,1,-2,-2,2,2]
dy = [-2,-2,2,2,1,-1,-1,1]
move_types = ['LLU','LLD','RRU','RRD','ULU','URU','DLD','DRD']

for i in range(len(move_types)):
  nx = x + dx[i]
  ny = y + dy[i]
  if nx < 97 or nx > 104 or ny <1 or ny>8 :
    continue
  count += 1
print(count)

# 답안 예시
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0
for step in steps:
  next_row = row +step[0]
  next_column = column + step[1]

  if next_row >= 1 and next_row <=8 and next_column >=1 and next_column <=8:
    result += 1
print(result)
