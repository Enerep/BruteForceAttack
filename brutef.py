import random
import pyautogui
import time
import string

#All characters
chars = string.printable
charlist = list(chars)

# 2 passwords variables
password = pyautogui.password("Enter a your password: ")
brute_password = ""

#starting timer
start_time = time.time()

#starting execution
while(password != brute_password):
    brute_password = random.choices(charlist, k=len(password))
    #seeing the characters:
    print("<--" + str(brute_password) + "-->")
    
    if(brute_password == list(password)):
        print("Your password is: " + "".join(brute_password))
        break
        
total_time = (time.time() - start_time)
print("Total execution time: " + str(total_time))

