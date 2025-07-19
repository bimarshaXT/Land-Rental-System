import datetime

def rent_write(mydictionary, user_land, grand_total, name, phone):
    today_date_and_time = datetime.datetime.now()

    with open("data.txt", 'w') as file:
        for kitta_no, details in mydictionary.items():
            file.write(','.join(details) + '\n')

    with open(f"{name}{phone}.txt", 'w') as file:
        file.write("-" * 300)
        file.write("\n")
        file.write("\t\t\t\t\t\t\t\t\t Techno Property Nepal")
        file.write("\n")
        file.write("-" * 300)
        file.write("\n")
        file.write("\t\t\t\t\t\t | Contact: 9814206920 | E-mail: technoproperty2069@gmail.com |")
        file.write("\n")
        file.write("-" * 300)
        file.write("\n")
        file.write("\t\t\t\t\t\t\t\t Address: Kamaladi, Kathmandu")
        file.write("\n")
        file.write("-" * 300)
        file.write("\n")
        file.write("Name of the Customer: " + name + "\n")
        file.write("Phone number of Customer: " + str(phone) + "\n")
        file.write("Date and Time of Renting: " + str(today_date_and_time) + "\n")
        file.write("-" * 300)
        file.write("\n")
        file.write("\t\t Kitta NO. \t\t\t Aana  \t\t\t Month \t\t\t\t Price per Month  \t\t\t Total Price   \t\t\t City  \t\t\t Direction\n")
        file.write("\n")
        file.write("-" * 300)
        file.write("\n")

        for i in user_land:
            file.write("\t\t" + str(i[0]) + "\t\t\t\t" + str(i[1]) + "\t\t\t" + str(i[2]) + "\t\t\t\t" + str(i[3]) + "\t\t\t\t" + str(i[4]) + "\t\t\t\t" + i[5] + "\t\t\t\t" + i[6] + "\n")
            file.write("\n")
            file.write("-" * 300)
            file.write("\n")
        file.write("Grand Total is " + str(grand_total) + '\n')
        file.write("\nThank you for using Technorental services")
        
def return_write(mydictionary, returned_land, name, phone, final_total):
    today_date_and_time = datetime.datetime.now()

    with open("data.txt", 'w') as file:
        for kitta_no, details in mydictionary.items():
            file.write(','.join(details) + '\n')

    with open("return.txt", 'w') as file:
        file.write("-" * 300)
        file.write("\n")
        file.write("\t\t\t\t\t\t\t\t\t Techno Property Nepal")
        file.write("\n")
        file.write("-" * 300)
        file.write("\n")
        file.write("\t\t\t\t\t\t | Contact: 9814206920 | E-mail: technoproperty2069@gmail.com |")
        file.write("\n")
        file.write("-" * 300)
        file.write("\n")
        file.write("\t\t\t\t\t\t\t\t Address: Kamaladi, Kathmandu")
        file.write("\n")
        file.write("-" * 300)
        file.write("\n")
        file.write("Name of the Customer: " + name + "\n")
        file.write("Phone number of Customer: " + str(phone) + "\n")
        file.write("Date and Time of Renting: " + str(today_date_and_time) + "\n")
        file.write("-" * 300 + "\n")
        file.write("\nKitta NO. \t\t Aana \t\t City \t\t Direction \t\t Rented Months \t\t Per Month Price \t\t Fine Amount \t\t Total Price")
        file.write("\n")
        file.write("-" * 300)
        file.write("\n")

        for land in returned_land:

            file.write(str(land[0]) + "\t\t\t" + str(land[1]) + "\t\t" + str(land[2]) + "\t\t\t" + str(land[3]) + "\t\t\t" + str(land[4])+ "\t\t" + str(land[5]) + "\t\t\t" + str(land[6]) + "\t\t" + str(land[7]))
            file.write("\n")
            file.write("-" * 300)
            file.write("\n")
        file.write("The total amount is:" + str(final_total) + '\n')  # Write final total
        file.write("\nThank you for using Techno Properties\n")


def extend_write(mydictionary, extended_contracts, name, phone, total_price):
    today_date_and_time = datetime.datetime.now()
    
    with open("data.txt", 'w') as file:
        for kitta_no, details in mydictionary.items():
            file.write(','.join(details) + '\n')

    with open("extension.txt", 'w') as file:
        file.write("\n")
        file.write("\t\t\t\t\t\t\t\t\t\t\t Techno Property Nepal")
        file.write("\n")
        file.write("\t\t\t\t\t\t\t\t Address: Kamalpokhari, Kathmandu Metro")
        file.write("\n")
        file.write("\t\t\t\t\t\t\t\t Contact: 9816942059 || Email: techno@gmail.com")
        file.write("\n")
        file.write("Name of the Customer: " + name + "\n")
        file.write("Phone number of Customer: " + str(phone) + "\n")
        file.write("Date and Time of Extending Contract: " + str(today_date_and_time) + "\n")
        file.write("-" * 165)
        file.write("\nKitta NO. \t\t Aana \t\t City \t\t Direction \t\t Rented Months \t\t Per Month Price \t\t Fine Amount \t\t Total Price")
        file.write("-" * 165)
        file.write("\n")

    
        for land in extended_contracts:
                
            file.write(str(land[0]) + "\t\t\t" + str(land[1]) + "\t\t" + str(land[2]) + "\t\t\t" + str(land[3]) + "\t\t\t" + str(land[4])+ "\t\t" + str(land[5]) + "\t\t\t" + str(land[6]) + "\t\t" + str(land[7]))
            file.write("\n")
            file.write("-" * 300)
            file.write("\n")
        file.write("The total amount is:" + str(total_price) + '\n')  # Write total amount
        file.write("\nThank you for using Techno Properties\n")
