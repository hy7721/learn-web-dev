# 기존 비밀번호 = "1234"
# 입력한 비밀번호 = "1234"
# 만약 비밀번호를 정확히 입력했으면 > 로그인 성공

origin_pass = "1234"
input_pass = input("패스워드를 입력하세요 >>>")

# 조건A : 만약 input_pass와 origin_pass가 같다면
if input_pass == origin_pass:
  # 조건 A가 참이라면
  print("로그인 성공!")
  print("반갑습니다.")

# 조건 B
elif input_pass == "":
  # 조건 A가 거짓, 조건 B가 참
  print("아무것도 입력하지 않았습니다.")

else :
  # 조건 A가 거짓, 조건 B도 거짓
  print("로그인 실패!")
  print("비밀번호를 확인하세요.")