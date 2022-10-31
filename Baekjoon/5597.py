# [백준 5597] 과제 안 낸 사람
import sys

students = [i for i in range(1, 31)]

for _ in range(28):
    applied = int(sys.stdin.readline().rstrip())
    students.remove(applied)

students.sort()
print(students[0])
print(students[1])
