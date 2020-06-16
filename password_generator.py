import random
import string

#sets the empty strings and lists
password = []
final    = ''

#asks the user how long they want their password to be and keeps asking until they input an integer
chars = input('How many characters would you like your password to be?\n')
while chars.isnumeric()==False:
    chars = input('How many characters would you like your password to be?\n')

#list of special characters
specials = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')')

        
'''
1 = lower letter
2 = upper letter
3 = number
4 = special character
'''

#loops once for each character in the password
for i in range(int(chars)):

    #picks a random number between 1 and 4 to chose what time of character to add
    character = random.randint(1,4)

    #for each randomly selected number, it randomly choses one from that category and adds sets the variable to it
    if character == 1:
        add = random.choice(string.ascii_lowercase)

    if character == 2:
        add = random.choice(string.ascii_uppercase)

    if character == 3:
        add = random.randint(0,9)

    if character == 4:
        add = random.choice(specials)

    #adds the contents of the variable to the list
    password.append(add)

#loops over the list and adds each item to the string
for i in password:
    final += str(i)

print ("Randomly generated passord:", final)

