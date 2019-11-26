#back to basics 

class Node: 
    def __init__(self, val): 
        self.value = val
        self.next = None
       
    def insert(self, head, val):
        new_head = Node(val)
        new_head.next= head
        return new_head
    
def printList(head):
    while head:
        print(head.value)
        head = head.next

def reverseList(head):
    newHead = None
    while head: 
        tempNode = head.next
        head.next = newHead
        newHead = head
        head = tempNode
    return newHead     

def isPalindrome(head):
    reverse = reverseList(head)
    if reverse == head:
        return True 
    else:
        return False
     
if __name__ == '__main__':
#usage examples 
    first = Node(1)
    second = Node(2)
    third = Node(3) 

    first.next  = second
    second.next = third
    #testing print List. Should print 1 2 3
    printList(first)
    
    #testing reverseList. Should print 3 2 1
    reverse = reverseList(first)
    printList(reverse)

    print(isPalindrome(first))