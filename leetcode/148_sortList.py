# -*- coding: utf-8 -*-
"""
给你链表的头结点head，请将其按升序排列并返回排序后的链表
"""

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            fast = slow = head
            pre = None
            
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            
            if not pre:
                return head
            pre.next = None
            
            left = self.sortList(head)
            right = self.sortList(slow)
            
            p = dummy = ListNode(-1)
            while left and right:
                if left.val < right.val:
                    p.next = left
                    left = left.next
                else:
                    p.next = right
                    right = right.next
                p = p.next
                
            if left:
                p.next = left
            if right:
                p.next = right
            return dummy.next
        
class ListNode():
    def __init__(self,val=None):
        self.val = val
        self.next = None

class link_list():
    def __init__(self,iter_list=None):
        self.head=None
        self._construct(iter_list)
        
    def _construct(self,iter_list):
        if len(iter_list) == 0 or iter_list is None:
            raise ValueError('wrong input')
        self.head = ListNode(iter_list[0])
        cur = self.head
        for i in iter_list[1:]:
            cur.next = ListNode(i)
            cur = cur.next
        
    def __repr__(self):
        cur = self.head
        res = ''
        while cur is not None:
            res+= str(cur.val)
            res+= '->'
            cur = cur.next
        return res
        
if __name__ == '__main__': 
    a = ListNode(4)
    a.next= ListNode(2)
    a.next.next = ListNode(1)
    a.next.next.next = ListNode(3)
    res = Solution().sortList(a)
    while res is not None:
        print(res.val,'->',end='')
        res = res.next