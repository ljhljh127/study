"""
다이나믹 프로그래밍 p 226 문제
문제
N가지 종류 화폐가 있을 때 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M이 되도록 할때
최소한의 화폐 개수를 구하시오

입력 조건
첫째 줄에 N,M이 주어진다. N은 1~100 M은 1~10000
이후 N개의 줄에 각 화폐의 가치가 주어진다. 화폐의 가치는 10000 보다 작거나 같은 자연수이다.

출력조건
첫쨰 줄에 M원을 만들기 위한 최소한의 화폐수를 출력한다. 불가능할때는 -1을 출력한다.
"""
# cache = [-1] * 10001

# def efficient_money(money_list, m):
#     if cache [m] != -1:
#         return cache [m]
#     min_moneycount = 10001
#     for money in money_list:
#         result = efficient_money(money_list, m- money)
#         if result != 10001:
#             min_moneycount = min(min_moneycount, result +1)
        
#     cache[m] = min_moneycount
#     return min_moneycount
    


# n, m = map(int, input().split())
# money_list = []
# for _ in range(n):
#     money_list.append(int(input()))

# efficient_money(money_list, m)

"""
recursuon errorㅠㅠ
"""

def efficient_money(money_list, m):
    cache = [10001] * (m+1)

    cache[0] = 0
    for i in range(n):
        for j in range(money_list[i], m+1):
            if cache[j -money_list[i]] != 10001:
                cache[j] = min(cache[j], cache[j - money_list[i]] +1 )
    
    if cache[m] == 10001:
        print(-1)
    else:
        print(cache[m])

n, m = map(int, input().split())
money_list = []
for _ in range(n):
    money_list.append(int(input()))

efficient_money(money_list, m)