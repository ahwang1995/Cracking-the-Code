from NodeSLL import Node
from stack import Stack
#check if a linked list is a palindrome
def palindrome(head):
	#get the length of the linked list
	linkedLength = head.listLength()
	n = head
	#use a stack to store the front of the linked list
	revFront = Stack()
	for x in range(0,linkedLength/2):
		revFront.push(n)
		n = n.next

	#if the linked list has an odd length then skip the middle node
	if (linkedLength % 2) == 1:
		n = n.next
	#compare the reversed front and back of the list
	while (n.next != None):
		temp = revFront.pop()
		print temp
		if temp.data != n.data:
			return False
		n = n.next
	temp = revFront.pop()
	#last compare
	if temp.data != n.data:
		return False
	return True

palinNode = Node('a')
palinNode.appendToTail('b')
palinNode.appendToTail('c')
palinNode.appendToTail('c')
palinNode.appendToTail('a')
print (palindrome(palinNode))