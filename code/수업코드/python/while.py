# while 문
"""
i = 0
while i < 3:
    print("반복문", i)
    i += 1
print("종료")

# 합계 구하기
num = 1
total = 0
while num <= 10:
    total += num
    num += 1
print(f"1 ~ 10까지의 합은 {total}")

# 입력값 받기
user_input = ""
while user_input != "종료":
    user_input = input("원하는 값을 입력하세요. 종료하려면 '종료'를 입력하세요: ")
    print(f"입력한 값: {user_input}")
print("프로그램이 종료되었습니다.")
"""

# break
'''
while True:
    lunch = input("오늘 점심 뭐먹지")
    if lunch == "돈까스":
        break
    print("다시 고르기")
print("점심 메뉴 완료!")
'''

# continue
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count, end=" ")

# 실습. while문
while True:
    user_input = input("양수를 입력하세요.('종료' 입력시 프로그램 종료): ")
    if user_input == "종료":
        print("프로그램을 종료합니다")
        break

    # 음수 또는 숫자가 아닌 값
    if not user_input.isdigit():
        print("양수를 입력하세요")
        continue
    
    number = int(user_input)
    if number == 0:
        continue

    total = 0
    num = 1
    while num <= number:
        total += num
        num += 1
    print(f"1부터 {number}까지의 합은 {total}입니다")