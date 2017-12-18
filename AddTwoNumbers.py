# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		nodeAdded = ListNode(l1.val + l2.val)
		if (l1.next == None and l2.next == None):
			return 
		addTwoNumbers(self, l1.next, l2.next)

def main():
	newNode = ListNode(0)
	addTwoNumbers(nodeList[0], nodeList[1], newNode)

main()
