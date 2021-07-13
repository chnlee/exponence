#행렬(matrix)
for i in range(5):
  for j in range(5):
    print('(',i,',',j,')')
    print()
#방향벡터
dx = [0,-1,0,1]
dy = [1,0,-1,0]
x,y = 2,2
for i in range(4):
  nx = x + dx[i]
  ny = y + dy[i]
  print(nx,ny)
