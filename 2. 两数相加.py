# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        l1Node = l1
        l2Node = l2
        additive = (l1Node.val + l2Node.val) // 10
        resultNode = ListNode((l1Node.val + l2Node.val) % 10, None)
        cursorNode = resultNode
        l1Node = l1Node.next
        l2Node = l2Node.next
        while True:
            if l1Node == None and l2Node == None:
                if additive == 0:
                    break
                cursorNode.next = ListNode(additive, None)
                break
            if l1Node == None: # l2Node != None
                nextAdditive = (additive + l2Node.val) // 10
                nextNode = ListNode((additive + l2Node.val) % 10, None)
                cursorNode.next = nextNode
                cursorNode = cursorNode.next
                additive = nextAdditive
                if additive > 0:
                    l2Node = l2Node.next
                    continue
                else:
                    nextNode.next = l2Node.next
                    break
            if l2Node == None: # l1Node != None
                nextAdditive = (additive + l1Node.val) // 10
                nextNode = ListNode((additive + l1Node.val) % 10, None)
                cursorNode.next = nextNode
                cursorNode = cursorNode.next
                additive = nextAdditive
                if additive > 0:
                    l1Node = l1Node.next
                    continue
                else:
                    nextNode.next = l1Node.next
                    break
            nextAdditive = (additive + l1Node.val + l2Node.val) // 10
            nextNode = ListNode((additive + l1Node.val + l2Node.val) % 10, None)
            cursorNode.next = nextNode
            cursorNode = cursorNode.next
            additive = nextAdditive
            l1Node = l1Node.next
            l2Node = l2Node.next
        return resultNode

class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        additive = (l1.val + l2.val) // 10
        resultNode = ListNode((l1.val + l2.val) % 10, None)
        cursorNode = resultNode
        l1 = l1.next
        l2 = l2.next
        while additive or l1 or l2:
            val = 0
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            if additive:
                val += additive
            additive = val // 10
            cursorNode.next = ListNode(val % 10, None)
            cursorNode = cursorNode.next
        return resultNode