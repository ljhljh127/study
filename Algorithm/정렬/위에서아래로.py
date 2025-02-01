
def uptodown():
    n = int(input())
    array = []
    for _ in range(n):
        array.append(int(input()))

    array.sort(reverse=True)
    return array

print(uptodown())