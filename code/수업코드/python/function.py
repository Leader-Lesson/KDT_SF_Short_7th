# 함수
# 함수 정의
def say_hello(born, name):
    age = 2025 - born
    print(f"{name}님의 나이는  {age}세 입니다.")

say_hello(2000, "민지")

# 구구단 코드

# 4단, 7단 출력 

# 함수 매개변수로 리스트 전달
def times(nums):
    # print(nums)
    return [i ** 2 for i in nums]

number = [2,3,6,9]
print(times(number))

# 전역변수
quantity = 2

def get_price(price):
    price *= quantity
    return price

print(f"{quantity}개의 가격은 {get_price(5000)}입니다")

# 지역변수
def oneUp():
    x = 0
    x += 1
    return x

print(oneUp())
# print(x)

# 유효범위
quantity = 10
def price_sum(price):
    # quantity = 7
    return price * quantity

print(price_sum(1000))

# global
x = 0
def twoUp():
    global x
    x += 2
    return x

print(twoUp())

# 기본 매개변수 (기본값 설정 가능)
def pr_str(txt, count = 1):
    for i in range(count):
        print(txt)

pr_str("Hello",2)
pr_str("Hi")