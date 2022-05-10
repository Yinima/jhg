
def greeting():
    print("------------------------------------------------------------\n")
    print(" ~~~~ Welcome to the Bike Management System~~~~\n "  )
    print("------------------------------------------------------------")



# using datetime module

import datetime;


def accessTime():
# todate stores today date
    todate = datetime.datetime.now()
    print("Today Date :-", todate)
  

def show_Bikes():
    print("------------------")
    print("Bike ID  Bike_name  Company Color Quantity Amount")
    print("------------------")
    file1=open("bikes.txt","w")
    bike_id=1

    for line in file1:
        print(bike_id,+line.replace(","))
        bike_id+=1
        print("--------------\n")
        file.close()
     
    
    
         
      




   
def bike_2D_list():
    with open('bikes.txt', 'r') as file:
        results = []
        for line in file:
            words = line.split(',')
            results.append((words[0:]))
    return results

         
def options():
    print("Select any of the options given below:")
    print("1. Display Bikes")
    print("2. Purchase bikes")
    print("3. Update Bikes")
    print("4. Close the program\n")
    

    option = 0 
    while not option in range(1,5):
        try:
            option = int(input("Enter your choice: \n"))
        except:
            print("nYou've entered out of range:\n")

    if option > 4 or option < 1:# if option is > 4 or < 1
        print("\nError found!! Plz enter only number listed below")
        options() #calling option()
    elif(option == 1):#if we enter 1 than bike details will be shown
        display_Bike()    
    elif(option == 2):#if we enter 3 than purchaseBike function will be called
        purchase_Bike()
    elif(option == 3):#if we enter 2 than updateQuantity function will be called.
        update_Quantity()
    elif(option == 4):#if we enter 4 than program will be closed
        print("Bye bye! Do visit again")
        quit()


def display_Bike():#Display Bikes
    results = bike_2D_list()############################

    for v in results:
        bike_id ,Name, Company, Color, Quantity, Amount = v# declaring V as variable and setting values as name, company etc
        print ("{:<25} {:<50} {:<20} {:<10} {:<10}".format(bike_id,name, company, color,Quantity,Amount.replace(',')))



def display_Bike():#Display Bikes
    print("------------------\n")
    print("|~~~ Display  Bikes ~~~ |\n")
    print("------------------\n")
    show_Bike()############## calling showBike function
    print('\n')
    options()#calling options method

def purchase_Bike():#Purchase bikes
    print("\n----------------------")
    print("|~~~ Purchase  Bikes ~ ~~ |")
    print("----------------------\n")
    #CustomerDetails
    Customer_name = input("\nEnter the Customer name: ")
    address = input("\nEnter the address of the buyer: ")
    phone_no = input("\nEnter the contact of the buyer: ")
    date = accessTime()#calling accessTime method

                      #int and str cannot be concate that's why str(accessTime())
    billName = Customer_name + str(accessTime()) + 'bikes.txt'###############################
    buyMore = True #buyMore is true
    allBike = {} # allBike is empty list
    while buyMore: # contion is 'if we want to buy more '
        show_Bike() # calling showBike function 
        bike = int(input("\nEnter the id of bike you would like to purchase:\n "))
        bikeQuantity = int(input("\nEnter the total quantity you want to purchase: "))

                          #######################
        if bikeQuantity > int(BikesDetails()[bike][4]): # in 4 number bike(MV Augusta ,it's total quamtity is 5 , if we enter 6 than it will show the error given below
            print("\nopps!, You've entered out of stock.Plz enter less than 5\n\n")
        else:

            results = BikesDetails()####################
            results[bike][4] = str(int(results[bike][4]) - bikeQuantity)##########
            with open('BikesDetails.txt', 'w') as f2:#######################
                data = ""
                for i in results:
                    for j in i:
                        data += str(j)+"," # str j + comma is assigned to data 
                    data = data[:-1] # it will give 0 to length list - 1 
                f2.write(data)

            allBike.update({bike:bikeQuantity})#updating bike id 0 to bike quanitity
            print("\nBike has been added for purchase.")
            print("\nDo you want to purchase more bikes? Press y for Yes and n for No\n")
            yes = int(input(" : "))##### PROMPT for yes (0 to len list)
            if yes == y:###########
                buyMore = False # it will repeat the loop
                

        with open(billName, 'w') as f:##############
            f.write('Customer Name: ' + Customer_name + '\nCustomer Address: ' + address + '\nCustomer Phone_no: ' + Phone_no + '\nPurchase Date: ' + date + '\n\n\nBikes Purchased:\n---------------------------------------------------------\n')
                       
        grandTotal = 0
        for i in allBike:
            with open(billName, 'a') as f:
                                #results in var i of indes 0   #results in var i of indes 2     #results in var i of indes 4    #results in variable i allBike                       ##replace with $ and coma       #results in var i allBike  
                f.write('Bike Name: ' + results[i][0] + '\nBike Color: ' + results[i][2] + '\nUnit Price: ' + results[i][4] + 'Quantity: ' + str(allBike[i]) + '\nTotal Amount: $' + str(int(results[i][4].replace('$',''))*allBike[i]) + '\n----\n')
            grandTotal = grandTotal + int(results[i][4].replace('$',''))*allBike[i]

        with open(billName, 'a') as f:############
            f.write('\nGrand Total: $' + str(grandTotal))#######

        print('\n\n Your selected bikes hasbeen purchased successfully. \n')

    options()#calling options() function 

def update_Quantity():
    print("\n\n------------------")
    print("|~~~ Update  Quantity~~~  |")
    print("------------------\n")
    Distributor_name = input("\nEnter the name of the Distributor: ")
    address = input("\nEnter the address of the Distributor: ")
    Phone_no = input("\nEnter the contact of the Distributor: ")
    date = accessTime()

    QuantityName = Distributor_name + str(accessTime()) + 'bikes.txt'#########
    addMore = True
    allBike = {} # empty list
    while addMore:
        showBike()
        bikeDetails = []
        bike = int(input("\nEnter the id of bike you want to add Stock: "))
        bikeQ = int(input("\nEnter the total quantity you want to add stock: "))
        ship = input("\nEnter the name of the Shipping Company: ")
        shipCost = input("\nEnter the shipping Cost: ")
        bikeDetails = [bikeQ,ship,shipCost.replace('$','')]


        results = bike_2D_list()
        results[bike][3] = str(int(results[bike][3]) + bikeQ)
        with open('bikes.txt', 'w') as f2:
            data = ""
            for i in results:
                for j in i:
                    data += str(j)+","
                data = data[:-1]
            f2.write(data)

        allBike.update({bike:bikeDetails})
        print("\nBike added to the stock.")
        print("\nDo you want to add more bikes? Press 1 for Yes and 0 for No\n")
        yesno = int(input(": "))
        if yesno == 0:
            addMore = False

        with open(stockName, 'w') as f:
            f.write('Distributor Name: ' + name + '\nDistributor Address: ' + address + '\nDistributor Contact' + contact + '\nTransation Date: ' + date + '\n\n\nBikes Added:\n---------------------------------------------------------\n')

        grandTotal = 0
        for i in allBike:
            with open(QuantityName, 'a') as f:
                f.write('Bike Name: ' + results[i][0] + '\nBike Color: ' + results[i][2] + '\nUnit Price: ' + results[i][4] + 'Quantity: ' + str(allBike[i][0]) + '\nTotal Amount: $' + str(int(results[i][4].replace('$',''))*allBike[i][0]) + '\nShipping Company' + allBike[i][1] + '\nShipping Cost: $' + allBike[i][2] +  '\n\n---------------------------------------------------------\n\n')
            grandTotal = grandTotal + int(results[i][4].replace('$',''))*allBike[i][0] + int(allBike[i][2])

        with open(stockName, 'a') as f:
            f.write('\nGrand Total: $' + str(grandTotal))

        print('\n\n Your selected bikes were added successfully. \n')
        #print(allBike)

    options()
