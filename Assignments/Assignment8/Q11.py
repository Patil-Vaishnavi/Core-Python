
def armstrong(n):
    original = n
    total = 0
    digits = len(str(n))

    while n > 0:
        digit = n % 10
        total += digit ** digits
        n = n // 10

    if total == original:
        print("Armstrong number")
    else:
        print("Not Armstrong number")

n = int(input("Enter number: "))
armstrong(n)
