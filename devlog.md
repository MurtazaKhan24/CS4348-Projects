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

    The driver program now sends commands to the encryption program using subprocess communication.
    Commands and responses are done through the use of (stdin/stdout).
    While I'm testing it however, I run across an issue with losing the data
    and the program freezing sometimes.
I'll try to find out the issue by debugging the code using print statements for next time.

### Feb 23rd 6:30 pm
Was able to fix the issue with subprocess communication
I found out that the subprocess buffer wasn't flushing properly
Added "sys.stdout.flush() to make it work properly"

Also coded some other checks and tested it to see if it worked properly such as:
    "PASSKEY" being set before encryption/decryption.
    Making sure the encrypt and decrypt work using the passkey
Final testing allowed me to confirm the vigenere cypher was working

### Feb 23rd 8:30pm
Added the history and quit functionality to the program 

I'll start working on the logging feature for next time.

### Feb. 25 5:11pm
Started implementing logging functionality.

Searched out how to use the datetime module in python
Currently, the logger is only displaying the SESSION STARTED cmmand and QUIT but not anything else.

Will find out whats the issue

### Feb. 25 7:00pm 
Began fixing the logging program

    I added print statements and saw that the logger wasn't properly recieving messages from the driver
    I changed Popen() to stdout = subprocess.PIPE and stderr=subprocess.PIPE to capture the output.
    Started working as intended

Next I'll try and fix the current structure of the logger to make it the same as in the project description.

### March 2nd 3:00pm
Added struture to the logger program to display log messages similar to the example in the project 1 requirements

### March 7th 2:00pm
Finalizing logging system, make sure every command is properly displayed on the logger program 

### March 7th 4:00pm
Spent time testing out various inputs for the program such as:
    PASSKEY 123 to see if the error check will occur
    Encrypt Hello before setting password.
All tests seem to work and function as intended
Will try to test the code in the linux environment (cs1 utd) to make sure everything works there too

### March 24th 2:00pm 
Ran into an error with the linux server not running the program:
    Due to outdated python version, the program couldn't recognize the prameter "text = True" for the processes.
    Used "universal_newline=True" instead and it started working
Finalizing the project by adding README file and tweaking devlog before submitting.

