a = int(input())
d = 0
def findevenorodd(num, d):
    if(num%2 == 0):
        print("Number is Even")
        d = num
        return d
    else:
        print("Number is odd")


findevenorodd(a, d)