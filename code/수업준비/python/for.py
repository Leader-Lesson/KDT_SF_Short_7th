"""
# for문
for i in range(10):
    print(i, end=" ")
print()
for i in range(3, 9):
    print(i, end=" ")
print()
for i in range(1, 100, 12):
    print(i, end=" ")

fruits = ["사과", "바나나", "포도", "체리"]
for fruit in fruits:
    print(fruit, end="|")

# 합계구하기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for num in numbers:
    total += num
print(f"합계는 {total}입니다")
"""
# 조건문 사용
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 != 0:
        print(num, end=" ")

        """
# for문
# 리스트와 for문
fruits = ["사과", "포도", "바나나", "복숭아"]
for fruit in fruits:
    print("과일은: ", fruit)

# 합계구하기
number = [10, 20, 30, 40, 50]
total = 0
for num in number:
    total += num
print(f"리스트 값의 합계는 {total}입니다")

# 조건문 사용
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in number:
    if num % 2 == 0:
        print(num, end=" ")


# 리스트내포
squares = [i ** 2 for i in range(1, 20)]
print(squares)

# if문과 함께사용
even_squares = [i ** 2 for i in range(1, 10) if i % 2 == 0]
print(even_squares)


# 딕셔너리와 for문
my_dic = {
    "name": "홍길동",
    "address": "서울시 은평구",
    "gender": "남자",
    "hobby": ["런닝", "헬스", "낚시"]
}

# 키값만 순회
# for i in my_dic:
#     print(i, end=" ")
# print()
# for i in my_dic.keys():
#     print(i, end=" ")
# print()
# for i in my_dic.values():
#     print(i, end=",")
# print()
for key, value in my_dic.items():
    print(f"{key}: {value}")

# JSON = 딕셔너리


# # 실습. 구구단 만들기
# n = int(input("몇단을 출력할까요? "))
# for i in range(1, 10):
#     print(f"{n} x {i} = {n * i}")

# 실습. 정수 합 계산
# n = int(input("어디까지 계산할까요? "))
# total = 0
# for i in range(1, n + 1):
#     if i % 2 != 0:
#         total += i

# print(f"1부터 {n}까지의 홀수의 합: {total}")

# 실습. 평균값 구하기
students = {
    "학생1": {"국어": 83, "영어": 92, "수학": 88},
    "학생2": {"국어": 90, "영어": 79, "수학": 86},
    "학생3": {"국어": 88, "영어": 86, "수학": 94}
}

for student, score in students.items():
    # print(student, score)
    total = sum(score.values())  # 세 과목의 합계
    avg = total / len(score)
    # print(avg)
    print(f"{student}의 평균은 {avg:.2f}")

# 이중for문
for i in range(5):
    for j in range(3):
        print(f"i :{i}, j :{j}")
    print()


# 2차원리스트와 for문

matrix = [
    [3, 6, 9, 12],
    [2, 4, 6, 8],
    [10, 20, 30, 40],
    [11, 12, 13, 14]
]
for row in matrix:
    for elem in row:
        if elem % 3 == 0:
            print(elem, end=" ")
"""

# 실습. 이중for문 구구단 만들기
# for i in range(2, 10):
#     print(f"[{i}단]")
#     for j in range(1, 10):
#         print(f"{i} x {j} = {i * j}")
#     print()

# # 실습. 자판기 프로그램
# vending_machine = ["게토레이", "게토레이", "레쓰비", "레쓰비", "생수", "생수", "생수", "이프로"]

# while True:
#     user_input = input("사용자를 선택하세요. (1. 소비자, 2. 주인, 3. 종료): ")

#     if user_input == "1" or user_input == "소비자":
#         drink = input("마시고 싶은 음료는? ")
#         if drink in vending_machine: # 있으면 제거
#             vending_machine.remove(drink)
#             print(f"{drink} 드릴게요")
#         else:
#             print("음료수가 없습니다.")
#         print("남은음료수: ", vending_machine)

#     elif user_input == "2" or user_input == "주인":
#         move = input("할일을 선택하세요. (1. 추가, 2. 삭제): ")
#         if move == "1" or move == "추가":
#             drink = input("추가할 음료수는?")
#             vending_machine.append(drink)
#             print("추가 완료")
#         elif move == "2" or move == "삭제":
#             drink = input("삭제할 음료수는?")
#             if drink in vending_machine:
#                 vending_machine.remove(drink)
#                 print(f"{drink} 삭제 완료")
#             else:
#                 print(f"{drink}는 현재 없습니다.")
#         else:
#             print("값을 잘못입력하셨습니다.")
#         print("남은음료수: ", vending_machine)

#     elif user_input == "3" or user_input == "종료":
#         print("자판기 프로그램을 종료합니다.")
#         break
#     else:
#         print("값을 잘못 입력하셨습니다.")



# 실습. 함수화 하기
def check_machine():
    print("남은음료수: ", vending_machine)

def is_drink(drink):
    return drink in vending_machine

def add_drink(drink):
    vending_machine.append(drink)
    print("추가 완료")

def remove_drink(drink, user):
    if user == "1" or user == "소비자":
        vending_machine.remove(drink)
        print(f"{drink} 드릴게요")
    else:
        vending_machine.remove(drink)
        print(f"{drink} 삭제 완료")

vending_machine = ["게토레이", "게토레이", "레쓰비", "레쓰비", "생수", "생수", "생수", "이프로"]

while True:
    user_input = input("사용자를 선택하세요. (1. 소비자, 2. 주인, 3. 종료): ")

    if user_input == "1" or user_input == "소비자":
        drink = input("마시고 싶은 음료는? ")
        if is_drink(drink):  # drink in vending_machine
            # vending_machine.remove(drink)
            # print(f"{drink} 드릴게요")
            remove_drink(drink, user_input)
        else:
            print("음료수가 없습니다.")
        check_machine() #print("남은음료수: ", vending_machine)

    elif user_input == "2" or user_input == "주인":
        move = input("할일을 선택하세요. (1. 추가, 2. 삭제): ")
        if move == "1" or move == "추가":
            drink = input("추가할 음료수는?")
            add_drink(drink)
            # vending_machine.append(drink)
            # print("추가 완료")
        elif move == "2" or move == "삭제":
            drink = input("삭제할 음료수는?")
            if is_drink(drink): # drink in vending_machine:
                remove_drink(drink, user_input)
                # vending_machine.remove(drink)
                # print(f"{drink} 삭제 완료")
            else:
                print(f"{drink}는 현재 없습니다.")
        else:
            print("값을 잘못입력하셨습니다.")
        check_machine() #print("남은음료수: ", vending_machine)

    elif user_input == "3" or user_input == "종료":
        print("자판기 프로그램을 종료합니다.")
        break
    else:
        print("값을 잘못 입력하셨습니다.")