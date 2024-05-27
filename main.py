import os
def main() :
  directory = input("Enter the directory to list: ")
  command = f"ls {directory}"  # Vulnerable to Command Injection
  os.system(command)
if __name__ == '__main__':
    main()  
