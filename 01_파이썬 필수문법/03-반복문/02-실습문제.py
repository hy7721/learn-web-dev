# 패스트게임즈에 인턴으로 근무하게 된 종현. 사수에게 과제로 게임 메뉴 만들기를 받았다. 과제 내용은 다음과 같았다.
# [ 과제 ]
# 숫자 1 입력 : '게임을 시작합니다' 출력
# 숫자 2 입력 : '실시간 랭킹' 출력
# 숫자 3 입력 : '게임을 종료합니다' 출력 후 프로그램 종료
# (단, 3을 입력할 때까지 프로그램은 계속 실행된다. 1~3 외 다른 숫자를 입력한 경우 '다시 입력해 주세요' 를 출력한다.)

while True :
  print('[메뉴를 입력하세요.]')
  select = int(input('1. 게임시작 2. 랭킹보기 3. 게임종료 >>>'))


  if select == 1 :
    print('게임을 시작합니다.')
  elif select == 2 :
    print('실시간 랭킹')
  elif select == 3 :
    print('게임을 종료합니다.')
    break
  else :
    print('다시 입력해주세요.')