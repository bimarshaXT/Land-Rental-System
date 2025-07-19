import datetime
import write

def rent_land(mydictionary, name, phone):
    continue_loop = True
    user_land = []
    grand_total = 0  # Initialize grand_total here
    while continue_loop:
        kitta_no = int(input("Please select the kitta number: "))
        while kitta_no <= 100 or kitta_no > len(mydictionary) + 100 or mydictionary[kitta_no][4].lower() != "available":
            if kitta_no <= 100 or kitta_no > len(mydictionary) + 100:
                print("Enter a correct kitta number.")
            elif mydictionary[kitta_no][4].lower() != "available":
                print("Sorry, this land is not available for rent. Please choose another one.")
            else:
                break
            kitta_no = int(input("Please select the kitta number: "))

        aana_land = int(mydictionary[kitta_no][2])
        print(f"{kitta_no} Kitta number has {aana_land} aana of land")
        month = int(input("Enter the month you want to rent for: "))
        per_month_price = int(mydictionary[kitta_no][3])

        # Change availability to "Not Available" in mydictionary
        mydictionary[kitta_no][4] = "Not Available"

        bill_kitta_number = kitta_no
        aana = aana_land
        rented_month = month
        city = mydictionary[kitta_no][0]
        direction = mydictionary[kitta_no][1]
        per_month_price_land = per_month_price
        total_price = rented_month * per_month_price_land

        user_land.append([bill_kitta_number, aana, rented_month, per_month_price_land, total_price, city, direction])
        more = input("Do you want more? Press y to confirm: ")

        if more.lower() != "y":
            continue_loop = False
            for i in user_land:
                grand_total += int(i[4])  # Add the total price of each land
                
    # Print rented land details
    print("-" * 184)
    print("\n")
    print("\t\t\t\t\t\t\t\t\t\t\t Techno Property Nepal")
    print("\n")
    print("-" * 184)
    print("\t\t\t\t\t\t\t\t | Contact: 9814206920 | E-mail: technoproperty2069@gmail.com |")
    print("\n")
    print("-" * 184)
    print("\n")
    print("\t\t\t\t\t\t\t\t Address: Kamaladi, Kathmandu")
    print("-" * 184)
    print("\n")
    print("Date and Time of Returning: ", datetime.datetime.now(), "\n")
    print("-" * 184)
    print("\n")
    print("\t Kitta NO. \t\t Aana \t\t Month \t\t Price per Month \t\t Total Price   \t\t\tCity  \t\t Direction\n")
    print("\n")
    print("-" * 184)
    print("-" * 184)
    print("\n")
    for i in user_land:
        print("\t", i[0], "\t\t\t", i[1], "\t\t\t", i[2], "\t\t\t", i[3], "\t\t\t", i[4], "\t\t\t", i[5], "\t\t", i[6])
    print("\n")
    print("-" * 184)    
    print("Grand Total is", grand_total)
    print("Thank you for using Techno Properties")

    # Call rent_write here
    write.rent_write(mydictionary, user_land, grand_total, name, phone)
    
    return user_land  # Return user_land after finishing renting


def return_land(mydictionary, name, phone):
    continue_loop = True
    returned_land = []
    final_total = 0
    
    while continue_loop:
        kitta_no = int(input("Enter the kitta number of the land you want to return: "))
        
        while kitta_no <= 100 or kitta_no > len(mydictionary) + 100 or mydictionary[kitta_no][4] == "Available":
            if kitta_no <= 100 or kitta_no > len(mydictionary) + 100:
                print("Enter a correct kitta number.")
            elif mydictionary[kitta_no][4] == "Available" :
                print("Sorry, this land can not be for return. Please choose another one.")
            kitta_no = int(input("Please select the kitta number: "))

        aana_land = int(mydictionary[kitta_no][2])
        rented_month= int(input("Enter the month had rented for: "))
        returned_month = int(input("enter the month you returned after: "))
        per_month_price = int(mydictionary[kitta_no][3])

        mydictionary[kitta_no][4] = "Not Available"        
        bill_kitta_number = kitta_no
        aana = aana_land
        city = mydictionary[kitta_no][0]
        direction = mydictionary[kitta_no][1]
        per_month_price_land = per_month_price
        total_price = rented_month * per_month_price_land
        diff = returned_month - rented_month
        fine_amount = 0  # No fine

        if diff > 0:
                # Calculate fine
                fine_percentage = 0.1  # 10% fine per month
                fine_amount = diff * fine_percentage * per_month_price
                total_price += fine_amount
                print("the fined amount is: " + str(fine_amount))
                print("The total amount after being fined is:", str(total_price))
        else:
                fine_amount = 0
                print("The total amount is:"+ str(total_price))

        returned_land.append([bill_kitta_number, aana, city, direction, rented_month, per_month_price_land, fine_amount, total_price])
        more = input("Do you want to return more? Press y to confirm: ")
        if more.lower() != "y":
            continue_loop = False
            for i in returned_land:
                final_total += int(i[7])  # Add the total price of each land


    print("-" * 184)
    print("\n")
    print("\t\t\t\t\t\t\t\t\t\t\t Techno Property Nepal")
    print("\n")
    print("-" * 184)
    print("\t\t\t\t\t\t\t\t | Contact: 9814206920 | E-mail: technoproperty2069@gmail.com |")
    print("\n")
    print("-" * 184)
    print("\n")
    print("\t\t\t\t\t\t\t\t | Contact: 9814206920 | E-mail: technoproperty2069@gmail.com |")
    print("\n")
    print("-" * 184)
    print("\n")
    print("\t\t\t\t\t\t\t\t Address: Kamaladi, Kathmandu")
    print("\n")
    print("-" * 184)
    print("\n")
    print("Date and Time of Renting: ", datetime.datetime.now(), "\n")
    print("\n")
    print("-" * 184)
    print("\n")
    print(" Kitta NO. \t\t Aana \t\t City \t\t Direction \t\t Rented Months \t\t Per Month Price \t\t Fine Amount \t\t Total Price")
    print("\n")
    print("-" * 184)
    print("-" * 184)
    print("\n")
    for land in returned_land:
        print(str(land[0]) + "\t\t\t" + str(land[1]) + "\t\t" + str(land[2]) + "\t\t\t" + str(land[3]) + "\t\t\t" + str(land[4])+ "\t\t" + str(land[5]) + "\t\t\t" + str(land[6]) + "\t\t" + str(land[7]))
        print("-" * 165)
    print("The total amount is:", str(final_total))  # Print final total
    print("\n")
    print("-" * 184)
    # Call return_write function to write returned land details into a file
    write.return_write(returned_land, name, phone, final_total)
    return returned_land




def extend_contract(mydictionary, name, phone):
    continue_loop = True
    extended_contracts = []
    
    while continue_loop:
        kitta_no = int(input("Enter the kitta number of the land you want to extend: "))
        
        while kitta_no <= 100 or kitta_no > len(mydictionary) + 100:
            if kitta_no <= 100 or kitta_no > len(mydictionary) + 100:
                print("Enter a correct kitta number.")
            else:
                print("Sorry, this land is not available for return. Please choose another one.")
            kitta_no = int(input("Please select the kitta number: "))

        aana_land = int(mydictionary[kitta_no][2])
        rented_month= int(input("Enter the month had rented for: "))
        returned_month = int(input("enter the month you want to return for: "))
        extend_month = int(input("enter the month you want to extend for: "))
        per_month_price = int(mydictionary[kitta_no][3])

        bill_kitta_number = kitta_no
        aana = aana_land
        city = mydictionary[kitta_no][0]
        direction = mydictionary[kitta_no][1]
        total_month = rented_month + extend_month
        per_month_price_land = per_month_price
        total_price = total_month * per_month_price_land
        diff = returned_month - rented_month
        fine_amount = 0  # No fine

        if diff > 0:
                # Calculate fine
                fine_percentage = 0.1  # 10% fine per month
                fine_amount = diff * fine_percentage * per_month_price
                total_price += fine_amount
                print("The total amount after being fined is:", str(total_price))
        else:
                print("The total amount is:", str(total_price))
        
        extended_contracts.append([bill_kitta_number, aana, city, direction, rented_month, per_month_price_land, fine_amount, total_price])
        continue_loop = False

    # Print extended contract details
    print("-" * 184)
    print("\n")
    print("\t\t\t\t\t\t\t\t\t\t\t Techno Property Nepal")
    print("\n")
    print("-" * 184)
    print("\t\t\t\t\t\t\t\t | Contact: 9814206920 | E-mail: technoproperty2069@gmail.com |")
    print("\n")
    print("-" * 184)
    print("\n")
    print("\t\t\t\t\t\t\t\t | Contact: 9814206920 | E-mail: technoproperty2069@gmail.com |")
    print("-" * 184)
    print("\n")
    print("\t\t\t\t\t\t\t\t Address: Kamaladi, Kathmandu")
    print("-" * 184)
    print("\n")
    print("Date and Time of Returning: ", datetime.datetime.now(), "\n")
    print("-" * 184)
    print("\n")
    print("\t\t\t Kitta NO. \t Aana \t City \t Direction  \t Rented Months \t Per Month Price \t Fine Amount \t Total Price")
    print("-" * 184)
    print("-" * 184)
    print("\n")
    for land in extended_contracts:
        print("\t\t\t" + str(land[0]) + "\t\t" + str(land[1]) + "\t" + str(land[2]) + "\t" + str(land[3]) + "\t" + str(land[4])+ "\t" + str(land[5]) + "\t" + str(land[6]) + "\t" + str(land[7]))
        print("-" * 184)
    print("The total amount is:", str(total_price))  # Print final total
    print("\n")
    print("-" * 184)
    write.extend_write(mydictionary, extended_contracts, name, phone, total_price)

    return extended_contracts
