"""
# 함수
def say_hello(born, name):
    age = 2024 - born
    print(f"{name}님의 나이는 {age}세 입니다.")

say_hello(2000, "민지")
say_hello(2001, "혜린")

# 곱셈함수
def gugudan(dan, end):
    print(f"{dan}단")
    for i in range(1, end + 1):
        print(f"{dan} x {i} = {dan * i}")

gugudan(4, 20)
gugudan(7, 50)

# 결과값이 있는 함수
def calc_sum(num1, num2):
    total = 0
    for i in range(num1, num2 + 1):
        total += i
    return total

result = calc_sum(10, 20)
print(result)


def fruits():
    return ["사과", "바나나", "복숭아"]

print(fruits())

def students():
    return {
        "name": "홍길동",
        "age": 20,
        "major": "컴퓨터공학"
    }
print(students())


#함수실습1
def multi_or_add(num1, num2):
    if num1 == num2:
        return num1 * num2
    else:
        return num1 + num2

result = multi_or_add(2, 2)
result2 = multi_or_add(2, 3)
print("결과(곱) :",result)
print("결과(합) :",result2)

#함수실습2
def calc_price(price):
    # total = 0
    fee = 2500
    if price < 20000:
        total = price + fee
    else:
        total = price
    return total

result = calc_price(15000)
result2 = calc_price(30000)
print(f"상품가격은 {result}원")
print(f"상품가격은 {result2}원")

"""

#함수 매개변수로 리스트 전달
def times(nums):
    return [ i ** 2 for i in nums]

number = [2, 3, 6, 9 ]
print(times(number))

"""
# 전역변수
quantity = 10

def get_price(price):
    price = price * quantity
    return price

print(f"{quantity}개의 가격은 {get_price(5000)}입니다")

# 지역변수
def oneUp():
    x = 0
    x += 1
    return x

print(oneUp())

# 유효범위
quantity = 10

def price_sum(price):
    # quantity = 7
    return price * quantity

print(price_sum(2000))


x = 0
def oneUp():
    global x
    x += 1
    return x

print(oneUp())
print(oneUp())
print(oneUp())
print(x)

# 기본 매개변수
def pr_str(txt = "안녕하세요", count = 1):
    for _ in range(count):
        print(txt)

pr_str()
pr_str("hello", 5)
pr_str("hi")


# 함수 호출키워드
def intro(name, age, city):
    print(f"이름은 {name}이고 나이는 {age}이고 사는곳은 {city}입니다.")

intro("홍길동", 23, "서울")
intro(city="서울", name="임꺽정", age=25)
intro("홍길동", city="부산", age=25)
# intro(city="부산", age=25, "홍길동") 잘못예

# 가변 매개변수
def calc_avg(*args):
    print(args)
    total = 0
    for i in args:
        total += i
    avg = total / len(args)
    return avg

print(calc_avg(1, 2, 3, 4, 5, 6, 7, 8))

def text_def(a, b, *args):
    print("text :", a)
    print("b :", b)
    print("args :", args)

text_def("hi", 1,2,3,4,5)


def intro(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

intro(name="홍길동", age=20, city="서울", gender="남자")


# 내장함수
# abs(정수) - 절대값을 구하는 내장함수
def my_abs(x):
    if x < 0:
        return -x
    else:
        return x
    
print(my_abs(-10))
print(my_abs(5))
print(abs(-10))


#거듭제곱
print(pow(3, 4))

def my_pow(x, y):
    num = 1
    for i in range(y):
        print(f"i={i}, {num*x}={num}x{x}")
        num *= x
    return num

print(my_pow(3, 4))


# map()
def square(x):
    return x ** 3

numbers = [2, 4, 6, 8]

squared = list(map(square, numbers))
print(squared)

# filter()
def even_number(x):
    result = x % 2 == 0
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(even_number, numbers)))

# 여러개 한꺼번에 반환
def get_return():
    arr = ["사과", "바나나"]
    dic = {
        "name": "홍길동",
        "age": 20
    }
    num = 30
    return arr , dic, num

arrs, dits, nums = get_return()
print(arrs)
print(dits)
print(nums)

#실습4. 함수만들기
# 방법1
def count(num):
   lists = [ i for i in range(1, 31) if i % num == 0 ]
   counts = len(lists)
   return lists, counts

num = 4
lists, counts = count(num)
print(f"{num}의 배수: {lists}")
print(f"{num}의 개수: {counts}")

#방법2 - 중첩함수
def count(num):
    # 중첩함수 - 이 함수 내에서만 사용이 가능
    def check(x):
        return x % num == 0
    
    lists = list(filter(check, range(1, 31)))
    return lists, len(lists)

num = 5
lists, counts = count(num)
print(f"{num}의 배수: {lists}")
print(f"{num}의 개수: {counts}")

# 재귀함수
def sos(i):
    print("help me!", i)
    if i == 1:
        return ""
    else:
        return sos(i-1)

sos(10)   

# 팩토리얼
def factorial(n):
    print("n의 값", n)
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(3))

#실습5. 피보나치 수열
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))



# 람다식
# 일반함수
def add(x, y):
    return x + y
print(add(3, 4))
# 람다식
add = lambda x, y: x + y
print(add(4, 5))


oneup = lambda x : x + 1
print(oneup(1))
print((lambda x : x + 1)(2))

square = lambda x: x ** 2
print(square(4))
print((lambda x: x ** 2)(5))

minus = lambda x, y: x - y
print(minus(10, 2))
print((lambda x, y: x - y)(7, 4))

def call(func):
    for _ in range(10):
        func()

def hello():
    print("안녕하세요")

hello2 = lambda: print("반갑습니다.")

call(hello2)


numbers = [2, 4, 6, 8]
squered = map(lambda x : x ** 3, numbers)
print(list(squered))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(lambda x: x % 2 == 0, numbers)))

#실습4. 함수만들기 - 람다식
def count(num):
    lists = list(filter(lambda x: x % num == 0, range(1, 31)))
    return lists, len(lists)

num = 5
lists, counts = count(num)
print(f"{num}의 배수: {lists}")
print(f"{num}의 개수: {counts}")
"""
#실습6. hint:도시필터링, 숫자추출
city = "서울"
x = [
    ["서울", 10],
    ["서울", 20],
    ["부산", 30]
]
a = filter(lambda x: x[0] == city, x)
print(list(map(lambda x : x[1], a)))

i = 3.3333333333
print(f"{i:.2f}")


#실습6. 함수 종합 프로그래밍
#초기 날씨데이터
weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0]
]
# 평균기온함수
def avg_temperatures(weather_data):
    city = input("도시 이름을 입력하세요: ")
    total = 0
    count = 0
    for data in weather_data:
        if data[1] == city:
            total += data[2]
            count += 1
    return city, total / count

    # temp = filter(lambda x: x[1] == city,  weather_data) # 도시 추출
    # temperatures = list(map(lambda x : x[2], temp)) # 기온 추출
    # if not temperatures:
    #     return city, None
    # else:
    #     return city, sum(temperatures) / len(temperatures)

#최고/최저 기온함수
def maxmin_temperatures(weather_data):
    city = input("도시 이름을 입력하세요: ")
    temperatures = [data[2] for data in weather_data if data[1] == city]
    # temp = filter(lambda x: x[1] == city,  weather_data) # 도시 추출
    # temperatures = list(map(lambda x : x[2], temp)) # 기온 추출
    if not temperatures:
        return city, None, None
    else:
        return city, max(temperatures), min(temperatures)

# 강수량과 비가온날 찾는 함수    
def total_rain_day(weather_data):
    city = input("도시 이름을 입력하세요: ")
    temp = filter(lambda x: x[1] == city,  weather_data) # 도시 추출
    rain =  list(map(lambda x : x[3], temp)) # 강수량 추출
    total_rain = sum(rain) # 총 강수량
    rain_day = len(list(filter(lambda x : x > 0 , rain))) # 비가온날
    return city, total_rain, rain_day

# 데이터 추가 함수
def add_weather(weather_data):
    date = input("날짜를 입력하세요 (YYYY-MM-DD): ")
    city = input("도시 이름을 입력하세요: ")
    temperatures = float(input("평균 기온을 입력하세요 (℃ ): "))
    rain = float(input("강수량을 입력하세요 (mm): "))
    weather_data.append([date, city, temperatures, rain])
    return city

# 전체 데이터 출력 함수
def all_data(weather_data):
    print("\n현재 저장된 날씨 데이터:")
    for data in weather_data:
        print(f"날짜: {data[0]}, 도시: {data[1]}, 평균기온: {data[2]}℃ , 강수량: {data[3]}mm")

def main_program():
    while True:
        print("\n[날씨 데이터 분석 프로그램]")
        print("1. 평균 기온 계산")
        print("2. 최고/최저 기온 찾기")
        print("3. 강수량 분석")
        print("4. 날씨 데이터 추가")
        print("5. 전체 데이터 출력")
        print("6. 종료")
        choice = input("원하는 기능의 번호를 입력하세요: ")
        if choice == "1":
            city, avg_result = avg_temperatures(weather_data) # 도시의 평균 기온 계산 함수
            if avg_result is None:
                print(f"{city}의 정보가 존재하지 않습니다.")
            else:
                print(f"{city}의 평균 기온: {avg_result:.2f}℃")
           # print(list(filter(lambda x: x[1] == city,  weather_data)))
        elif choice == "2":
            city, max_value, min_value =  maxmin_temperatures(weather_data) #도시의 최고/최저 기온찾는 함수
            if max_value is None:
                print(f"{city}의 정보가 존재하지 않습니다.")
            else:
                print(f"{city}의 최고기온: {max_value}℃ , 최저기온: {min_value}℃")
        elif choice == "3":
            city, total_rain, rain_day =  total_rain_day(weather_data) # 강수량과 비온날 찾는 함수
            print(f"{city}의 총 강수량: {total_rain:.1f}mm")
            print(f"{city}의 비가온날: {rain_day}일")
        elif choice == "4":
            city = add_weather(weather_data) # 데이터 추가 함수
            print(f"{city}의 날씨 데이터가 추가되었습니다.")
        elif choice == "5":
            all_data(weather_data) # 전체 데이터 출력 함수
        elif choice == "6":
            print("프로그램을 종료합니다.")
            break
        else:
            print("1~6까지의 번호를 입력하세요")


# 프로그램 실행 함수
main_program()