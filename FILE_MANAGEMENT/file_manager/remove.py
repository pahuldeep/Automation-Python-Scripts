import os

def remove_exact(path, extension_name):
  """
  This function removes files with the specified extension from a directory and its subdirectories.

  Args:
      path (str): The directory path containing the files.
      extension_name (str): The extension of the files to be removed (e.g., "txt").

  Returns:
      None
  """
  for dirpath, dirname, filename in os.walk(path):
    for i in filename:
      name = i.split(".")[-1]
      if name == extension_name:
        remove_name = os.path.join(dirpath, i)
        confirm = input(f"Are you sure you want to remove '{remove_name}'? (y/n): ")
        if confirm.lower() == 'y':
          try:
            os.remove(remove_name)
            print(f"Removed '{remove_name}'.")
          except OSError as e:
            print(f"Error removing!!! '{remove_name}': {e}")
        else:
          print("Removal canceled.")