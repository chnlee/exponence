# 문자열 재정렬

# n = input()
# A = list()
# B = list()
# count = 0
# for i in range(len(n)):
#   if ord(n[i]) > 57:
#     A.append(n[i])
#   else :
#     B.append(n[i])

# A.sort()
# for j in B:
#   count += int(j)

# for k in A:
#   print(k,end="")
# print(count) 
#만약 count 가 0일 경우 추가 되지 않음을 설명하지 못해서 틀렸다고 할 수 있따.


data = input()
result = []
value = 0

for x in data:
  if x.isalpha(): #isalpha  알파벳인 경우를 판단하는 함수
    result.append(x)
  else:
    value += int(x)
  
result.sort()

if value != 0:
  result.append(str(value))
  
#리스트를 문자열로 변환하여 출력
print(''.join(result)) 
