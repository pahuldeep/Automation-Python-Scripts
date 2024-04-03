import os

def display_all(path):
    """
    This function shows all files within a given directory path.

    Args:
        path (str): The directory path to search for files.

    Returns:
        None
    """
    total = 0
    for dirpath, dirname, filename in os.walk(path):
        for i in filename:

            total+=1 
            print(i)
    print("\nTOTAL FILE PRESENT: ", total, "\n")


def display_all_not(path, *extensions):
  """
  This function shows files that do not have any of the specified extensions.

  Args:
      path (str): The directory path to search for files.
      *extensions: Variable number of strings representing the extensions to exclude (e.g., "txt", "py", "jpg").

  Returns:
      None
  """
  for dirpath, dirname, filename in os.walk(path):
    for i in filename:
      
      name = i.split(".")[-1].lower()  # Ensure case-insensitive comparison
      if not any(name == ext for ext in extensions):
        print(i)


def display_all_exact(path, input_name):
    """
    This function shows files that have the exact specified extension.

    Args:
        path (str): The directory path to search for files.
        input_name (str): The extension to search for (e.g., "txt").

    Returns:
        None
    """
    for dirpath, dirname, filename in os.walk(path):
        for i in filename:

            name = i.split(".")[-1]
            if(name == input_name): 
                print(os.path.join(dirpath, i))