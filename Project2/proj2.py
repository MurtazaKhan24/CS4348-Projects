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
customerTransaction = {}
transactions = ["Deposit", "Withdrawal"]
ready = [threading.Semaphore(0) for _ in range(NUM_CUSTOMERS)]
transactionSent = [threading.Semaphore(0) for _ in range(NUM_CUSTOMERS)]
left = [threading.Semaphore(0) for _ in range(NUM_CUSTOMERS)]

customersServed = 0
customersServedLock = threading.Lock()
exitSignal = threading.Event()

teller_exit_order = 0
exit_lock = threading.Condition()

def tellerCode(tellerId):
    print(f"Teller {tellerId} []: ready to serve")
    while not exitSignal.is_set():
        customerReady.acquire()

        if exitSignal.is_set():
            break

        queueLock.acquire()
        if not customerQueue:
            queueLock.release()
            continue
        customerId = customerQueue.pop(0)
        tellerAssignments[customerId] = tellerId
        queueLock.release()

        print(f"Teller {tellerId} [Customer {customerId}]: asks for transaction")
        ready[customerId].release()
        transactionSent[customerId].acquire()
        trans = customerTransaction[customerId]

        if trans == "Withdrawal":
            print(f"Teller {tellerId} [Customer {customerId}]: going to the manager")
            manager.acquire()
            print(f"Teller {tellerId} [Customer {customerId}]: getting manager's permission")
            time.sleep(random.uniform(0.005, 0.03))
            print(f"Teller {tellerId} [Customer {customerId}]: got manager's permission")
            manager.release()

        print(f"Teller {tellerId} [Customer {customerId}]: going to safe")
        safe.acquire()
        print(f"Teller {tellerId} [Customer {customerId}]: enter safe")
        time.sleep(random.uniform(0.01, 0.05))
        print(f"Teller {tellerId} [Customer {customerId}]: leaving safe")
        safe.release()

        print(f"Teller {tellerId} [Customer {customerId}]: finishes {trans.lower()} transaction")
        print(f"Teller {tellerId} [Customer {customerId}]: wait for customer to leave")
        left[customerId].acquire()

        global customersServed
        customersServedLock.acquire()
        customersServed += 1
        if customersServed == NUM_CUSTOMERS:
            exitSignal.set()
            for _ in range(NUM_TELLERS):
                customerReady.release()
        customersServedLock.release()

    global teller_exit_order
    with exit_lock:
        while teller_exit_order != tellerId:
            exit_lock.wait()
        print(f"Teller {tellerId} []: leaving for the day")
        teller_exit_order += 1
        exit_lock.notify_all()

def customerCode(customerId):
    time.sleep(random.uniform(0, 0.1))
    trans = random.choice(transactions)
    customerTransaction[customerId] = trans

    print(f"Customer {customerId} []: wants to perform a {trans.lower()} transaction")
    print(f"Customer {customerId} []: waiting to enter bank")
    door.acquire()
    print(f"Customer {customerId} []: entering bank")

    queueLock.acquire()
    customerQueue.append(customerId)
    queueLock.release()
    print(f"Customer {customerId} []: getting in line")

    customerReady.release()
    ready[customerId].acquire()
    tellerId = tellerAssignments[customerId]
    print(f"Customer {customerId} [Teller {tellerId}]: gives {trans.lower()} transaction")
    transactionSent[customerId].release()

    print(f"Customer {customerId} [Teller {tellerId}]: leaves teller")
    left[customerId].release()
    print(f"Customer {customerId} []: leaves the bank")
    door.release()

tellers = [threading.Thread(target=tellerCode, args=(i,)) for i in range(NUM_TELLERS)]
customers = [threading.Thread(target=customerCode, args=(i,)) for i in range(NUM_CUSTOMERS)]

for t in tellers:
    t.start()
for c in customers:
    c.start()

for c in customers:
    c.join()
for t in tellers:
    t.join()

print("The bank closes for the day.")
