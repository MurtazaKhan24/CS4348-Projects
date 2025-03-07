# CS 4348 Project devlogs

## Project 1 devlog

### Feb. 13 6:00pm
I'm starting the project by adding the necessary files made in python. I started to work on the driver program to add a user input feature and error handling for cases if there isn't any passkey or non alpha characters.

### Feb. 25 5:11pm
Worked on implementing the vigenere encryption and decryption algorithm as well as using the subprocess module to get user input from driver program via subprocess. Going to test if subprocess is going to work.
### Feb. 25 7:00pm 
Attempting to write the logger program file using the same subprocess technique between encyrption and driver.
### Feb. 25 8:00pm
Running to a problem with running the driver program, "response = send_command(f"PASS {password}")" is not working as intended. I'm going to try to fix this issue.

### March 7th 2:00pm
Resumed work after break.
Going to start working on implementing the logging program to work alongside the driver program, running.

### March 7th 4:00pm
Got logging to somewhat work as intended, it will start the logging message once the program is called and write a exit status once the user enters "quit". However, I cannot seem to allow other actions (i.e. pass, encrypt, decrypt, etc.) to work

