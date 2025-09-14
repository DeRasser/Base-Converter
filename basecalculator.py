x = int(input('Enter your number: '))
base = int(input('Enter base of your number: '))
for i in str(x):
        if int(i) >= base:
            print("The number doesn't match your base!")
            exit()
tobase = int(input('Enter base you want to convert your number to(max36): '))
alif = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dig = 0
res = ''
internum = 0

if base == 10:
    while x != 0:
        dig = x % tobase
        res = alif[dig] + res
        x //= tobase
    print(res)
else:
    for i in range(len(str(x))):
        internum = internum + int(str(x)[::-1][i]) * base ** i
    while internum != 0:
        dig = internum % tobase
        res = alif[dig] + res
        internum //= tobase
    print(res)




