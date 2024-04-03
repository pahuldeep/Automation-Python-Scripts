import os

def rename_all(path, old_name, new_name):
  """
  This function renames files within a directory and its subdirectories 
  by replacing a specified string with another string in the filenames.

  Args:
      path (str): The directory path containing the files.
      old_name (str): The string to be replaced in the filenames.
      new_name (str): The string to replace the old string with.

  Returns:
      None
  """
  for dirpath, dirname, filename in os.walk(path):
    for i in filename:
      if old_name in i:  # Check if old_name is present before processing

        old_path = os.path.join(dirpath, i)
        new_path = os.path.join(dirpath, i.replace(old_name, new_name))

        confirm = input(f"Rename '{old_path}' to\n '{new_path}'? (y/n): ")
        
        if confirm.lower() == 'y':
          try:
            os.rename(old_path, new_path)
            print(f"Renamed '{old_path}' to '{new_path}'.")
          except OSError as e:
            print(f"Error renaming '{old_path}': {e}")
        else:
          print("Renaming canceled.")
