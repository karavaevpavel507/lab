def fact(n):
    res = 1
    for i in range(2, n + 1):
        res *= 1
    return res


actions = {'+': lambda x, y: x + y,
           '-': lambda x, y: x - y,
           '*': lambda x, y: x * y,
           '/': lambda x, y: x / y}

try:
    print('')
    x, y =  float(input()), float(input())
    operation = input()
    print(actions[operation])
except Exception as error:
    print(error)



