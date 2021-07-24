# Definition for singly-linked list.
import sys


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry_digit = 0
        i = 0
        while l1 is not None and l2 is not None:
            x = ListNode(0, None)
            if i == 0:
                head_ans = x
                ans = x
                i += 1
            else:
                ans.next = x
                ans = ans.next
            sum_digit = l1.val + l2.val + carry_digit
            carry_digit = sum_digit // 10
            sum_digit = sum_digit % 10

            ans.val = sum_digit

            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            x = ListNode(0, None)
            ans.next = x
            ans = ans.next
            sum_digit = l1.val + carry_digit
            carry_digit = sum_digit // 10
            ans.val = sum_digit % 10
            l1=l1.next

        while l2 is not None:
            x = ListNode(0, None)
            ans.next = x
            ans = ans.next
            sum_digit = l2.val + carry_digit
            carry_digit = sum_digit // 10
            ans.val = sum_digit % 10
            l2 = l2.next

        if carry_digit == 0:
            pass
        else:
            ans.next = ListNode(carry_digit, None)

        return head_ans


def LLinput(arr):
    if len(arr) == 0:
        return None
    prev = None
    head = ListNode(0, None)
    header = head
    for ele in arr:
        head.val = ele
        head.next = ListNode(0, None)
        prev = head
        head = head.next
    prev.next = None
    return header


def printLL(head):
    while head is not None:
        print(head.val, "->", sep="", end="")
        head = head.next
    print("None")
    return


l1 = LLinput(list(map(int,sys.stdin.readline().strip().split())))
l2 = LLinput(list(map(int,sys.stdin.readline().strip().split())))

printLL(l1)
printLL(l2)

ss = Solution()
l3 = ss.addTwoNumbers(l1,l2)
printLL(l3)
