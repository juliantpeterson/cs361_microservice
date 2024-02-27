# Test script for microservice
# Created by: Julian Peterson
# Purpose: test the microservice that is intended to deliver value to Russel Hueso's project.

import time

FILE_NAME = 'state.txt'

state_name = input("Enter the name of a state: ")
with open(FILE_NAME, 'w') as file:
    file.write(state_name)


time.sleep(4)
print()
print("The NFL team(s) in that state is/are:")
with open(FILE_NAME, 'r') as file:
    response = file.readlines()
    if response[0] == state_name:
        print("Please enter a valid name of a state (Capitalize first letter, i.e. 'California' or 'New Hampshire')")
        exit()
    else:
        for item in response:
            print(item.strip())
