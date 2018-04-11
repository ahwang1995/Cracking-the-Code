from NodeSLL import Node
#add the sum of two linked lists assuming that the head is the one's place
def sumLists(head1,head2):
	factor = 1
	head1Num = 0
	head2Num = 0
	#get the number for head1
	while(head1.next != None):
		head1Num = head1Num + head1.data*factor
		factor = factor*10
		head1 = head1.next
	head1Num = head1Num + head1.data*factor
	factor = 1
	#get the number for head2
	while(head2.next != None):
		head2Num = head2Num + head2.data*factor
		factor = factor*10
		head2 = head2.next
	head2Num = head2Num + head2.data*factor
	#sum the the numbers together and return
	return head1Num + head2Num

num1 = Node(3)
num1.appendToTail(7)
num1.appendToTail(2)

num2 = Node(4)
num2.appendToTail(4)
num2.appendToTail(4)
num2.appendToTail(4)

print(sumLists(num1,num2))