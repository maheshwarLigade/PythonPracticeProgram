import os


def rename_files():
  # get the folder path lsit of files
  file_list = os.listdir(os.path.expanduser(r"/Users/maheshwarligade/Documents/PythonPractice/prank"))
  print(file_list)
  # get the current working directory path
  saved_path = os.getcwd()
  print("Current working directory path = "+ saved_path)
  # for each file & rename it
  for file_name in file_list:
      os.rename(file_name, file_name.translate(None, "0123456789"))
      os.chdir(r"/Users/maheshwarligade/Documents/PythonPractice/prank")


rename_files()
