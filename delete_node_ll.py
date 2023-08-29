# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # current = head
        # if current.val == node.val:
        #     #if the preset value is the node to be removed
        #     head = head.next
        
        # else:
        # #not the first element    
        #     while current.next:
        #         if current.next.val == node.val:
        #             #since we know that node is not the last element we can just point the previous current.next to current.next.next
        #             current.next = current.next.next
        #         else:
        #             current = current.next
        
        #change the value of  the present node to next node and delete the next node
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next





if __name__ == '__main__':
    #create a linked list using the ListNode class
    #conver the below list to a linked list
    a=[4,5,1,9]
    #create a linked list using for loop
    head = ListNode(a[0])
    current = head
    for i in range(1,len(a)):
        current.next = ListNode(a[i])
        current = current.next
    #initialize the solution class
    solution = Solution()
    #call the function
    node=ListNode(1)
    solution.deleteNode(node)
    #print the linked list after deletion
    current = head
    while current:
        print(current.val)
        current = current.next
