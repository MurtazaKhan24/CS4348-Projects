import threading
import random
import time


queueLock = threading.Semaphore(1)
customerReady = threading.Semaphore(0)
manager = threading.Semaphore(1)
safe = threading.Semaphore(2)

NUM_TELLERS = 2
NUM_CUSTOMERS = 3

customerQueue = []
tellerAssignments = {}
transactions = ["Deposit", "Withdrawal"]
customerTransaction = {}


ready = [threading.Semaphore(0) for _ in range(NUM_CUSTOMERS)]
transactionSent = [threading.Semaphore(0) for _ in range(NUM_CUSTOMERS)]
left = [threading.Semaphore(0) for _ in range(NUM_CUSTOMERS)]

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

        if trans == "Withdrawal":
            print("Teller", tellerId, "[Customer", customerId, "]: going to the manager")
            manager.acquire()
            print("Teller", tellerId, "[Customer", customerId, "]: getting manager's permission")
            time.sleep(random.uniform(0.005, 0.03))
            print("Teller", tellerId, "[Customer", customerId, "]: got manager's permission")
            manager.release()

        print("Teller", tellerId, "[Customer", customerId, "]: going to safe")
        safe.acquire()
        print("Teller", tellerId, "[Customer", customerId, "]: enter safe")
        time.sleep(random.uniform(0.01, 0.05))
        print("Teller", tellerId, "[Customer", customerId, "]: leaving safe")
        safe.release()

        print("Teller", tellerId, "[Customer", customerId, "]: finishes", trans.lower(), "transaction")
        print("Teller", tellerId, "[Customer", customerId, "]: wait for customer to leave")
        left[customerId].acquire()

def customerCode(customerId):
    time.sleep(random.uniform(0, 0.1))
    transType = random.choice(["Deposit", "Withdrawal"])
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

    print("Customer", customerId, "[Teller", tellerId, "]: leaves teller")
    left[customerId].release()
    print("Customer", customerId, "[]: leaves the bank")

tellers = []
for i in range(NUM_TELLERS):
    tellers.append(threading.Thread(target=tellerCode, args=(i,)))
    tellers[i].start()

customers = []
for i in range(NUM_CUSTOMERS):
    customers.append(threading.Thread(target=customerCode, args=(i,)))
    customers[i].start()

for c in customers:
    c.join()
for t in tellers:
    t.join()

