'''
Program Name: Program12_1.py
Prgram Description: This program reads lines from the mbox-short.txt file and displays how many messages were sent on a specific date.
Programmer: Ray, Stephen
Date: 03/28/2022
Course: CSC233-1L1
'''

import socket

#Explain the program to the user
def explainProgram():
    print("This program receives a url address and prints information from the page if it is accessible.")

#The urlName() function receives input from the user and assigns this value to the userUrl variable
def urlName():

    userUrl = input("Enter the url you would like to access.")

    return userUrl

#The readUrl() function accepts the userUrl variable as an argument and reads the lines of the specified file
def readUrl(userUrl):

    #Create socket
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Use try/except clause to access the selected url
    try:
        #split the url entered by the user using the '/' character
        host = userUrl.split('/')[2]
        
        #Connect socket
        mysock.connect((host, 80))
        cmd = f'GET {userUrl} HTTP/1.0\r\n\r\n'.encode()
        mysock.send(cmd)

        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            print(data.decode(),end='')

        mysock.close()

    #Print error message for invalid url
    except:
        print("Invalid url entered.")
       
#The main function calls all relevant functions and assigns variables userUrl to their appropriate returned values
def main():
    explainProgram()

    userUrl = urlName()
    readUrl(userUrl)
    
#Call the main() function
main()