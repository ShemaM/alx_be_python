# shopping_list_manager.py

def display_menu():
    print("\n=== Shopping List Manager ===")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def display_list(shopping_list):
    """Display the current shopping list."""
    if not shopping_list:
        print("The shopping list is empty.", flush=True)
    else:
        print("\nCurrent Shopping List:", flush=True)
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}", flush=True)


def add_item(shopping_list):
    """Prompt the user to add an item and display the updated list."""
    item = input("Enter item to add: ").strip()
    if not item:
        print("Item cannot be empty.", flush=True)
        return

    # Prevent duplicates (case-insensitive)
    if item.lower() in (x.lower() for x in shopping_list):
        print(f"'{item}' is already in the shopping list.", flush=True)
        return

    shopping_list.append(item)
    print(f"'{item}' has been added.", flush=True)
    display_list(shopping_list)


def remove_item(shopping_list):
    """Prompt the user to remove an item by name or index and display the updated list."""
    if not shopping_list:
        print("The shopping list is empty. Nothing to remove.", flush=True)
        return

    display_list(shopping_list)
    user_input = input("Enter item name or number to remove: ").strip()

    if not user_input:
        print("Invalid input.", flush=True)
        return

    # Remove by number
    if user_input.isdigit():
        index = int(user_input)
        if 1 <= index <= len(shopping_list):
            removed = shopping_list.pop(index - 1)
            print(f"'{removed}' has been removed.", flush=True)
            display_list(shopping_list)
        else:
            print("Invalid number. No item removed.", flush=True)
        return

    # Remove by name (case-insensitive)
    for item in shopping_list:
        if item.lower() == user_input.lower():
            shopping_list.remove(item)
            print(f"'{item}' has been removed.", flush=True)
            display_list(shopping_list)
            return

    print(f"'{user_input}' not found in the shopping list.", flush=True)


def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_item(shopping_list)

        elif choice == "2":
            remove_item(shopping_list)

        elif choice == "3":
            display_list(shopping_list)

        elif choice == "4":
            print("\nFinal Shopping List:", flush=True)
            display_list(shopping_list)
            print("Goodbye!", flush=True)
            break

        else:
            print("Invalid choice. Please try again.", flush=True)


if __name__ == "__main__":
    main()
