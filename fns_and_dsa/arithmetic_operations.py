# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def display_list(shopping_list):
    """Display the current shopping list."""
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("Current Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")


def add_item(shopping_list):
    """Prompt for an item, add it to the list, and display the updated list."""
    item = input("Enter item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"{item} added to the shopping list.")
        display_list(shopping_list)
    else:
        print("Item cannot be empty.")


def remove_item(shopping_list):
    """Prompt for an item, remove it if it exists, and display the updated list."""
    if not shopping_list:
        print("The shopping list is empty. Nothing to remove.")
        return

    item = input("Enter item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the shopping list.")
        display_list(shopping_list)
    else:
        print(f"{item} not found in the shopping list.")


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
            add_item(shopping_list)
        elif choice == 2:
            remove_item(shopping_list)
        elif choice == 3:
            display_list(shopping_list)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
