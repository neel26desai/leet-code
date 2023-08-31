#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        #first merge 2 linked list
        #we'll merge both in new list
        #check if the first list is not empty, if its not point the last element to the first element of list2,
        current = list1
        head = current
        if list1:
            while current.next:
                current = current.next
        #we reached the end
        #check if list2 is not empty before pointing 
            if list2:
                current.next = list2
        else:
            #list1 is empty, so point the head to list2
            head = list2
        #sort the 2 linked list using : Bubble sort
        #we'll use 2 pointers, one for current and one for next
        current = head
        while current:
            next_node = current.next
            while next_node:
                if current.val > next_node.val:
                    #swap the values
                    current.val, next_node.val = next_node.val, current.val
                next_node = next_node.next
            current = current.next
        return head

if __name__ == "__main__":
    #create 2 linked list, using lists and for loop
    list1 = [1,2,4]
    list2 = [3,5]
    #convertignt the above lists to linked list
    ll1 = ListNode(1)
    ll1_head = ll1
    for i in list1[1:]:
        ll1.next = ListNode(i)
        ll1 = ll1.next
    #refactor the above 3 lines of code and for ll2
    ll2 = ListNode(3)
    ll2_head = ll2
    for i in list2[1:]:
        ll2.next = ListNode(i)
        ll2 = ll2.next

    # #print both linked list entirely, using while loop
    # current = ll1_head
    # while current:
    #     print(current.val)
    #     current = current.next
    # current = ll2_head
    # while current:
    #     print(current.val)
    #     current = current.next
    
    #create a function object
    obj = Solution()
    #call the function
    new_head = obj.mergeTwoLists(ll1_head, ll2_head)
    while new_head:
        print(new_head.val)
        new_head = new_head.next


  