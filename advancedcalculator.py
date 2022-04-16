def gather(number1,number2):
    return number1 + number2
def interest(number1,number2):
    return number1 - number2
def multiply(number1,number2):
    return number1 * number2
def divide(number1,number2):
    return number1 / number2

print("Operation : ")
print("1 : Gather ")
print("2 : Interest ")
print("3 : Multiply  ")
print("4 : Divide ")

choose = print(int(input("Choose Operation")))
number1 = print(int(input("Sayi 1 Giriniz :")))
number2 = print(int(input("Sayi 2 Giriniz :")))
if choose == '1':
    print("Total: "+str(gather(number1,number2)))
elif choose  =='2':
    print("Extraction : "+str(interest(number1,number2)))
elif choose  == '3':
    print("Impact: "+str(multiply(number1,number2))
elif choose  == '4':
    print("Divide : "+str(divide(number1,number2)))
