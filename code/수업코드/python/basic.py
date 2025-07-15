"""
# print() 함수
print("안녕하세요")
print("Hello", "Python")
print("Hello", "Python", sep="")
print("Hello", "Python", sep="/")
print("Hello", "Python", sep="#")
print("안녕하세요", end="/")
print("저는 홍길동입니다.")
print(111)

# input() 함수
singer = input("좋아하는 가수는? ")
print("좋아하는 가수는", singer, "입니다.")
"""

# 한 줄 주석, """ or ''' : 여러 줄 주석

# 변수
x = 10
print("x", x, id(x))
y, z = 3.14, "안녕하세요"
print("y", y, "z", z)
x = "반갑습니다"
print("after x", x, id(x))
x = 10
print(id(x))

# 키워드
import keyword
# print(keyword.kwlist)

# 연산자
x = 48 / 2 * (9 + 3)
print(x)

x = (100 - 2) / 7 + 9 * 3 # 41.0
print(x)

# 복합 대입 연산자
num = 5
# num = num + 5
num += 5
print("+=", num) # 10
# num = num - 2
num -= 2
print("-=", num) # 8
# num = num * 6
num *= 6
print("*=", num) # 48
# num /= 2 나누기
# num //= 3 몫
# num %= 4 나머지
# num **= 3 거듭제곱

# 실습. 연산자 연습
num = 33
a = num % 2 == 0
print("True면 짝수, False면 홀수:", a)

# 자료형
# 자료형 식별 방법
print(type(1111))
print(type(333.33))
print(type("안녕하세요"))
print(type("a"))
print(type(True))
print(type(None))

# 변수의 사이즈
from sys import getsizeof
print(getsizeof(111), getsizeof("111"))

# 형변환
# num = int(input('숫자를 입력하세요'))
# a = num % 2 == 0
# print("True면 짝수, False면 홀수:", a)

print(int(5.5)) # 5
a = "10"
b = int(a)
print(type(int(a))) # int
print(type(a)) # str

# 문자열 연산
a = "파이썬"
print("안녕하세요 " + a + " 공부중이에요")
# print("에러" + 123)
print("hey!" * 5)

korea_song = """ehddfjsklfjlksdjfklsjfkljfkl
sjfks
d"""

# 문자열 포맷팅
print("올해는 2024년 용띠의 해이다")
year = "올해는 %d년 %s의 해이다" % (2024, "용띠")
print(year)
year = "올해는 %d년 %s의 해이다" % (2025, "뱀띠")
print(year)

# 포맷코드 활용
number = "저는 올해 %d살입니다" % 20
print(number)
calc = "20 나누기 3은 %f" % 6.6
print(calc)
text = "저는 %10s에서 살고있습니다" % "서울"
print(text)
char = "한글자 출력! %c" % "C"
print(char)

country = "대한민국"
city = "서울"
people = "한국인"
text = "저는 올해 "
# 저는 올해 20살 입니다
text = "저는 올해 {0}살 입니다".format(20)
print(text)
# 저는 대한민국 사람이며 서울에 살고있습니다
text = "저는 {0} 사람이며 {1}에 살고있습니다".format(country, city)
print(text)
text = "제가 사는 {0}은 {a}에 있습니다".format(city, a = "한국")
print(text)
text = "{}, {}, {}, {}".format(80,90,100,200)
print(text)

# f 문자열 포맷팅
name = "홍길동"
age = 20
print(f"내 이름은 {name}입니다. 나이는 {age + 1}살 입니다.")
print(f"내 이름 [{name:@^20}]")

# 실습. 이스케이프 연습
print("|\_/|")
print("|q p|    /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")

# 실습. f 문자열 포맷팅
name = "luna"
print(f"[{name:=^20}]")
print(f"{{ 중괄호 }} 출력")

# 문자열 슬라이싱
date = "20250711"
year = date[0:4] # date[:4]
month = date[4:6]
day = date[6:8] # date[6:]
print(f"{year}년 {month}월 {day}일")
# 문자열 길이
print(len("Hello Python!"))

a = "Hello, Python"
# 문자열 개수
print(a.count("l")) # 2
# 위치 찾기
print(a.find("P")) # 7
print(a.find("s")) # -1
# 다수일 경우
first_o = a.find("o")
print(first_o) # 4
second_o = a.find("o",first_o + 1) # 11
print(second_o)

# 바꾸기, 나누기
print(a.replace("Python", "파이썬"))
print(a.split("l"))

# 대/소문자 바꾸기
print(a.upper())
print(a.lower())

# 공백 없애기
a = "       Hello       "
print(f"[{a.rstrip()}]")
print(f"[{a.lstrip()}]")
print(f"[{a.strip()}]")

# 문자열 판별
print("1234".isdecimal()) # True
print("-1234".isdigit())  # False
print("1234".isnumeric()) # True

print("Hello".isalpha()) # True
print("HELLO".isupper()) # True