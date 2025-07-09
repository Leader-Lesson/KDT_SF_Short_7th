"""
# 리스트 기초
number = [1, 2, 3, "Hello", "Python"]
print(number[3])
print(number[0])

text = "Hello, Python"
text = list(text)
print(text)

# 리스트 슬라이싱
shop = ["반팔", "청바지", "이어폰", ["무선키보드", "기계식기보드"]]
print(shop[:2])  # 0 <= shop < 2
print(shop[3])
print(shop[-2])
shop[0] = "긴팔"
print(shop)
# shop[100] = "신발"
# print(shop)
del shop[1]
print(shop)
del shop[2:]
print(shop)
a = [1, 2, 3]
b = ["안녕하세요", "반갑습니다"]
print(a + b)
print(b * 3)

# 정렬함수
num = [3, 1, 5, 2]
num_asc = sorted(num)
print(num_asc)
num_desc = sorted(num, reverse=True)
print(num_desc)
print(num)
num.sort()  # 매서드
print(num)

korean = ["강", "이", "박", "최", "김"]
korean.sort(reverse=True)
print(korean)

alphabet = ['b', 'c', 'a', 'd']
alphabet.reverse()
print(alphabet)
print(alphabet.index('c'))
# print(alphabet.index('w'))

a = ['a', 'b', 'c', "안녕", "Hi"]
a.append("Good")
print(a)
a.pop()
print(a)
a.pop(2)
print(a)
a.remove("안녕")
print(a)
a.insert(2, "잘가")
print(a)
a.clear()
print(a)

x = ['q', 'w', 'e', 'r', 'w']
print(x.count('w'))

# 실습. 리스트 연습문제
rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
print(rainbow[2])
sorted_rainbow = sorted(rainbow)
print(sorted_rainbow)
rainbow.append("pink")
print(rainbow)
del rainbow[3:7]
print(rainbow)

# 이차원 리스트
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[2][0])
# 요소추가
matrix[1] = matrix[1] + [99]
print(matrix)
# 행 추가
matrix = matrix + [[10, 11, 12]]
print(matrix)
# 요소 수정
matrix[0][0] = 100
matrix[1][1] = 5000
print(matrix)
# 행 삭제
del matrix[2]
print(matrix)
# 행 개수
rows = len(matrix)
print(rows)
# 열 개수
cols = len(matrix[0])
print(cols)

# 이차원 매서드
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 요소 추가
matrix[0].append(10)
print(matrix)
# 행 추가
matrix.append([10, 11, 12])
print(matrix)
matrix[1].insert(1, 100)
print(matrix)
matrix.insert(2, ["안녕하세요", "반갑습니다", "어서오세요"])
print(matrix)
# 확장
matrix[0].extend([11, 12])
print(matrix)

# 튜플
t1 = (1,)
t2 = (1, 2, 3, 4, 5, 3, 3, 3, 3)
t3 = 1, 2, 3
t4 = ('a', 'b', 'c', ("안녕", "감사"))
print(t1[0])
print(t2.count(3))
print(t3.index(2))
print(t4[3][0])
print(len(t4))
print('d' in t4)


# Set
# s1 = {1, 1, 1, 1, 1, 1, 1, 2}
# print(s1)
# s2 = ['안녕', '잘가', 'Hi', '안녕']
# print(set(s2))

"""

"""
s1 = {1, 2, 3, 3, 4}
print(s1)
s1.add(5)
print(s1)
s1.update([6, 7, 8, 9, 10])
print(s1)
s1.remove(3)
print(s1)
s1.discard(9)
print(s1)
# s1.remove(11)
# print(s1)
s1.discard(11)
print(s1)
s1.clear()
print(s1)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
# 합집합
# s3 = s1 | s2
s3 = s1.union(s2)
print(s3)

# 교집합
# s3 = s1 & s2
s3 = s1.intersection(s2)
print(s3)

# 차집합
# s3 = s1 - s2
# s3 = s2 - s1
s3 = s2.difference(s1)
print(s3)

# 딕셔너리
# 생성
dict1 = {}
dict1 = dict()
print(dict1)
dict1 = {
    "name": "홍길동",
    "age": 20,
    "city": "서울",
    "hobby": ["런닝", "등산", "헬스"]
}
print(dict1)
dict2 = dict(name="홍길동", age=20)
print(dict2)
print(dict1['name'])
print(dict1['hobby'][2])
# 값 수정
dict1["age"] = 21
print(dict1)
# 값 추가
dict1["birthday"] = 20001011
print(dict1)
dict1['hobby'] = ['런닝', '등산', '헬스', "캠핑"]
print(dict1)
del dict1["birthday"]
print(dict1)

# 딕셔너리 메서드
fruits = {
    'apple': '사과',
    'banana': '바나나'
}
print(fruits.get('apple'))
print(fruits.get('peach'))
print(fruits.get('peach', '복숭아'))
# 여러 요소 추가
fruits.update({
    'grapes': '포도',
    'melon': '멜론'
})
print(fruits)
print(fruits.keys())
print(fruits.values())
print(fruits.items())
fruits.clear()
print(fruits)


# 실습. 성적관리
students = {}
students['Alice'] = 85
students['Bob'] = 90
students['Charlie'] = 95
students['David'] = 80
students['Alice'] = 88
del students['Bob']
print(students)
"""
# 내장함수
# sum()
# numbers = [1, 2, 3, 4, 5]
# print(sum(numbers))

# scores = {"국어": 90, "영어": 80, "수학": 85}
# print(sum(scores.values()))


# zip()
names = ['Alice', 'Bob', 'Charlie', 'David']
scores = [85, 90, 88, 95]
zipped = list(zip(names, scores))
print(zipped)