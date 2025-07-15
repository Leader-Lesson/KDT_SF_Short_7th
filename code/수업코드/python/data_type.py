# 리스트 기초
number = [1, 2, 3, "Hello"]
print(number[0])
print(number[3])

text = "Hello, Python"
text = list(text)
print(text)

# 리스트 슬라이싱
shop = ["반팔", "청바지", "이어폰", ["무선 키보드", "기계식 키보드"]]
print(shop[:2]) # ['반팔', '청바지']
print(shop[3]) # ['무선 키보드', '기계식 키보드']

shop[0] = "긴팔"
print(shop)
# shop[100] = "신발"

del shop[1]
print(shop)

a = [1, 2, 3]
b = [4, 5]
print(a + b)
print(a * 2)

# 정렬 함수 : sorted()
num = [3, 1, 5, 2]
num_asc = sorted(num)
print(num_asc)
num_desc = sorted(num, reverse=True)
print(num_desc)
print(num)
# 정렬 메서드 : sort()
num.sort()
print(num)

korean = ["강", "이", "노", "김"]
korean.sort(reverse=True)
print(korean)

alphabet = ["b", "d", "a", "c"]
alphabet.reverse()
print(alphabet)

a = ['a', 'b', 'c', '안녕', 'Hi']
# append() : 맨 뒤에 추가
a.append("Good")
print(a)
# pop() : 맨 뒤에 삭제
a.pop()
print(a)
a.pop(2)
print(a)
# remove(삭제할 요소)
a.remove("안녕")
print(a)
# insert(삽입할 위치, 요소)
a.insert(2, "반가워")
print(a)
# clear() : 전부 삭제
a.clear()
print(a)

# 이차원 리스트
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[2][0]) # 7
# 요소 추가
matrix[1] = matrix[1] + [99]
print(matrix)
# 행 추가
matrix = matrix + [[10,11,12]]
print(matrix)
# 요소 수정
matrix[0][0] = 100
matrix[1][1] = 500
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

# append()
matrix[0].append(10)
print(matrix)
# insert()
matrix[1].insert(1, 100)
print(matrix)
# extend()
matrix[0].extend([11,12])
print(matrix)

# 튜플
t1 = (1,)
t2 = (1,2,3,4,4,5)
t3 = 1,2,3
t4 = (1,2,(3,4))
print(t1)
print('t2.count(4)', t2.count(4))
print(t3.index(1))
print(t4[2][1])

# Set : 집합, 중복X, 순서X
s1 = {1,1,1,1,2,3,4,5,6}
print(s1) # {1, 2, 3, 4, 5, 6}

s1.add(7)
print(s1)
s1.update([6,7,8,9,10])
print(s1)
s1.remove(3)
print(s1)
s1.discard(9)
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
s3 = s2.difference(s1)
print(s3)

# 딕셔너리
# 생성
dict1 = {}
dict1 = dict()
dict1 = {
    "name": "홍길동",
    "age": 20,
    "city": "서울",
    "hobby": ["런닝", "등산", "수영"]
}
print(dict1)
dict2 = dict(name="홍길동", age=20)
print(dict2)

# 값 수정
dict1["age"] = 21
print(dict1)
# 값 추가
dict1["birthday"] = 20010101
print(dict1)
# 값 삭제
del dict1["birthday"]
print(dict1)

# 내장 함수
# sum()
numbers = [1,2,3,4,5]
print(sum(numbers))

scores = {"국어": 90, "영어": 80, "수학": 85}
print(sum(scores.values()))

# zip()
names = ['Alice', 'Bob', 'David']
scores = [85,90,95]
zipped = list(zip(names, scores))
print(zipped)