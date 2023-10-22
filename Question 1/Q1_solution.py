import numpy as np
import pandas as pd
import sys
import re

def password_checker(password):
    password = str(password)
    
    feedback = []
    
    ## To check the lenght of password
    if len(password) <8:
        feedback.append("Warning! Password is less than 8 characters. Please provide a longer password.")
    else:
        feedback.append("Great! Password has sufficient length!")
    
    ## To check presence of upper and lower case combination in password
    ## Loop through the list to check each characters for upper and lower case combination through 
    ## one single if statement with both conditions together.
    
    interim = 0
    for i in password:
        if not (i.isupper() & i.islower()):
            interim += 1
    if interim > 1:
        feedback.append("Great! Password has an upper and lower case combination!")
    else:
        feedback.append("Warning! Please use combination of upper and lower case.")
    
    ## To check presence of digits in password.
    ## Use regular expressions to test for presence of digits
    if re.fullmatch(r"\d+", password):
        feedback.append("Warning! Please provide atleast one digit.")
    else:
        feedback.append("Great! Password has atleast one digit!")
        
    
    ## To check presence of one special character
    ## Use regular expresssions to test this condition by declaring the list of special characters and searching 
    ## for the same in the password
    se = re.compile('[@_!-+#$%^&*()<>?/\|}{~:]')
   
    if(se.search(password) != None):
        feedback.append("Great! Password has atleast one special character.")
    else:
        feedback.append("Warning! Please provide atleast one special character")
        
    for i in feedback:
        print(i,sep=',',end='\n')

if __name__=='__main__':
    input = sys.argv[0]
    password_checker(input)
    
