num = int(input("enter the number:"))
if num == 1:
    print("is not prime number")
if num > 1:
    for n in range(2, num):
        if num % 2 == 0:
            print(num, "is not prime")
            break

    else:
        print(num, "is a prime number")
