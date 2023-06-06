sorted_numbers=[]
def NumberSorter():
    usr_input1 = input("==========Number Sorter==========\nHow to use:\n \t- When you add numbers, they get added to a list to be then be put in order.\nType 'n' to start adding numbers to the list: ")
    if usr_input1 == 'n':
        maxlength = int(input("Enter how many numbers will be added to the list: "))
        for i in range(0,maxlength):
            usr_input2 = int(input("Enter numbers here: "))
            sorted_numbers.append(usr_input2)
        return sorted_numbers.sort()
    else:
        print("Error, next was not typed")
        exit()

NumberSorter()
print(f"Here is your sorted list of numbers: {sorted_numbers}")
   

