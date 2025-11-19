# shopping_list_manager.py

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
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number 1-4.")
            continue

        if choice == 1:
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"{item} added to the shopping list.")
            else:
                print("Item cannot be empty.")

        elif choice == 2:
            if not shopping_list:
                print("The shopping list is empty. Nothing to remove.")
                continue
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from the shopping list.")
            else:
                print(f"{item} not found in the shopping list.")

        elif choice == 3:
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("Current Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
