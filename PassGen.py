import random
import string
import os
import subprocess
import sys

def account():    #gets the account name
    return (input("Enter site or game: "))

def username():    #gets the username
    return (input("Enter username: "))

def passlength():    #gets the length of the password to be generated
    return (int(input("Enter length of password: ")))

def getanswer():    #determines whether or not special characters are allowed
    if (input("Use special characters? (Y/N) ").upper()) == "Y":
        return True
    else:
        return False

def letgen(answer):    #generates base string
    basedict = {1 : string.ascii_uppercase, 2 : string.ascii_lowercase, 3 : string.digits, 4 : "!@#$%&"}

    if answer == True:
        return basedict[1] + basedict[2] + basedict[3] + basedict[4]
    else:
        return basedict[1] + basedict[2] + basedict[3]

def openfile(filename):
    if (input("Open password list? (Y/N) ").upper()) == "Y":
        try:
            os.startfile(filename)
        except AttributeError:
            subprocess.call('open', filename)
    else:
    	sys.exit

def main():
    filename = "PWList.txt"
    answer = getanswer()
    password = [random.choice(letgen(answer)) for i in range(passlength())]
    with open(filename, 'a') as out:
        out.write(account() + " " + username() + " " + ("".join(password)) + "\n")
    openfile(filename)

if __name__ == "__main__":
	main()
