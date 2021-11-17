# 구구단 출력 프로그램을 만들어보자.
# 프로그램 사용자로부터 출력할 단을 입력 받고, 해당 구구단을 출력하는 프로그램이다.

x = int(input('몇 단을 츨력할까요? >>>'))

for i in range(1, 10):
  print(x,'*', i, '=', x*i)

# 출력
# 몇 단을 츨력할까요? >>>5
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45