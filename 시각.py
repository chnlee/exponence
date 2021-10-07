#시각
#가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제
#완전 탐색(Brute Forcing) 문제 유형
#내 풀이
N = int(input())
count = 0
for i in range(N+1):
    for j in range(60):
      for k in range(60):
        if '3' in str(i):
          count += 1
        else:
          if '3' in str(j):
            count +=1
          else:
            if '3' in str(k):
              count +=1
print(count) 

# 답안 예시
h = int(input())
count = 0 
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1
