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
            shopping_list.append(item)
        elif choice == '2':
            index = int(input("Index to remove: "))
            del shopping_list[index + 1]
        elif choice == '3':
            print("#"*30)
            for id, item in enumerate(shopping_list):
                print(f"==> {id + 1}: {item}")
            print("#"*30)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()