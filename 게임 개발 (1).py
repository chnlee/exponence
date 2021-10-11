# 게임 개발
n, m = map(int,input().split())
d = [[0] * m for _ in range(n)]
x, y, direction = map(int,input().split())
d[x][y] = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]
array = []
for i in range(n):
  array.append(list(map(int,input().split())))

def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3 

count = 1
turn_time = 0
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  else:
    turn_time += 1
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dx[direction]
    if array[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn_time = 0
print(count)
# # 답지    풀이
# # N,M을 공백으로 구분하여 입력받기
# n, m = map(int,input().split())

# # 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
# d = [[0]*m for _ in range(n)]
# # 현재 캐릭터의 X 좌표, y 좌표 방향을 입력받기
# x, y ,direction = map(int, input().split())
# d[x][y] = 1 # 현재 좌표를 방문 처리한다

# # 전체 맵 정보를 입력받기
# array = []
# for i in range(n):
#   array.append(list(map(int,input().split())))

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# # 왼쪽으로 회전
# def turn_left():
#   global direction
#   direction -= 1
#   if direction == -1:
#     direction = 3