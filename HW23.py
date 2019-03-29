#Task 1

class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class linkedList:
	def __init__(self):
        	self.head=None
	
	def append(self,data):
        	newNode=Node(data)
        	if self.head==None:
            		self.head=newNode
            		return
        	else:
            		lastNode=self.head
            		while lastNode.next != None:
                		lastNode=lastNode.next
            		lastNode.next=newNode
        
	def deleteAtPos(self,pos):
		curNode=self.head
		if pos==0:
			self.head=curNode.next
			curNode=None
			return
		else:
			cnt=0
			prev=None
			while curNode != None and cnt != pos:
				prev=curNode
				curNode=curNode.next
				cnt+=1
			if curNode==None:
				print("The node doesn't exist")
				return
			else:
				prev.next=curNode.next
				curNode=None

	def len_iterative(self):
		cnt=0
		curNode=self.head
		while curNode != None:
			curNode=curNode.next
			cnt+=1
		return cnt
	
	def len_recursive(self, headNode):
		if headNode is None:
			return 0
		else:
			return 1+self.len_recursive(headNode.next)

	def printList(self):
    		curNode=self.head
    		while curNode!=None: 
        		print(curNode.data)
        		curNode=curNode.next

	def swapNode(self, key1, key2):
		if key1==key2:
			print('The two nodes are the same node, cannot be swapped')
			return
		
		prev1=None
		curNode1=self.head
		while curNode1 != None and curNode1.data != key1:
			prev1=curNode1.next
	
		prev2=None
		curNode2=self.head
		while curNode2 != None and curNode2.data != key2:
			prev2=curNode2
			curNode2=curNode2.next

		if curNode1==None or curNode2==None:
			print("The nodes don't exist in the list")
			return
		else:
			if prev1==None:
				self.head=curNode2
				prev2.next=curNode1
			elif prev2==None:
				self.head=curNode1
				prev1.next=curNode2
			else:
				prev1.next=curNode2
				prev2.next=curNode1
			
			temp1=curNode1.next
			temp2=curNode2.next
			curNode1.next=temp2
			curNode2.next=temp1

	def reverse_iterative(self):
		prev=None
		curNode=self.head
		while curNode !=None:
			nxt_temp=curNode.next
			curNode.next=prev
			prev=curNode
			curNode=nxt_temp
		self.head=prev

lst=linkedList()
lst.append(5)
lst.append(4)
lst.append(8)
lst.append(1)
lst.append(6)
lst.printList()
print('\n')

lst.deleteAtPos(3)
lst.printList()
print('\n')

print(lst.len_recursive(lst.head))
print('\n')

lst.swapNode(5,6)
lst.printList()
print('\n')

lst.reverse_iterative()
lst.printList()

