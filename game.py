#Welcome screen
description = "big room with chandelar haging from the roof, and paintings all."
doors = ["north", "south", "west", "east"]

#Start Game
print("Hej Välkommen till Wendis Spel")
print("*******************************")
print("                      ")

#main loop
run = True
while run:
    
    #Print room
    print("you are standing in a " + description)
    print("There are doors tou your: ", doors)
    print("")
    
    #menu
    print("What do you want to do?")
    print("1. Go to north")
    print("2. Go to west")
    print("3. Go to south")
    print("4. Go to east")
    print("5. Look")
    print("0. Guit Game")
    
    #ask user for input
    choice = input("Select a option")
    
    #Sanitize user input
    if not choice.isnumeric():
        print("Sorry! did not understand what you mean?")
        continue
    #Do something based on what the user asks for..
    #if the user enters something you dondt understand, let him knom.
    choice = int(choice)
    if choice == 0:
        run = False
    elif choice == 1:
        print("you are going north ")
        print("------------------------")
    elif choice == 2:
        print("you are going west")
        print("------------------------")
    elif choice == 3:
        print("you are going south")
        print("------------------------")
    elif choice == 4:
        print("you are going east")
        print("------------------------")
    elif choice == 5:
        print("you are looking really hard, but can find anything new ")
        print("------------------------")
    else:
        print("Sorry, you asked for something i cannot do! ")
        print("------------------------")