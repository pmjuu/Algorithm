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
