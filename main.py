#from turtle import Turtle,Screen

#a class begins with a capital letter
#timmy = Turtle()
#timmy.shape("turtle")
#timmy.color("red")

#my_screen = Screen() #the screen is a class and my_screen is a variable
#print(my_screen.canvheight)  #.canvaheight is the attribute
#my_screen.exitonclick() 

#object and methods
#e.g car.stop() car is the object and .stop() is the method

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}):")
    if choice == 'off':
        is_on = False
        print("The machine is turned off")
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        #print(drink)
        
        