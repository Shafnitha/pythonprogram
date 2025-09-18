
class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0

def balanced(str):
    bracket_match={')':'(',']':'[','}':'{'}  
    brackets=set(bracket_match.values())

    stack=Stack()
    for ch in str:
        if ch in brackets:
          stack.push(ch)
        elif ch in bracket_match:
            top=stack.pop()
            if top!=bracket_match[ch]:
                return "Not Balanced"  
    if stack.is_empty():
        return "Balanced"
    else:
        return "Not Balanced"
str=input("Enter the String:")
print(balanced(str))        



