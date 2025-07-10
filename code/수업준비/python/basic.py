"""
print()함수
print("안녕하세요")
print("Hello", "Python")
print("Hello", "Python", sep="|")
print("안녕하세요", end="/")
print("저는 000입니다.")
print(1111111)


# input() 함수
# singer = input("좋아하는가수는? ")
# print("좋아하는 가수는 ", singer, "입니다")
"""
# 한 줄 주석에 사용. 코드뒤에서도 사용가능

'''
# 변수
x = 10
print("before x", x, id(x))
# y, z = 3.14, "안녕하세요"
# print("y", y)
# print("z", z)
x = "반갑습니다"
print("after x", x, id(x))
# x = 10
# print("x", x)

a = [1, 2, 3]
print("before a", a,  id(a))
a.append(4)
print("after a", a,  id(a))

# 키워드
import keyword
# print(keyword.kwlist)

# x = 48 / 2 (9 + 3)
# print(x)

# x = (100 - 2) / 7 + (9 * 3)
# print(x)

# 복합대입연산자
# num = 5
# # += 5 ===> num = num + 5
# num += 5
# print("+=", num)
# num -= 2  # num = num - 2
# print("-=", num)
# num *= 6  # num = num * 6
# print("*=", num)
# num /= 2  # num = num / 2
# print("/=", num)
# num //= 5  # num = num // 5
# print('//=', num)
# num %= 3  # num = num % 3
# print('%=', num)
# num = 4
# num **= 4  # num = num ** 4
# print('**=', num)

# 비교연산자
# num1 = 10
# num2 = 20
# num3 = "10"
# print(num1 > num2)
# print(num1 < num2)
# print(num1 == num3)
# print(num1 >= 10)
# print(num2 <= 19)
# print(num1 != num3)

# 논리연산자
# a = 2 > 1  # True
# b = 3 < 2  # False
# c = 1 == 1  # True
# d = 3 >= 4  # False
# print(a and c)  # True
# print(a and d)  # False
# print(b or c)  # True
# print(b or d)  # False
# print(not a)  # False
# print(not d)  # True


# in 연산자
a = "hello world"
print("H" in a)  # False
print("h" in a)  # True
print("a" not in a)  # True
print("w" not in a)  # False
'''


# 실습. 연산자 연습
num = 33
a = num % 2 == 0
print("True면짝수, False면 홀수: ", a)

"""
# 변수의 사이즈 알아보는 방법
from sys import getsizeof
print(getsizeof(1))
print(getsizeof("1"))


# 변수의 자료형 알아보는 방법
print(type(11111))
print(type(333.333))
print(type("안녕하세요"))
print(type(True))
print(type(None))


# 형변환
num = int(input('숫자를 입력하세요'))
a = num % 2 == 0
print("True면짝수, False면 홀수: ", a)

print(int(5.5))
a = "10"
print(type(int(a)))
print(type(a))
num = 10
print(type(str(num)))


# 문자열 연산하기
a = "파이썬"
print("안녕하세요 " + a + " 반갑습니다.")
# print("오류" + 1234)
print("hey!" * 10)
"""

# korea_song = """
# 동해물과 백두산이 마르고 닳도록
# 하느님이 보우하사 우리나라 만세
# 무궁화 삼천리 화려강산
# 대한사람 대한으로 길이 보전하세
# """
# print(korea_song)

"""
# 따옴표출력
print(' "오늘저녁 뭐먹지?" ')
print(" '오늘저녁 뭐먹지?' ")


# 이스케이프
print("Hello\nWorld")
print("Hello\tWorld")
print("Hello\\World")
print(' \'Hello\'  ')
print(" \"Hello\"  ")


# 문자열 포매팅
print("올해는 2024년 용띠의 해이다")
year = "올해는 %d년 %s의 해이다" % (2024, "용띠")
year = "올해는 %d년 %s의 해이다" % (2025, "뱀띠")
print(year)

# 포맷코드 활용
number = "저는 올해 %d살입니다" % 20
print(number)
calc = "20 나누기 3은 %.10f" % 6.66
print(calc)
text = "저는 %-10s에서 살고있습니다." % "서울"
print(text)
char = "이모티콘은 %c 이것으로 할께요" % "😄"
print(char)


country = "대한민국"
city = "서울"
people = "한국인"
text = "저는 올해 {0}살 입니다".format(20)
print(text)
text = "저는 {0} 사람이며 {1}에 살고있습니다".format(country, city)
print(text)
text = "제가 사는 {0}은 {a}에 있습니다".format(city, a="한국")
print(text)
text = "중괄호 출력하고 싶을때 {{ 중괄호 }} ".format()
print(text)
text = "{}, {}, {}, {}".format(80, 90, 100, 200)
print(text)
a = "[{0:&^10}]".format("hey")
print(a)


# f 문자열 포매팅
name = "홍길동"
age = 20
print(f"내이름은 {name}입니다. 나이는 {age + 1}입니다.")
print(f"내이름 [{name:@^20}]")


# 실습. 이스케이프 연습
print("|\\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\   ")
print("|\"^\"`    |")
print("||_/=\\\\__|")

# 실습. f 문자열 포매팅
test = "마틴"
print(f"[{test:=^30}]")
print(f"{{ 중괄호 }}출력")


# 퀴즈
a = "Hello, Python"
print(a[7] + a[8] + a[9] + a[10] + a[11] + a[12])
print(a[7:])
# 문자열 슬라이싱
date = "20240930"
year = date[:4]
month = date[4:6]
day = date[6:]
print(year + "년", month+"월", day+"일")
print(len(date))
print(a.count('l'))


# 위치 찾기
a = "Hello, Python"
print(a.find("P"))
print(a.find("s"))
# 다수일 경우
first_o = a.find('o')
print(first_o)
second_o = a.find('o', first_o + 1)
print(second_o)

print(a.index("P"))
print(a.index("s"))


# 바꾸기, 나누기
a = "Hello, Python"
print(a.replace("Python", "파이썬"))
print(a.split("l"))


# 대/소문자 바꾸기
a = "Hello, World"
print(a.upper())
print(a.lower())

a = "      Hello        "
print(f"[{a.rstrip()}]")
print(f"[{a.lstrip()}]")
print(f"[{a.strip()}]")


print("1234".isdecimal())
print("-1234".isdigit())
print("1234".isnumeric())
print("Hello".islower())
print("HELLO".isupper())
"""

# 실습. 종합실습
# a = input("이름을 입력하세요 ")
# b = input("나이를 입력하세요 ")
# print(f"안녕하세요! {a}님 ({b}세)")
# a = input("이름을 입력하세요 ")
# b = int(input("태어난 년도를 입력하세요 "))
# c = int(input("올해 년도를 입력하세요 "))
# print(f"올해는 {c}년, {a}님의 나이는 {c - b}세 입니다")