# Stack implementation in python
stack = []
max_size = int(input('Enter the size of stack:'))
def push():
    if len(stack) == max_size:
        print('Stack is Full')
    else:
        elem =input('enter the element:')
        stack.append(elem)
        print(stack)
        
def pop():
    if not stack:
        print('Stack is empty!')
    else:
        e = stack.pop()
        print('Removed element is :', e)
        print(stack)
def display():
    print(stack)
def top_element():
    res = stack[-1]
    print(res)   
def isempty():
    if len(stack) == 0:
        print(True)
    else:
        print(False)
def isfull():
    if len(stack) == max_size:
        print(True)
    else:
        print(False)
    
    
while True:
    print('Select the operation to be performed 1.push 2.pop 3.display 4.top 5.isempty 6.isfull 7.quit')
    choice = int(input())
    if choice == 1: 
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        top_element()
    elif choice == 5:
          isempty()
    elif choice == 6:
        isfull()
    elif choice == 7:
        break
    else:
        print('Enter the correct choice')
