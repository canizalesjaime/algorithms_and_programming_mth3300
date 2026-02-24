def question1():
    x=int(input("Enter Number: "))
    if x > 0:
        print("positive")
    elif x < 0:
        print("negative")
    else:
        print("zero")


def question2():
    i = 1
    while i < 21:
        if i == 13:
            break
        else:
            print(i)


def question3():
    numbers = [3, 8, 12, 7, 5, 10, 6]
    for x in numbers:
        if x%2==0:
            print(x)


#question4 part 1
def decimal_to_binary(dec):
    bin=""
    while dec > 0:
        if dec%2==0:
            bin="0"+bin
        else:
            bin="1"+bin
        dec=dec//2

    return bin

# question 4 part 2
def hexa_to_decimal(hexa):
    exp = len(hexa)-1
    hexa_map={'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    sum = 0
    for d in str(hexa):
        d=d.lower()
        if d in hexa_map:
            sum = hexa_map[d]*(16**exp)+sum

        else:
            sum = int(d)*(16**exp)+sum

        exp=exp-1 

    return sum
    #return int(hexa, 16) #simpler built in approach


print(decimal_to_binary(5))
print(decimal_to_binary(256))
print(decimal_to_binary(14))