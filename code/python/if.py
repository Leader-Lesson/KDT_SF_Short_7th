"""
age = 20

if age < 20:
    print("미성년자 입니다")
else:
    print("미성년자가 아닙니다.")

print(f"나이는 {age}입니다")

# 실습.if
password = input("비밀번호를 입력해주세요: ")
if password == "abc123":
    print("비밀번호가 맞습니다")

number = int(input("숫자를 입력하세요: "))
if number % 2 == 0:
    print("짝수입니다.")

# 실습. if~else
password = input("비밀번호를 입력해주세요: ")
if password == "abc123":
    print("비밀번호가 맞습니다")
else:
    print("비밀번호가 틀립니다")

number = int(input("숫자를 입력하세요: "))
if number % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다")

# elif문
age = int(input("나이를 입력하세요"))

if age < 20:
    print("10대입니다")
elif age < 30:
    print("20대입니다")
elif age < 40:
    print("30대입니다")
elif age < 50:
    print("40대입니다")
else:
    print("50대이상입니다.")

# 실습. elif
score = int(input("점수를 입려하세요: "))
if score >= 90:
    print("학점: A")
elif score >= 80:
    print("학점: B")
elif score >= 70:
    print("학점: C")
elif score >= 60:
    print("학점: D")
else:
    print("학점: F")

# 실습. 중첩 조건문
age = int(input("나이를 숫자로 입력하세요: "))

if age > 0:
    method = input("결제방법을 입력해주세요(카드 또는 현금): ")
    if method == "카드":
        if age < 8:
            price = "무료"
        elif age < 14:
            price = "450원"
        elif age < 20:
            price = "720원"
        elif age < 75:
            price = "1200원"
        else:
            price = "무료"
    elif method == "현금":
        if age < 8:
            price = "무료"
        elif age < 14:
            price = "450원"
        elif age < 20:
            price = "1000원"
        elif age < 75:
            price = "1300원"
        else:
            price = "무료"
    else:
        price = None
        print("결제방법을 카드나 현금으로 입력하세요")

    if price:
        print(f"{age}세의 {method}요금은 {price}입니다.")


else:
    print("나이는 음수가 될 수 없습니다.")


# 삼항연산자
age = int(input("나이를 입력하세요"))
# message = "20대입니다." if age < 30 and age >= 20 else "20대가 아닙니다."
message = "20대입니다." if age < 30 and age >= 20 else "30대입니다" if age < 40 and age >= 30 else "20대도 30대도 아닙니다."
print(message)


# 조건문에서 in연산자 활용
fruit = input("과일을 한글로 입력하세요: ")

if fruit in ["사과", "바나나", "복숭아"]:
    print(f"{fruit}은(는) 과일에 포함되어 있습니다.")
else:
    print("존재하지 않는 과일입니다.")
"""
# 실습. in연산자 활용
fruits = {
    "apple": 95,
    "banana": 105,
    "cherry": 50
}

fruit = input("과일을 영문으로 입력하세요: ")

if fruit in fruits:
    print(f"{fruit}의 칼로리는 {fruits[fruit]}Kcal입니다")
else:
    print(f"{fruit}는 정보가 존재하지 않습니다.")