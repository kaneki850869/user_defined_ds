#Queue implementation

queue = []
max_size = int(input('Enter the size of queue'))
def enqueue():
    if len(queue) == max_size:
        print('Queue is full:(')
    else:
        elem = input('Enter the element:')
        queue.append(elem)
        print(queue)
def dequeue():
    if not queue:
        print('Queue is empty!')
    else:
        e = queue.pop(0)
        print('Removed element is:', e)
def isfull():
    if len(queue) == max_size:
        print(True)
    else:
        print(False)
def isempty():
    if not queue:
        print(True)
    else:
        print(False)
def display():
    print(queue)
def Front():
    front = queue[0]
    print(front)
def Rear():
    rear = queue[-1]
    print(rear)
    
while True:
    print('Select the mode of operation 1.enqueue 2.Dequeue 3.isfull 4.isempty 5.display 6.Front 7.Rear 8.quit')
    option = int(input())
    if option == 1:
        enqueue()
    elif option == 2:
        dequeue()
    elif option == 3:
        isfull()
    elif option == 4:
        isempty()
    elif option == 5:
        display()    
    elif option == 6:
        Front()
    elif option == 7:
        Rear()
    elif option == 8:
         break        
    else:
        print('Enter the correct option')