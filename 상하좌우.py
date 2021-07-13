#내 풀이
N = int(input())
_list = [(i+1,j+1) for i in range(N) for j in range(N)]
A = list(input().split())
#서동북남
x,y = 1,1
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for i in A:
  if(i == "L"):
    if((x+dx[0],y+dy[0]) in _list):
      x +=dx[0]
      y +=dy[0]
    else: continue
  if(i == "R"):
    if((x+dx[1],y+dy[1]) in _list):
      x +=dx[1]
      y +=dy[1]
    else: continue
  if(i == "U"):
    if((x+dx[2],y+dy[2]) in _list):
      x +=dx[2]
      y +=dy[2]
    else: continue
  if(i == "D"):
    if((x+dx[3],y+dy[3]) in _list):
      x +=dx[3]
      y +=dy[3]
    else: continue
print(x,y)

#교재 풀이
n = int(input())
x,y = 1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
      print(nx,ny)
  if nx< 1 or ny <1 or nx >n or ny >n :
    continue
  x,y = nx,ny
print(nx,ny)  
