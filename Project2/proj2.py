import threading
import random
import time


queueLock = threading.Semaphore(1)
customerReady = threading.Semaphore(0)
NUM_TELLERS = 2
NUM_CUSTOMERS = 3

customerQueue = []
tellerAssignments = {}


ready = [threading.Semaphore(0) for _ in range(NUM_CUSTOMERS)]
introduced = [threading.Semaphore(0) for _ in range(NUM_CUSTOMERS)]

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

        print("Teller", tellerId, "[Customer", customerId, "]: serving a customer")
        ready[customerId].release()
        introduced[customerId].acquire()
        print("Teller", tellerId, "[Customer", customerId, "]: noted customer introduction")

def customerCode(customerId):
    time.sleep(random.uniform(0, 0.05))
    queueLock.acquire()
    customerQueue.append(customerId)
    queueLock.release()
    print("Customer", customerId, "[]: getting in line")

    customerReady.release()
    ready[customerId].acquire()
    tellerId = tellerAssignments[customerId]
    print("Customer", customerId, "[Teller", tellerId, "]: introduces itself")
    introduced[customerId].release()


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


