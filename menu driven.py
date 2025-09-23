#menu driven

menu={
    1:"pizza",
    2:"samosa",
    3:"pasta",
    4:"sandwich",
    5:"paratha",
    6:"coffe",
    7:"tea",
    8:"juice",
    9:"coke",
    10:"water"
}

for k,v in menu.items():
    print(f"press {k} for {v}")
opt=int(input("enter your option:"))
if opt==1:
    menuPizza={
        1:"Margherita",
        2:"Pepperoni",
        3:"Veggie",
        4:"Supreme",
    }
    for k,v in menuPizza.items():
        print(f"press {k} for {v}") 

    optPizza=int(input("enter your option:"))
    if optPizza==1:
        print("you have selected Margherita pizza")
    elif optPizza==2:
        print("you have selected Pepperoni pizza")
    elif optPizza==3:
        print("you have selected Veggie pizza")
    elif optPizza==4:
        print("you have selected Supreme pizza")
    else:
        print("you have selected wrong pizza") 

    sizePizza=input("enter your size:")
    if sizePizza=="small":
        print("you have selected small size pizza")
    elif sizePizza=="medium":
        print("you have selected medium size pizza")
    elif sizePizza=="large":
        print("you have selected large size pizza")
    else:
        print("you have selected wrong size pizza") 

    billPizza=0
    if optPizza==1:
        if sizePizza=="small":
            billPizza=100
        elif sizePizza=="medium":
            billPizza=150
        elif sizePizza=="large":
            billPizza=200
    elif optPizza==2:
        if sizePizza=="small":
            billPizza=120
        elif sizePizza=="medium":
            billPizza=170
    elif optPizza==3:
        if sizePizza=="small":
            billPizza=150
        elif sizePizza=="medium":
            billPizza=200
    elif optPizza==4:
        if sizePizza=="small":
            billPizza=180
        elif sizePizza=="medium":
            billPizza=230
    print(f"your bill is: {billPizza}")
    
    billPizza=billPizza+50
    print(f"your bill is: {billPizza}")
