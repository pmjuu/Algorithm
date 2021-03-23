'''1 거스름돈 동전 개수'''
n = 1260
count = 0

list = [500, 100, 50, 10]

for coin in list:
  count += n // coin
  n %= coin

print(count)


'''2 큰 수의 법칙'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
result = 0

data.sort(reverse=True) #내림차순 정렬
first = data[0]  #가장 큰 수
second = data[1] #두번째로 큰 수

while True:

  for i in range(k): #가장 큰 수 k번 더하기
    if m == 0: break
    result += first
    m -= 1
  if m == 0: break

  result += second #두번째로 큰 수 한 번 더하기
  m -= 1

print(result)


'''3 숫자 카드 게임'''
row, column = map(int, input().split())
result = 0

for i in range(row):
  data = list(map(int, input().split())) #행마다 입력받기
  min_value = min(data)
  result = max(min_value, result)

print(result)


'''4 1이 될 때까지'''
n, k = map(int, input().split())
result = 0

while n > 1:
  if n % k == 0: 
    n //= k #N이 K로 나누어 떨어진다면 K로 나누기
  else:
    n -= 1 #나누어 떨어지지 않는다면 1 빼기
  result += 1

print(result)

###연산의 수 줄이는 코드 - 1씩 빼는 것 미리 계산해서 한번에 빼기
n, k = map(int, input().split())
result = 0

while True:
  if n < k: break

  target = (n // k) * k
  result += (n - target)
  n = target

  n //= k
  result += 1

result += (n-1)
print(result)
