# cs361_microservice
Microservice for partner's program

Instructions for how to programmatically request data from this microservice:
1. First, be sure to change the name of FILE_NAME in the microservice to ensure the request is being written to the correct file. By default, the name of the file is state.txt.
2. Run the microservice
3. Write the name of a US state to state.txt
4. The name of the state must be a valid name of a state. The first letter of each word of the state must be capitalized.
5. The microservice will read the .txt file every 3 seconds, and write the name of any and all NFL teams that reside in that state.

Instructions for how to programmatically receive data from this microservice:
1. As test_microservice.py illustrates, it is possible to read state.txt by using the following script:
```
with open(FILE_NAME, 'r') as file:
    response = file.readlines()
    if response[0] == state_name:
        print("Please enter a valid name of a state (Capitalize first letter, i.e. 'California' or 'New Hampshire')")
        exit()
    else:
        for item in response:
            print(item.strip())
```
2. After reading the file, the program is able to print all NFL teams in the state that was written in the file previously.
3. If the file contains the same code that was written into the file beforehand, then that means the issue was caused by the request rather than the response.

# UML Diagram
[UML_Diagram_microservice.pdf](https://github.com/juliantpeterson/cs361_microservice/files/14413713/UML_Diagram_microservice.pdf)
