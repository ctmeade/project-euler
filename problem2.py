### By considering the terms in the Fibonacci sequence
### whose values do not exceed four million, find the sum\
### of the even-valued terms.
# By Chris Meade

def evenFib(max):
        finalAns = 0
        a = 1
        b = 2
        while a <= max:
            if a % 2 == 0:
                finalAns += a
            a, b = b, a + b
        return str(finalAns)
    
print(evenFib(4000000))

