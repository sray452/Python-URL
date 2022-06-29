'''
Program Name: Program12_3.py
Prgram Description: This program reads lines from the mbox-short.txt file and displays how many messages were sent on a specific date.
Programmer: Ray, Stephen
Date: 03/28/2022
Course: CSC233-1L1
'''

import re
import urllib.request

#Explain the program to the user
def explainProgram():
    print("This program receives a url address and prints information from the page if it is accessible.")

#The urlName() function receives input from the user and assigns this value to the userUrl variable
def urlName():

    userUrl = input("Enter the url you would like to access.")

    return userUrl


#The readUrl() function accepts the userUrl variable as an argument and reads the lines of the specified file
def readUrl(userUrl):

    try :
        
        #Open the url and read the first 3000 characters
        websiteUrl = urllib.request.urlopen(userUrl)        
        content = websiteUrl.read(3000)

        #Print the first 3000 characters of the url
        print("The first 3000 characters of the url:\n",content)

        #Read the url in its entirety and convert it to string data to count the characters
        content = websiteUrl.read()
        content = str(content)
        #Use regular expression to count the characters and not spaces, print the result
        numChars = re.sub(r"\s+","", content)
        #since all the whitespaces removed, so here iam printing the number characters by len of the s.
        print("\nThe number of characters in the url is:" , len(numChars))
    except:
        print("Invalid url entered.")    

            
       
#The main function calls all relevant functions and assigns variables userUrl to their appropriate returned values
def main():
    explainProgram()

    userUrl = urlName()
    readUrl(userUrl)
    
    
#Call the main() function
main()