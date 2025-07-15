"""
ge = 20

if age < 20:
    print("미성년자 입니다")
else:
    print("미성년자가 아닙니다")

print(f"나이는 {age}입니다")

# 실습. if문
password = input("비밀번호를 입력해주세요: ")
if password == "abc123":
    print("비밀번호가 맞습니다")

number = int(input("숫자를 입력하세요: "))
if number % 2 == 0:
    print("짝수입니다")

# elif문
age = int(input("나이를 입력하세요"))

if age > 0:
    if age < 20:
        print("10대 입니다")
    elif age < 30:
        print("20대 입니다")
    elif age < 40:
        print("30대 입니다")
    elif age < 50:
        print("40대 입니다")
    else:
        print("50대 이상 입니다")
else:
    print("0보다 큰 값을 넣어주세요")
"""

# 삼항 연산자
age = int(input("나이를 입력하세요"))
message = "20대 입니다" if age < 30 and age >= 20 else "20대가 아닙니다"
print(message)

# 조건문에서 in 연산자 사용
fruit = input("과일을 한글로 입력하세요")

if fruit in ["사과", "복숭아", "바나나"]:
    print(f"{fruit}은 과일에 포함되어 있습니다")
else:
    print("존재하지 않는 과일입니다")
