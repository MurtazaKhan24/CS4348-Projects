### How to run/ what is displayed
    Make sure you're in the "Project 1" folder in the terminal
    Use the command "python3 driver.py logfile.txt" to start the program

    If for some reason "universal_newlines=True" displays an error, change the parameter to "text=True"
    
    The terminal will prompt the user for a list of commands, the user has to type the command first
    make sure to ONLY type the command first (i.e. password, encrypt, decrypt) and not with the word as well. 
    (i.e. "password hello" or "encrypt world").
    Afterwards, the program will prompt the user for the word to set as the password, encrypt, or decrypt.
    The program will then run the specified command and output the result.
### What each file does
    The driver.py file is the main program that interacts with the user and uses subprocesses to sends user commands to the encryption program
    (i.e. password, encrypt, decrypt, history)
    The encrytion.py file has the vigenere cypher logic within it and communicates with the driver to run the encryption and decryption
    Finally, the logger.py file has the logic to record the users actions and program to a specified log file
