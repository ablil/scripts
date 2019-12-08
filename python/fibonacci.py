def fibonacci(n):
    ''' return the n'th number of fibonacci sequence '''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_list(n):
    # return a list of fibonacci numbers
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else :
        res = [0, 1]
        i = 3
        while i <= n :
            res.append(res[len(res)-1] + res[len(res) - 2])
            i += 1
        return res
