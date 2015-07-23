def is_prime(n):
    if n % 2 != 0:
        for i in range(3, n):
            if n % i == 0:
                return False
        return True

list = []

for number in range(1, 10000):
    if is_prime(number):
        if str(number)[::-1] == str(number):
            list.append(number)
# print list

print list.pop()
