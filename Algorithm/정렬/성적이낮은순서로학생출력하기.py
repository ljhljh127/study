
"""
정렬 180p문제
문제
N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다.   
각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.

입력조건
첫 번째 줄에 학생의 수 N이 입력된다. (1 ≤ N ≤ 100,000)
두 번째 줄부터 N + 1 번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다.
문자열 A의 길이와 학생의 성적은 100 이하의 자연수이다.

출력조건
모든 학생의 이름을 성적이 낮은 순서대로 출력한다. 성적이 동일한 학생들의 순서는 자유롭게 출력해도 괜찮다.
"""

def grade_downtoup():
    n = int(input())
    students = []
    for _ in range(n):
        student = input().split()
        students.append(student)
    students.sort(key = grade)

    for i in students:
        print(name(i))

def grade(data):
    return data[1]

def name(data):
    return data[0]

grade_downtoup()

