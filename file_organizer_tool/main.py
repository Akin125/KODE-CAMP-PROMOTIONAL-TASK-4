import os
from organizer import organize_directory
from file_types import EXTENSIONS

def display_menu():
    print("\n=== File Organizer Tool ===")
    print("1. Organize a directory")
    print("2. View supported file types")
    print("3. Exit")
    return input("Choose an option (1-3): ")

def main():
    while True:
        choice = display_menu()

        if choice == "1":
            directory = input("Enter directory path to organize: ").strip()
            if os.path.exists(directory):
                organize_directory(directory)
                print(f"\nSuccessfully organized files in: {directory}")
            else:
                print("Error: Directory not found!")

        elif choice == "2":
            print("\nSupported file categories:")
            for category, extensions in EXTENSIONS.items():
                print(f"\n{category.capitalize()}:")
                print(", ".join(extensions))

        elif choice == "3":
            print("Thank you for using File Organizer!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
