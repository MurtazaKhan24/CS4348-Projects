import threading
import random
import time

NUM_TELLERS = 3
NUM_CUSTOMERS = 50

queueLock = threading.Semaphore(1)
customerReady = threading.Semaphore(0)
manager = threading.Semaphore(1)
safe = threading.Semaphore(2)
door = threading.Semaphore(2)

customerQueue = []
tellerAssignments = {}
transactions = ["Deposit", "Withdrawal"]
customerTransaction = {}
ready = [threading.Semaphore(0) for _ in range(NUM_CUSTOMERS)]
transactionSent = [threading.Semaphore(0) for _ in range(NUM_CUSTOMERS)]
left = [threading.Semaphore(0) for _ in range(NUM_CUSTOMERS)]

customersServed = 0
customersServedLock = threading.Lock()
all_customers_done = threading.Event()

def tellerCode(tellerId):
    print("Teller", tellerId, "[]: ready to serve")
    while True:
        if all_customers_done.is_set():
            break

        customerReady.acquire()

        if all_customers_done.is_set():
            break

        queueLock.acquire()
        if len(customerQueue) == 0:
            queueLock.release()
            continue
        customerId = customerQueue.pop(0)
        tellerAssignments[customerId] = tellerId
        queueLock.release()

        print("Teller", tellerId, f"[Customer {customerId}]: asks for transaction")
        ready[customerId].release()
        transactionSent[customerId].acquire()
        trans = customerTransaction[customerId]

        if trans == "Withdrawal":
            print("Teller", tellerId, f"[Customer {customerId}]: going to the manager")
            manager.acquire()
            print("Teller", tellerId, f"[Customer {customerId}]: getting manager's permission")
            time.sleep(random.uniform(0.005, 0.03))
            print("Teller", tellerId, f"[Customer {customerId}]: got manager's permission")
            manager.release()

        print("Teller", tellerId, f"[Customer {customerId}]: going to safe")
        safe.acquire()
        print("Teller", tellerId, f"[Customer {customerId}]: enter safe")
        time.sleep(random.uniform(0.01, 0.05))
        print("Teller", tellerId, f"[Customer {customerId}]: leaving safe")
        safe.release()

        print("Teller", tellerId, f"[Customer {customerId}]: finishes {trans.lower()} transaction")
        print("Teller", tellerId, f"[Customer {customerId}]: wait for customer to leave")
        left[customerId].acquire()

        global customersServed
        customersServedLock.acquire()
        customersServed += 1
        if customersServed >= NUM_CUSTOMERS:
            all_customers_done.set()
        customersServedLock.release()

    print(f"Teller {tellerId} []: leaving for the day")

def customerCode(customerId):
    time.sleep(random.uniform(0, 0.1))
    transType = random.choice(transactions)
    customerTransaction[customerId] = transType

    print("Customer", customerId, "[]: wants to perform a", transType.lower(), "transaction")
    print("Customer", customerId, "[]: waiting to enter bank")
    door.acquire()
    print("Customer", customerId, "[]: entering bank")

    queueLock.acquire()
    customerQueue.append(customerId)
    queueLock.release()
    print("Customer", customerId, "[]: getting in line")

    customerReady.release()
    ready[customerId].acquire()
    tellerId = tellerAssignments[customerId]
    print("Customer", customerId, f"[Teller {tellerId}]: gives {transType.lower()} transaction")
    transactionSent[customerId].release()

    print("Customer", customerId, f"[Teller {tellerId}]: leaves teller")
    left[customerId].release()
    print("Customer", customerId, "[]: leaves the bank")
    door.release()

tellers = [threading.Thread(target=tellerCode, args=(i,)) for i in range(NUM_TELLERS)]
customers = [threading.Thread(target=customerCode, args=(i,)) for i in range(NUM_CUSTOMERS)]

for t in tellers:
    t.start()
for c in customers:
    c.start()

for c in customers:
    c.join()

for _ in range(NUM_TELLERS * 2):
    customerReady.release()

for t in tellers:
    t.join()

print("The bank closes for the day.")