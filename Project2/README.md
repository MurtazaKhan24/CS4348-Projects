## How to run
First make sure you're in the right directory where the program is stored. Use either the "python proj2.py" or "python3 proj2.py" (depending on whats installed on your machine) command to run the program.

Make sure to have the latest python installed

## Features
Customers randomly choose between deposit and withdrawal
Only 2 tellers may access the safe simultaneously
Only 1 teller may talk to the manager at a time (required for withdrawals)
Only 2 customers may enter the bank at a time
Tellers serve customers, complete the transactions, and exit in increasing order (Teller 0, 1, 2)

### Tellers
Start by announcing they are ready
Wait for a customer
Ask the customer for a transaction
For withdrawals, visit the manager (5–30ms delay)
Enter the safe (max 2 tellers allowed) and perform transaction (10–50ms delay)
Notify the customer and wait for them to leave
Exit in order once all 50 customers are served

### Customers
Wait 0–100ms before arriving at the bank
Wait to enter if 2 other customers are inside
Randomly choose deposit or withdrawal
Approach a teller and provide transaction type
Leave the bank once the transaction is complete