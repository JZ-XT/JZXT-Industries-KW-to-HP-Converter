def print_menu():
    print (30 * "-" , "JZXT's Mechanic's Toolkit" , 30 * "-")
    print ("1. KW to HP Conversion")
    print ("2. HP to KW Conversion")
    print ("3. Feature Not Available")
    print ("4. Feature Not Available")
    print ("5. Exit")
    print (87 * "-")

  
while True:
    print_menu()
    choice = input("Enter your choice [1-5]: ")
    if choice==1:     
        print ("You Have Selected KW to HP Conversion")
        kw = input ('How many KW is the car making? ')
        hp = kw / 0.745699872
        print(str(kw) + ' KW is equivalent to {0:.2f}'.format(hp) + ' HP\n') # \n == newline carrage, acheives the same as print('')
    elif choice==2:
        print ("You Have Selected HP to KW Conversion")
        hp = input ('How much HP is the engine making? ')
        kw = hp * 0.745699872
        print(str(hp) + ' HP is equivalent to {0:.2f}'.format(kw) + ' KW\n\n')
    elif choice==3:
        print ("This feature is not yet available\n\n")
    elif choice==4:
        print ("This feature is not yet available\n\n")
    elif choice==5:
        print ("Exiting program...\n")
        break
