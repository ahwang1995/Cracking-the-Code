from NodeSLL import Node
from stack import Stack
#check if a linked list is a palindrome
def palindrome(head):
	#get the length of the linked list
	linkedLength = head.listLength()
	n = head
	revFront = Stack()
	for x in range(0,linkedLength/2):
		revFront.push(n)
		n = n.next

	if (linkedLength % 2) == 1:
		n = n.next
	while (n.next != None):
		temp = revFront.pop()
		print temp
		if temp.data != n.data:
			return False
		n = n.next
	temp = revFront.pop()
	if temp.data != n.data:
		return False
	return True

palinNode = Node('a')
palinNode.appendToTail('b')
palinNode.appendToTail('c')
palinNode.appendToTail('c')
palinNode.appendToTail('a')
print (palindrome(palinNode))