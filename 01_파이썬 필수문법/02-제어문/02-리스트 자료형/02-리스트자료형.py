# 턱걸이 평균 측정 프로그램을 만들어보자. 먼저 턱걸이 횟수를 저장할 빈 리스트를 만든다. 그리고 일주일간의 턱걸이 횟수를 입력 받아 리스트에 저장한다. 리스트에 저장된 데이터의 평균을 구해 출력한다.

# 내풀이
result = []
day1 = int(input("1일차 턱걸이 횟수 >>>"))
result.append(day1)
day2 = int(input("2일차 턱걸이 횟수 >>>"))
result.append(day2)
day3 = int(input("3일차 턱걸이 횟수 >>>"))
result.append(day3)
day4 = int(input("4일차 턱걸이 횟수 >>>"))
result.append(day4)
day5 = int(input("5일차 턱걸이 횟수 >>>"))
result.append(day5)
day6 = int(input("6일차 턱걸이 횟수 >>>"))
result.append(day6)
day7 = int(input("7일차 턱걸이 횟수 >>>"))
result.append(day7)

print(result)

average = (result[0] + result[1] + result[2] + result[3] + result[4] + result[5] + result[6]) / 7
print(average)



# 모범답안
data = []
x = int(input("1일차 턱걸이 횟수"))
data.append(x)
x = int(input("2일차 턱걸이 횟수"))
data.append(x)
x = int(input("3일차 턱걸이 횟수"))
data.append(x)
x = int(input("4일차 턱걸이 횟수"))
data.append(x)
x = int(input("5일차 턱걸이 횟수"))
data.append(x)
x = int(input("6일차 턱걸이 횟수"))
data.append(x)
x = int(input("7일차 턱걸이 횟수"))
data.append(x)
# 어차피 데이터가 차곡차곡 쌓이기 때문에 다른 변수를 할당할 필요가 없다.

total = data[0] + data[1] + data[2] + data[3] + data[4] + data[5] + data[6]
average = total / 7

print(int(average))
# 정수로 출력



# 반복문으로 수정(100일 동안 등록한다고 할 때)
for i in range(1,101):
  x = int(input(i, "일차 턱걸이 횟수 >>>"))
  data.append(x)