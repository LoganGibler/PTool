import random
import sys
import string
# MAKE MAN PAGE, LIKE LEGIT OPTIONS MAN ex: -gc -c -g
#  STRETCH:  maybe script asks if u want the generated password checked
#encode
#passcrack
numberlist = string.digits
specialcharslist = ["!","@","#","$","%","&"]
letterslist = string.ascii_letters
def generator():
    password = ""
    passwordlist = []

    numbers = random.choices(numberlist, k=random.randint(3,6))
    letters = random.choices(letterslist, k=random.randint(3,6))
    specialchar = random.choice(specialcharslist)

    scramble = []
    for num in numbers:
        scramble.append(num)
    for letter in letters:
        scramble.append(letter)

    scramble.append(specialchar)
    
    passwordlist += random.choices(scramble, k=random.randint(10,16))
   
    passwordlist.insert(random.randint(0,10), specialchar)

    random.shuffle(passwordlist)

    for character in passwordlist:
        password += character

    print("Your generated password: ", password)
    return password

special_characters = """!@#$%^&*()-+?_=,<>/"""
def passcheck(password):
    
    if len(password) < 8:
        print("Ensure password is at least 8 characters long")
    else:
        print("Password has sufficient length ") #more specific, ie 8-11 characters weak, 12-14 moderate, 15+ strong

    
    if any(char in special_characters for char in password):
        print("Password has special characters")
    else:
        print("Needs at least 1-2 special characters")

def compare():
    # String to search for in file.  This is a user input string.
    string1 = input("Enter password to search for: ")
    # opening a text file
    file1 = open("LeakedPasswords.txt", "r")
    # read file content
    readfile = file1.read()
    # checking condition for string found or not found and printing results.
    if string1 in readfile:
        print('You chose -->',string1 + ".", '\nThis password is compromised. Please choose again.')
    else:
        print('You chose -->', string1 , '\nThis password was not found')
    # closing file
    file1.close()

def main():
    passwd = ""
    option = sys.argv[1]
    # if option:
    #     print("Please give option")
    if option == "--g":
        generator()
    if option == "--c":
        passwd = sys.argv[2]
        print("Checked Password:  ", passwd)
        passcheck(passwd)
    if option == "--gc":
        passcheck(generator())
    if option == "--cp":
        compare()

    
        
main()