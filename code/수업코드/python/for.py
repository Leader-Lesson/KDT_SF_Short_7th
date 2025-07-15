# for 문
for i in range(10):
    print(i, end=" ") # 0 ~ 9

print()

for i in range(3, 10):
    print(i, end=" ") # 3 4 5 6 7 8 9
print()

for i in range(1, 10, 2):
    print(i, end=" ") # 1 3 5 7 9

print()

fruits = ["사과", "바나나", "멜론"]
for fruit in fruits:
    print(fruit, end = " ")

numbers = [1,2,3,4,5,6]
total = 0
for num in numbers:
    total += num
print(f"합계는 {total}")
