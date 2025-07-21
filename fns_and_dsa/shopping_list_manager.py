def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            if item.strip():
                shopping_list.append(item.strip())
                print(f"'{item.strip()}' has been added to the shopping list.")
            else:
                print("No item entered.")

        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item.strip() in shopping_list:
                shopping_list.remove(item.strip())
                print(f"'{item.strip()}' has been removed from the shopping list.")
            else:
                print(f"'{item.strip()}' not found in the shopping list.")

        elif choice == '3':
            if shopping_list:
                print("Current Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Shopping list is empty.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
