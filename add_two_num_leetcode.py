"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head=None
    def insertion_at_end(self,input_element):
        link_element=ListNode(input_element)
        pointer=self.head
        if pointer==None:
            self.head=link_element
            link_element.next=None
        else:
            while(pointer.next):
                pointer=pointer.next
            pointer.next=link_element
            link_element.next=None
    
class Solution(object):
    
    def generate_number(self,list_input):
        pointer=list_input
        generated_number=""
        while(pointer):
            generated_number=generated_number+str(pointer.val)
            pointer=pointer.next
        return generated_number[::-1]
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1=self.generate_number(l1)
        num2=self.generate_number(l2)
        sum_num=str(int(num1)+int(num2))
        invert_num = sum_num[::-1]
        # print invert_num
        llist1=LinkedList()
        for i in range(len(invert_num)):
            llist1.insertion_at_end(int(invert_num[i]))
        return llist1.head
        