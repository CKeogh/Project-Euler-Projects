def is_prime(n):
    for i in range(2, n):
        if n %i == 0:
            return False
    return True

sum = 0
userRange = int(input("please enter a range: "))

for i in range(2, userRange):
    if is_prime(i):
        sum += i
print("THE ANSWER IS %d" % (sum))
