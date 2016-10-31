"""
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
if __name__ == "__main__":
    target_number = 600851475143
    factors = []

    while True:
        for i in range(1, 10000):
            if target_number % i == 0:
                factors.append(i)
                target_number /= i
        
        if target_number == 1:
            break
    
    print 'Max: {}'.format(max(factors))
