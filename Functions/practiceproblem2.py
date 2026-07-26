def fact(n):
    val = 1
    for i in range(1, n+1):
        val *= i
    print(val)
    return val

fact(7)

