print("*******************************************")
print("***       Number System Conversion      ***")
print("*** Francis Rabanes and Shane Quinquino ***")
print("*******************************************")

print("")
print("*********************************")
print("|  [ 1 ] Binary Conversion      |")
print("|  [ 2 ] Octal Conversion       |")
print("|  [ 3 ] Hexadecimal Conversion |")
print("*********************************")
selec = int(input("Which Conversion?"))

if selec == 1:
    num = int(input("Enter Number: "))
    print("[",format( num, "b"),"]")
elif selec == 2:
    num = int(input("Enter Number: "))
    print("[",format( num, "o"),"]")
elif selec == 3:
    num = int(input("Enter Number: "))
    print("[",format( num, "x"),"]")
else:
    print("****************************************")
    print("*** Invalid input. Please try again. ***")
    print("****************************************")