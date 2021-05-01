n= int(input("digame un numero: "))
for i in range(1,11):
    print(n,"*",i , "=", n*i)


name = input("dime tu nombre: ")
number = int(input("dime un numero: "))
for i in range(number):
    if(i < number):
        print("Name_ ", name)

number = int(input("dime un numero: "))
for i in range(number):
    num = 7 * i
    if( num <= number and num != 0):
        print(num)
