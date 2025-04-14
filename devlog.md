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


## Project 2

### April 7th 9:10pm
Setting up initial project with simple threading to see if the basics are working.

Managed to set up a simple thread with 2 tellers and 3 customers from the example files provided. The customers introduce themselves and tellers recognize customers introduction.

created customers and tellers using threading.thread call, and variables such as teller assignments to track which teller is serving which customer

included some semaphores or syncing

Will try to add simple transactions next time.

### April 8th 9:00pm 
Starting to work on providing the customer transactions such as withdrawal or deposit 

using the random module to decide whether the customer will do a deposit or withdrawal
implemented transactionSent semaphore to pass trans info from customer to teller

Still using 2 tellers and three customers to make sure the threading logic will work as intended

Will try to add manager permissions for withdrawals, safe access to safe, and random waiting times

### April 9th 12:00pm
Added manager access for withdraw requests from customers as well as randomized wait times (5-30 ms when talking to manager, 10-50ms when accessing safe, and 0-100ms for customer wait times using time.sleep()), and safe access to vaults by limiting tellers to 2 at the safe at one time

added manager logic by creating a manager semaphore where only 1 teller can talk to a manager at a time
added a safe semaphore where only two tellers can access the safe at a time

Ran into some problems with increasing the numbers of customers, so will see the issue next time

Once the issue is found, I'll gradually increase the number of customers to 50
Also need to add the logic for limiting customers entry via the front door to 2 at a time.

### April 10th 9:00pm
Expanded the program to handle 10 customers, ran into some issues regarding the tellers reaching all of them but was able to figure it out

Implementing logic where only 2 customers enter the bank at a time
Adding a door semaphore of 2. Is taken when a customers enters, is freed when a customer leaves.
Ran some tests to see if it works and works as intended

Going to add check to see if all customers served, first add a customers served thread lock and increment once a teller is done with a customer.

Boolean variable for checking if the total number of customers served is >= to total customers
Ran some tests and works as intended

### April 11th 4:00pm
Increased the customer size to 50 but program was hanging at the end preventing quitting 

Trying to add a event to tell tellers to exit after all customers and exit the program

Still didn't work I'll try debug and find out the issue

### April 11th 6:00pm
debugged, found out the issue is that tellers were waiting for customers even after the 50th one was served

used a shared exit signal event which is set to true once all 50 customers are served

check to see if exit signal is set then break from the program and print "bank is closed for the day"

tellers are exiting from random which is different from example run, will try to fix that next time

### April 11th 6:21pm
testing out different for tellers to leave in order

found you can use a threading condition to have a turn taking exit in increasing order

once one teller is done, they notify the next teller to leave

going to compare my run with the sample run to see if its similar, add a readme and finalize the project

### April 13th 8:30pm
Finalized the project and added readme for submission