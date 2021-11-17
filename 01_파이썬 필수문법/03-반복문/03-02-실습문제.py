# 위 문제에서 전체 문제 개수, 맞힌 문제 개수, 틀린 문제 개수 노출 시킬 것.

# 한국어 리스트
word_list = ['사랑해', '귀엽다', '고마워', '행복해']

# 점수
score = 0

print("Let's Learning Korean.")

for word in word_list :
  print(word)
  data = input()
  if data == word :
    score += 1
  
print('전체 문제 개수 : ', len(word_list))
print('맞힌 개수 : ', score)
print('틀린 개수 : ', len(word_list) - score)

# 출력
# Let's Learning Korean.
# 전체 문제 개수 :  4
# 맞힌 개수 :  2
# 틀린 개수 :  2