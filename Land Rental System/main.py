
import read
import operation
import write

def main():
    print("-" * 184)
    print("\n")
    print("\t\t\t\t\t\t\t\t\t\t Techno Property Nepal")
    print("\n")
    print("-" * 184)
    print ("\n")
    print("\t\t\t\t\t\t\t\t | Contact: 9814206920 | E-mail: technoproperty2069@gmail.com")
    print ("\n")
    print("-" * 184)
    print ("\n")
    print("\t\t\t\t\t Welcome to Techno Property Nepal: Your gateway to Explore, Rent and Manage land properties all over Nepal")
    print ("\n")
    print("-" * 184)
    print ("\n")
    name = input("enter your name: ")
    phone = int(input("enter your number: "))
    print("\t\t\t\t\t\t\t\t\tDetails of the lands in our database:")
    print("\n")

    mydictionary = read.read_data("data.txt")  # Read land details from file

    print("Below are the options available with us.")
    print("\n")
    print("-" * 184)
    print("-" * 184)
    print("\n")
    print("\t\t\tKitta no. \t\t\t District \t\t Direction \t\t\t Anna \t\t\t Price \t\t\t Availability")
    print("\n")
    print("-" * 184)
    print("-" * 184)
    print("\n")
    # Print land details
    for kitta_no, details in mydictionary.items():
        print("\t\t\t" + str(kitta_no) + "\t\t\t\t" + str(details[0]) + "\t\t\t" + str(details[1]) + "\t\t\t" + str(details[2]) + "\t\t\t" + str(details[3]) + "\t\t\t" + str(details[4]) + "\n")
    print("-" * 184)
    choice = None
    # Menu for the user to choose between renting, returning, or exiting
    while True:
        print("\n")
        print("1. Rent Land")
        print("2. Return Land")
        print("3. Extend Contract")
        print("4. Exit")


        try: 
            choice = int(input("Enter your choice: "))
        except ValueError: 
            print("Error: Please enter a valid integer value.")


        if choice == 1:
            operation.rent_land(mydictionary, name, phone)
        elif choice == 2:
            operation.return_land(mydictionary, name, phone)
        elif choice == 3:
            operation.extend_contract(mydictionary, name, phone)  
        elif choice == 4:
            print("Thank you for visiting our System")
            break
    else:
        print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()



