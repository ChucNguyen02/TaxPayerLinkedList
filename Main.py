from TaxPayer import TaxPayer
from Node import Node
from TaxPayerLinkedList import TaxPayerLinkedList

def main():
    tax_list = TaxPayerLinkedList()
    
    while True:
        print("\n===== INCOME TAX CALCULATOR =====")
        print("1. Load data from file")
        print("2. Input & add to end")
        print("3. Display data")
        print("4. Save data to file")
        print("5. Search by code")
        print("6. Delete by code")
        print("7. Sort by code")
        print("8. Input & add to beginning")
        print("9. Add after position k")
        print("10. Delete position k")
        print("0. Exit")
        
        try:
            choice = int(input("\nEnter your choice (0-10): "))
            
            if choice == 1:
                filename = "data.txt"
                success = tax_list.load_from_file(filename)
                print("Data loaded successfully." if success else "Data loaded fail!!!")

            elif choice == 2:
                code = input("Enter taxpayer code: ")
                name = input("Enter taxpayer name: ")
                try:
                    income = float(input("Enter income: "))
                    deduction = float(input("Enter deduction: "))
                    tax_list.add_to_end(code, name, income, deduction)
                except ValueError:
                    print("Invalid input. Income and deduction must be numbers.")

            elif choice == 3:
                tax_list.display_all()

            elif choice == 4:
                filename = "data.txt"
                tax_list.save_to_file(filename)

            elif choice == 5:
                code = input("Enter code to search: ")
                taxpayer = tax_list.search_by_code(code)
                if taxpayer:
                    print("\nTaxpayer found:")
                    print(f"Code      : {taxpayer.code}")
                    print(f"Name      : {taxpayer.name}")
                    print(f"Income    : {taxpayer.income:.2f}")
                    print(f"Deduction : {taxpayer.deduction:.2f}")
                    print(f"Tax       : {taxpayer.tax:.2f}")
                else:
                    print(f"No taxpayer with code '{code}' found.")

            elif choice == 6:
                code = input("Enter code to delete: ")
                tax_list.delete_by_code(code)

            elif choice == 7:
                tax_list.sort_by_code()

            elif choice == 8:
                code = input("Enter taxpayer code: ")
                name = input("Enter taxpayer name: ")
                try:
                    income = float(input("Enter income: "))
                    deduction = float(input("Enter deduction: "))
                    tax_list.add_to_beginning(code, name, income, deduction)
                except ValueError:
                    print("Invalid input. Income and deduction must be numbers.")

            elif choice == 9:
                try:
                    pos = int(input("Enter position (k): "))
                    code = input("Enter taxpayer code: ")
                    name = input("Enter taxpayer name: ")
                    income = float(input("Enter income: "))
                    deduction = float(input("Enter deduction: "))
                    tax_list.add_after_position(pos, code, name, income, deduction)
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")

            elif choice == 10:
                try:
                    pos = int(input("Enter position (k) to delete: "))
                    tax_list.delete_at_position(pos)
                except ValueError:
                    print("Invalid input. Position must be a number.")

            elif choice == 0:
                print("Exiting program. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 11.")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
