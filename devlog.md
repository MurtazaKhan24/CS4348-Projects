# CS 4348 Project devlogs

## Project 1 devlog

### Feb. 13 6:00pm
Started the project by setting up the necessary Python files. Focused on designing the driver program, which will include
    Handling user input and error handling such as attempting to encrypt/decrypt without a passkey

Got little done so far, plan to implement the commands and user interaction on the driver file, and Vigenère cipher encryption and decryption next.

### Feb. 15 3:30 pm
Worked on implementing basic commands through the driver program such as 
        "Passkey"
        "Encrypt"
        "Decrypt"

Also, I hard coded it so if the user enters the wrong command or enters encrypt before password, the program will output the appropriate error
Right now though, the commands aren't being sent over to the logger or encrypt files so its very basic. I will work implementing the vigenere cypher for encryption next.

### Feb 18th 5:45pm
Started working on the Vigenère encryption and decryption algorithm.
    Hard coded some test encryptions using a key which helped me see if the algorithm was working as intended. 
    Decryption was running into some problems since it outputted an empty output. 
    It was a little hard to understand how to move the characters based on the password as well as looping the passkey back to the start if the encryption is still on going, but some research on the algorithm helped me.

I will try to work on adding the error inputs when the user enters a non alphanumeric character or password.

### Feb 20th 7:00pm
Hard coded some input validation to encryption and decryption.

    Now, if a user enters an invalid input (e.g., "ENCRYPT Hello World!"), the program displays an error message instead of attempting encryption.

So now the error messages displayed will be if:
The encryption/decryption command is run before the password is set
If the user enters a non-alpha num character for either password or encrypt/decrypt.

Next, I will start to work on adding the subprocess module to allow the driver and encrypt files to communicate with one another.

## Feb. 22nd 2:00 pm
Began working on subprocess communication.
    Was a bit tricky to understand, but through research, I was able to implement a very basic version of the module to communicate with the encrypt.py file using popen commands.

    The driver program now sends commands to the encryption program using subprocess.
    Commands and responses are exchanged through standard input/output (stdin/stdout).
    Issue of responses not returning correctly is happening
Plan: debug code and subprocess to make sure it's being used correctly

### Feb 23rd 6:30 pm
Refined the subprocess execution flow:
Ensured commands are properly sent and received between programs.
Fixed an issue where the subprocess would hang indefinitely due to improper input buffering.

Ran additional test cases to verify:

    "PASSKEY" must be set before encryption/decryption.
    Encryption and decryption now correctly modify text based on the passkey.

Plan: Start working on the logging feature.

### Feb. 25 5:11pm
Started implementing logging functionality.

    Plan: The logger will record all user actions and program status updates.
    Integrated subprocess communication between the driver program and the logging program.

Next step: Ensure logs are correctly written when commands are executed.

### Feb. 25 7:00pm 
Began writing the logger program.

    The logger will:
    Start when the program is launched.
    Record user actions (PASSKEY, ENCRYPT, DECRYPT).
    Log the exit status when "QUIT" is entered.

However, not all commands are being recorded. Investigating why subprocess messages are not reaching the logger consistently.

### Feb. 25 8:00pm
Encountered an issue with the command execution flow:

    "response = send_command(f'PASS {password}')" is not working as intended.
    Debugging revealed that the subprocess pipe closes prematurely, causing loss of data.

Plan:

    Refactor the way commands are sent and responses are handled.
    Ensure all processes run smoothly without blocking execution.

### March 2nd 3:00pm
Added struture to the logger program to display log messages similar to the example in the project 1 requirements

### March 7th 2:00pm
Finalizing logging system, make sure every command is properly displayed on the logger program 

### March 7th 4:00pm
Got logging to somewhat work as intended, it will start the logging message once the program is called and write a exit status once the user enters "quit". However, I cannot seem to allow other actions (i.e. pass, encrypt, decrypt, etc.) to work

### March 8th 2:00pm 
Added flushing to ensure the logs are written immediately after commands are executed, finished development

