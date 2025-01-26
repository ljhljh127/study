"""
구현 113p 문제
문제
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오

입력 예시
5

출력 예시
11475
"""
def time():
    n = int(input())
    answer = 0
    for i in range(n+1):
        for j in range(60):
            for k in range(60):
                time=f'{i}시{j}분{k}초'
                if "3" in time:
                    answer += 1
    return answer

print(time())