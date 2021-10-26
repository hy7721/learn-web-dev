# 프로그램 사용자로부터 국어, 수학, 영어 성적이 입력된다. 세 과목의 평균 점수가 80점 이상이면 합격이다. 그런데 점수에 따라 합격 또는 불합격이 정해지는 프로그램에 오류가 발생했다. 80점 미만일 경우 불합격이 표시되도록 프로그램을 작성해보자. (단, 0점에서 100점 사이의 숫자를 입력하지 않으면 "잘못 입력하였습니다"를 출력하자)

# 내 풀이
korean = int(input("국어 점수"))
math = int(input("수학 점수"))
english = int(input("영어 점수"))

total = korean + math + english
average = total / 3

if average >= 80:
  print("불합격!")

elif 0 <= korean <= 100 or 0 <= math <= 100 or 0 <= english <= 100:
  print("잘못 입력했다!")



# 방법1 (모범 답안)
if 0 <= korean <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
  if average >= 80:
    print("불합격")
  else average < 80
    print("합격")
else:
  print("잘못 입력하였습니다.")

# 방법2 (모범 답안)
if korean < 0 or korean > 100 or math < 0 or math > 100 or english < 0 or english > 100:
  print("잘못 입력하였습니다.")
elif average >= 80
  print("불합격")
else:
  print("합격")
