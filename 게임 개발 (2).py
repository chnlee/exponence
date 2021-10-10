# # 게임 개발
# A, B = map(int,input().split())
# x, y, loc = map(int,input().split())
# count = 0
# _map = [list(map(int,input().split())) for _ in range(A)]

# dx = [0,1,0,-1]
# dy = [-1,0,1,0]
# # 왼쪽 방향부터 차례대로 갈 곳을 정한다.
# # 왼쪽 방향으로 회전 후 왼쪽으로 한 칸을 전진한다.
# # 가보지 않았다면, 왼쪽 방향으로 회전만 수행한다.
# if loc == 0:
