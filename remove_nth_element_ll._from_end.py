# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n: int):
        #remove the nth element from the end
        #first lets find the the todday number of nodes
        length = 0
        current = head
        while current:
            length=length+1
            current = current.next
        
        #nth from the end i s length -n from the begining
        n_from_beg = length - n

        if n_from_beg==0:
            #dropping the first element of the list 
            return head.next
        else:    
            #iterate to n_from_beg and remove it
            current = head 
            pos = 0
            #iterating to make sure that the next element is not null
            while current.next:
                if pos == n_from_beg-1:
                    #before reaching the node to be deleted just point the next of current to the next.next
                    current.next = current.next.next
                    break
                    
                else:
                    #increase the pos by 1 and moce current to next
                    pos = pos+1
                    current = current.next

            return head

if __name__ == '__main__':
    #create a linked list using the ListNode class
    #conver the below list to a linked list
    a=[1,2,3,4,5]
    a=[1,2]
    #create a linked list using for loop
    head = ListNode(a[0])
    current = head
    for i in range(1,len(a)):
        current.next = ListNode(a[i])
        current = current.next
    #initialize the solution class
    solution = Solution()
    #call the function
    head = solution.removeNthFromEnd(head,2)
    #print the linked list after deletion
    current = head
    while current:
        print(current.val)
        current = current.next
