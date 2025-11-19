#creating lists to store employee details
employee_name = []
employee_ID = []
properties_sold = []

#for employee of the week
bonus_percent = 0.15

#commission amount
commission_per_sale = 500 

#commission rate per property calculation
def commission_calculation(properties_sold):
    return properties_sold * commission_per_sale



#input number of employees
#the number of employees inputed will determine the number of times the user input will be displayed

number_of_employee = int(input("How many employees are there? : "))
print()

for i in range (0,number_of_employee):
    EmployeeName = input("\nEnter employee name: ")
    employee_name.append(EmployeeName)

    EmployeeID = int(input("\nEnter employee's ID number: "))
    employee_ID.append(EmployeeID)

    PropertiesSold = int(input("\nEnter number of properties sold: "))
    properties_sold.append(PropertiesSold)



#menu displays
#define the menu function outside the loop
def menu_list():
    print('''
    1. Employee List.
    2. Sales commission for each employee.
    3. Total sales commission for the week. 
    4. Total number of properties sold.
    5. Employee of the week award.
    6. Bonus amount.
    7. Do you want to see menu again? (Y/N)''')

while True:
#calling a function
    menu_list()

    print()
    choice = int(input("Choose a number from the menu: "))

    if choice == 1:
        print()
        #diplay ranked employee list based on properties sold
        print("Employee List: ")
        
        #combining into a list of tuple
        employee_information = list(zip(employee_name, properties_sold)) #zip() used to combine into a list of tuples 'employee_information'

        #bubble sort  ranks from highest to lowest
        n = len(employee_information)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if employee_information[j][1] < employee_information[j + 1][1]:
                    employee_information[j], employee_information[j + 1] = employee_information[j + 1], employee_information[j]

    # Display the sorted list
        for rank, (name, sold) in enumerate(employee_information, start=1):
            print(f"{rank}. {name} - Properties Sold: {sold}")
        

    elif choice == 2:
        print()
        print("Sales commisiion for each employee: ")
        print()

    #display sales commission for each employee
        for sale in range(len(employee_name)):
            commission = commission_calculation(properties_sold[sale])
            approximate_commission = round(commission, 2)
            print(f"{employee_name[sale]} - Sales Commission: £{approximate_commission}")
    
    elif choice == 3:
        print()
    #display total sales commission for the week
        total_commission = sum(commission_calculation(sold) for sold in properties_sold)
        approximate_commission_total = round(total_commission, 2)
        print(f"Total commission for the week: £{approximate_commission_total}")
        
    elif choice == 4: 
        print()
    #display total numbers of properties sold
        total_properties_sold =  sum(properties_sold)  #calculate the sum of values in 'properties_sold' list
        print(f"Total Properties Sold for the week: {total_properties_sold}")
        

    elif choice == 5:
        li = properties_sold
        index = -1
        highest = -1
        for i in range(len(li)):
                if li[i]> highest:
                   highest = li[i]
                   index = i 
    #display employee of the week (name, employee ID, properties sold)           
        print()
        print(f"Employee of the week: \nName: {employee_name[index]} \nEmployee ID: {employee_ID[index]} \nNumber of properties sold: {properties_sold[index]}") #-1 says pick the last one 

        

    #calculates bonus amount 
    elif choice == 6:
        ni = properties_sold
        index_2 = -1              #Stores employee with highest properties sold
        highest_2 = - 1           #stores highest number of properties sold 
        for p in range(len(ni)):
                if ni[p]> highest_2:
                   highest_2 = ni[p]
                   index_2 = p
    #display bonus amount
        print()
        print(f"Employee of the week: \nName: {employee_name[index_2]} \nBonus amount: £{properties_sold[index_2] *commission_per_sale * bonus_percent} ") #[-1] picks the lowest property_sold then calculate to get bonus amount


    elif choice == 7:
        print()
        Exit_choice = input("Do you want to see menu again? (Y/N) ")
        if Exit_choice == "Y" or Exit_choice == "y":
            menu_list()  #can also use 'continue'
        elif Exit_choice =="N" or Exit_choice == "n":
            print("Exiting program, bye!")
            break     
        else:
            print("Invalid choice. Exiting program. ") 










