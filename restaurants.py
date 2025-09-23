#menu driven


print("Welcome to the restaurant by shyamsir \n")

print("Please select the item from the menu")
print("1. Pizza")
print("2. Burger")
print("3. Salad")
print("4. Coke")
print("5. Pepsi")
print("6. Water")
print("7. Exit")

op=int(input("Enter your choice: "))
if op==1:
    print("You have selected Pizza")
    qty=int(input("enter qty =>"))
    price=qty*100
    print("Your total amount is =>",price)

elif op==2:
    print("You have selected Burger")
    qty=int(input("enter qty =>"))
    price=qty*50
    print("Your total amount is =>",price)

elif op==3:
    print("You have selected Salad") 
    qty=int(input("enter qty =>"))
    price=qty*20
    print("Your total amount is =>",price)
    
elif op==4:
    print("You have selected Coke")
    qty=int(input("enter qty =>"))
    price=qty*20
    print("Your total amount is =>",price)

elif op==5:
    print("You have selected Pepsi")    
    qty=int(input("enter qty =>"))
    price=qty*20
    print("Your total amount is =>",price)

elif op==6:
    print("You have selected Water")
    qty=int(input("enter qty =>"))
    price=qty*20
    print("Your total amount is =>",price)

elif op==7:
    print("Thank you for visiting")
    print("Your total amount is =>",price)

else:
    print("Please select a valid item from the menu")