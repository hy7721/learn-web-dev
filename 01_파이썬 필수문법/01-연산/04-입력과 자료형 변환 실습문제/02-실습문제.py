# 사용자로부터 태어난 연도를 입력 받으면, 현재 나이를 출력하기

# 내 풀이
year = input('태어난 연도를 입력하세요>>>')
age = 2021 - int(year) + 1

print('현재 나이는', age, '세 입니다.')



# 모범 답안
year = int(input("태어난 연도를 입력하세요 >>>"))
age = 2021 - year + 1