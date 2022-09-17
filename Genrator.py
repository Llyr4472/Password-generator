import random
import os


def export(password):
    with open('Results.dat', 'a') as f:
        f.write(password)
        f.write('\n')
        f.close()

def dic(nums, sym, upc):
    num_d = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    sym_d = ['!', '@', '#', '$', '&', '*', '-', '_', '.']
    upc_d = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lwc_d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
    dictionary = lwc_d
    if nums == True:
        dictionary = dictionary + num_d
    if sym == True:
        dictionary = dictionary + sym_d
    if upc == True:
        dictionary = dictionary + upc_d
    return dictionary

def ask(question):
    while True:
        inp = input(f"{question}(y/n)\n")
        if str.capitalize(inp) =="Y": 
            return True
            break
        elif str.capitalize(inp) == 'N':
            return False
            break
        else:
            print("Invalid input")

def gen(dictionary):
    return random.choice(dictionary)

def main():
    # inputs
    length = int(input('Enter the length of password \n'))
    nums = ask('Conataining numbers?')
    sym = ask('Containing special characters?')
    upc = ask('Containing Uppercase letters?')
    
    # Dictionary
    dictionary = dic(nums, sym, upc)
    
    # Generation
    password = ''
    i = 0
    while length > i:
        password += gen(dictionary)
        i += 1
    
    # output
    print('\n \nYour password has been copied to clipboard.\n')
    print(f'Password: \n{password}')
    os.system(f'echo {password} |clip ')

    #export
    try:
        export(password)
    except:
        pass
    

if __name__ == '__main__':
    main()
    input()