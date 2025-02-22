
# 다이나믹 프로그래밍을 적용 하였을 때
cache = [0]*100

def fibo(x):
    if x==1 or x==2:
        return 1
    if cache[x] != 0 :
        return cache[x]
    
    cache[x] = fibo(x - 1) + fibo(x - 2)
    return cache[x]

print(fibo(99))


# 다이나믹 프로그래밍을 적용하지 않았을 때
def fibo(x):
    if x==1 or x==2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(99))