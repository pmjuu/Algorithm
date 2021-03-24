'''1 상하좌우'''
n = int(input())
data = input().split()
x, y = 1, 1

for i in data:
  dx, dy = 0, 0
  if i == 'L': dy = -1
  elif i == 'R': dy = 1
  elif i == 'U': dx = -1
  elif i == 'D': dx = 1
  nx = x + dx
  ny = y + dy

  if 0 < nx <= n and 0 < ny <= n: #이동 후 임시 좌표가 공간 안에 있으면 최종 좌표값에 저장한다.
    x, y = nx, ny

print(x, y)


'''2 시각'''
###삽질하는 풀이
import sys
n = int(sys.stdin.readline().rstrip())
count = 0

for i in range(n+1): #시
  data = []
  data.append(i//10)
  data.append(i%10)
  for j in range(60): #분
    data2 = []
    data2.append(j//10)
    data2.append(j%10)
    for k in range(60): #초
      data3 = []
      data3.append(k//10)
      data3.append(k%10)
      if 3 in data + data2 + data3:
        count += 1

print(count)

###str() 활용한 효율적인 풀이
h = int(input())
count = 0

for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(j):
        count += 1

print(count)
