def collatz_checker(n):
    if n<1:
        print("Not Valid")

    if n>1:
        while n>1:
            
            if n%2!=0:
                n = (3*n) +1 
                print(int(n))

            elif n%2==0:
                n /= 2
                print(int(n))

            
        print("Collatz Sequence Verified")

n = int(input("Enter starting point for collatz sequence : "))

collatz_checker(n)
