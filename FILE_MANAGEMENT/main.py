import os

from file_manager import show
from file_manager import remove
from file_manager import rename


def main():
    print("\n\tFILE MANAGEMENT\n")

    print("Show ALL files in the directory: 1")
    print("Show files NOT having specific extensions: 2")
    print("Show files with an EXACT extension: 3\n")
    
    print("Remove files with an EXACT extension: 4")
    print("\nRename files with a SPECIFIC extension: 5")

    work = input("\nEnter the operation number: ")
    extension = input("\nEnter the extension (without the dot, e.g., txt): ")

    # Iterate through directories in the current path
    for dirpath in os.listdir():
        # Check if it's actually a directory (avoid hidden files etc.)
        if os.path.isdir(os.path.join(os.getcwd(), dirpath)):
            full_path = os.path.join(os.getcwd(), dirpath)  # Construct full path
            match work:

                case "1":
                    show.display_all(full_path)
                case "2":
                    show.display_all_not(full_path, extension)
                case "3":
                    show.display_all_exact(full_path, extension)
                case "4":
                    remove.remove_exact(full_path, extension)
                case "5":
                    new_name = input("Enter the new name (without the dot): ")
                    rename.rename_all(full_path, extension, new_name)  # Use correct arguments
                case _:
                    print("Invalid option.")

if __name__ == "__main__":
    main()
