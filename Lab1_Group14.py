# Group Name: Nezar Mazraie, Spencer DaSilva
# Course: INFT-1207-03
# Date: 1/21/2025
# Description: A code that takes user input and makes a password based on it

# Imported Libraries
import random
import string

# Asks the user to input their desired length of the password
def user_validation():
    whileloopcondition = 0
    while whileloopcondition < 1:
        try:
                # Asks the user how the length of the password they desire and stores it
                passwordlength = int(input("How long do you want the password to be (8-20 characters)?: "))

                if passwordlength >= 8 and passwordlength <= 20 and passwordlength.is_integer():
                    whileloopcondition = 1
                    return passwordlength
                else:
                    print("Password must be between 8 and 20 characters.")

        except:
            print("Password must be between a whole number integer:")

# Asking the user how many of each character type
def password_details(length):
    whilecondition = 0
    while whilecondition < 1:
        totallength = length
        try:
            num_letters = int(input("How many letters do you want the password to have?: "))
            if 0 <= num_letters <= totallength:
                totallength -= num_letters
                num_digits = int(input("How many digits do you want the password to have?: "))
                if 0 <= num_digits <= totallength:
                    totallength -= num_digits
                    num_special = int(input("How many special characters do you want the password to have?: "))
                    if num_special == totallength:
                        return num_letters, num_digits, num_special
                    else:
                        print(f"Your password length is {length}.\nEnsure that your parameters are less than {length}.")
                else:
                    print(f"Your password length is {length}.\nEnsure that your parameters are less than {length}.")
            else:
                print(f"Your password length is {length}.\nEnsure that your parameters are less than {length}.")

        except ValueError:
            print(f"Your password length is {passwordlength}.\nEnsure that your parameters are less than {passwordlength}.")


# Generates the Password based on the parameters set by the user
def password_generator(num_letters, num_digits, num_special):
    pass_list = []
    for i in range(num_letters):
        pass_list.append(random.choice(string.ascii_letters))
    for i in range(num_digits):
        pass_list.append(random.choice(string.digits))
    for i in range(num_special):
        pass_list.append(random.choice(string.punctuation))
    random.shuffle(pass_list)
    password = ''.join(pass_list)
    return password

# Entry point of the code
if __name__ == '__main__':

    # Calls the functions with the required variables to be able to calculate and store everything required
    passwordlength = user_validation()
    num_letters, num_digits, num_special = password_details(passwordlength)
    Password = password_generator(num_letters, num_digits, num_special)
    # The user output
    print("This is your password:", Password)
    # Outputs the user's parameters
    print ("Password successfully generated with!", "\n - Letters:", num_letters, "\n - Digits:", num_digits, "\n - Special Characters:", num_special)