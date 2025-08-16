HISTORY_FILE = "history.txt"

def main():
    print("---- Welcome to the Calculator made by Kashish ----")
    while True:
        user_input = input("Enter opration what you want to do \n 1 - Eqestion \n 2 - History \n 3 - Clear \n 4 - Exit ").strip().lower()
    
        if user_input == '2' or user_input == 'history':
            show_history()
        elif user_input == '3' or  user_input == 'clear':
            clear_history()
        elif user_input == '4' or  user_input == 'Exit':
            print("Exiting the program!!")
            exit()
        elif user_input == '1' or user_input =='eqestion':
            eqestion()
        else:
            print("Something wrong")
            exit()


def eqestion():
    opration = input("Enter your Equestion = ").strip()
    parts = opration.split()

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])
    if len(parts)!=3:
        print("Invalid Input Please try again")
    else:
        if op=='+':
            result = num1+num2
        elif op=='-':
            result = num1-num2
        elif op=='*':
            result = num1*num2   
        elif op=='/' and num2>num1:
            result = num1/num2
        else:
            print("Something wants wrong SORRY")

        with open(HISTORY_FILE, 'a') as file:
            file.write(f"{opration} = {result}\n")
def show_history():
    with open (HISTORY_FILE,'r') as file:
        lines = file.readlines()
        if lines==0:
            print("lines not found")
        else:
            for line in reversed(lines):
                    print(line.strip())
def clear_history():
    open(HISTORY_FILE, 'w').close()
    print("History cleared.")


main()



    