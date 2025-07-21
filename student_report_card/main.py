from operations import add_student, view_students, update_score

def main():
    while True:
        print("\n--- Student Report Card System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Score")
        print("4. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_score()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()