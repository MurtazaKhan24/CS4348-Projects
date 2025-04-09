import threading
import random
import time


queueLock = threading.Semaphore(1)
customerReady = threading.Semaphore(0)
NUM_TELLERS = 2
NUM_CUSTOMERS = 3

customerQueue = []
tellerAssignments = {}
transactions = ["Deposit", "Withdrawal"]
customerTransaction = {}


ready = [threading.Semaphore(0) for _ in range(NUM_CUSTOMERS)]
transactionSent = [threading.Semaphore(0) for _ in range(NUM_CUSTOMERS)]

def tellerCode(tellerId):
    print("Teller", tellerId, "[]: ready to serve")
    for _ in range(NUM_CUSTOMERS // NUM_TELLERS + 1):
        customerReady.acquire()
        queueLock.acquire()
        if len(customerQueue) == 0:
            queueLock.release()
            break
        customerId = customerQueue.pop(0)
        tellerAssignments[customerId] = tellerId
        queueLock.release()

        print("Teller", tellerId, "[Customer", customerId, "]: asks for transaction")
        ready[customerId].release()
        transactionSent[customerId].acquire()
        trans = customerTransaction[customerId]
        print("Teller", tellerId, "[Customer", customerId, "]: received", trans.lower(), "transaction")

def customerCode(customerId):
    time.sleep(random.uniform(0, 0.05))
    transType = random.choice(transactions)
    customerTransaction[customerId] = transType

    queueLock.acquire()
    customerQueue.append(customerId)
    queueLock.release()
    print("Customer", customerId, "[]: wants to perform a", transType.lower(), "transaction")
    print("Customer", customerId, "[]: getting in line")

    customerReady.release()
    ready[customerId].acquire()
    tellerId = tellerAssignments[customerId]
    print("Customer", customerId, "[Teller", tellerId, "]: gives", transType.lower(), "transaction")
    transactionSent[customerId].release()

tellers = []
for i in range(NUM_TELLERS):
    tellers.append(threading.Thread(target=tellerCode, args=(i,)))
    tellers[i].start()

customers = []
for i in range(NUM_CUSTOMERS):
    customers.append(threading.Thread(target=customerCode, args=(i,)))
    customers[i].start()

# Wait for all threads
for c in customers:
    c.join()
for t in tellers:
    t.join()

