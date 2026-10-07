def nthfibonacci(n:int) -> int:
    num = [0,1]
    for i in range(2,n+1):
        num.append(num[i-1] + num[i-2])

    return num[n]


n = int(input ("Enter the number:"))
result = nthfibonacci(n)
print(result)