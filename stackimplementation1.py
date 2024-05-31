
def push(stack,ele):
    stack.append(ele)
    print(ele," inserted into the stack succesfully ")
    print(stack)
def pop(stack):
    if len(stack)==0:
        print("stack is empty")
        return
    print(stack[-1],"deleted succesfully")
    stack.pop()
    print(stack)
    
stack=[]

push(stack,10)
push(stack,20)
push(stack,30)
push(stack,40)
push(stack,50)

pop(stack)
pop(stack)
pop(stack)
pop(stack)
pop(stack)