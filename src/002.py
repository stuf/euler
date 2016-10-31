"""
Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""
limit = 4000000

total = 0
x1 = 1
x2 = 2

if __name__ == "__main__":
    while True:
        if x2 % 2 == 0 and x2 < limit:
            total += x2
        elif x2 >= limit:
            break
        
        y = x1 + x2
        x1 = x2
        x2 = y

    print 'Sum: {}'.format(total)
