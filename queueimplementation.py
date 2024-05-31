def enqueue(Q,ele):
    Q.append(ele)
    print(ele,"inserted into Queue")
    print(Q)

def deQueue(Q):
    if len(Q)==0:
        print("queue is empty")
        return
    print(Q[0],"is getting deleted")
    Q.pop(0)
    print(Q)

Q=[]
enqueue(Q,10)
enqueue(Q,20)
enqueue(Q,30)
enqueue(Q,40)
print("the Quese are:",Q)

deQueue(Q)
deQueue(Q)
deQueue(Q)
deQueue(Q)

