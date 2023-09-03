#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
 #write a function to convert a list to a linked list
def list_to_linkedlist(lst):
    head = ListNode(lst[0])
    current = head
    for i in range(1, len(lst)):
        current.next = ListNode(lst[i])
        current = current.next
    return head

def print_ll(node1):
    node=node1
    while node:
        print(node.val)
        node = node.next

class Solution:
    def middle_element(self,head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse_ll(self,node):
        #for each node set its next node to point to previous node
        prev = None
        current = node
        while current:
            next = current.next # as we ll pe changing next to prev we need to keep tack of the next node to mode forward
            current.next = prev
            prev = current # now the reverse will pint to current element
            current = next
        return prev
    
    def isPalindrome(self, head) -> bool:
        #find the middle value of the ll
        middle = self.middle_element(head)
        #need to reverse from middle to end
        head_half_reverse = self.reverse_ll(middle)
        start, mid = head, head_half_reverse
        is_palindrome=True
        while mid:#we iterate trough mid as it reach none earlier
            if start.val != mid.val: # we iterate till mid, cause in case of even lenght both sizes are name 
                return False
            else:
                print(start.val,mid.val)
                start=start.next
                mid = mid.next
        return is_palindrome



if __name__ == "__main__":
    l1=[1,2,3,4]
    l1=list_to_linkedlist(l1)
    so =Solution()
    #print(so.middle_element(l1))
    # revere_l1= so.reverse_ll(l1)
    # print_ll(revere_l1)
    # l1=[1,2,3,4,5]
    # l1=list_to_linkedlist(l1)
    # #print(so.middle_element(l1))
    # revere_l1= so.reverse_ll(l1)
    # print_ll(revere_l1)
    l1=[1,2,3,2,1]
    l1=list_to_linkedlist(l1)
    #get to middle and rever from there
    mid = so.middle_element(l1)
    r_m = so.reverse_ll(mid)
    print_ll(l1)
    print('reverse')
    print_ll(r_m)
    #print(so.isPalindrome(l1))