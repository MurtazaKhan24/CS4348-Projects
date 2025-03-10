# CS 4348 Project devlogs

## Project 1 devlog

### Feb. 13 6:00pm
I'm starting the project by adding the necessary files made in python. I started to work on the encryption algorithm and researching out to use the subprocess module in python.

### Feb. 25 5:11pm
Finished successfully implementing the vigenere cipher in the encryption program, ran some test cases to make sure it works. Starting to work on the creating processes for cross file communication.

### Feb. 25 7:00pm 
Added the basic user inputs the driver program will display once the user runs the program, now need to use processes to send user input to encyrption program.

### Feb. 25 8:00pm
Added subprocess to run the encryption program at the start of the driver program. Running to a problem with send input from the driver program to encryption program, "response = send_command(f"PASS {password}")" is not working as intended. I'm going to try to fix this issue.

### Feb. 26 1:00pm
Send command function wasn't running as intended, researched more about the subprocess module command and realized I can use the write and flush commands instead to send user input and clear it afterwards.

### March 7th 2:00pm
Resumed work after break.
Going to start working on implementing the logging program to work alongside the driver program, running.

### March 7th 4:00pm
Got logging to somewhat work as intended, it will start the logging message once the program is called and write a exit status once the user enters "quit". However, I cannot seem to allow other actions (i.e. pass, encrypt, decrypt, etc.) to work

### March 9th 2:00pm
Got logging to work as intended, finished bulk of the project, just going to refine a few things before submitting.
