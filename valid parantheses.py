def validParentesis(word):
    stack=[]
    for char in word:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        else:
            if len(stack)==0:
                return False
            else :
                stack.pop()
                
    if len(stack)==0:
        return True
    return False
    
word = input()
result=validParentesis(word)
print(result)