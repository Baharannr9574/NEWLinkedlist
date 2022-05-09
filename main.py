class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Node.__init__(self, data)
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            # listOne.headValue = Node("first")
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def display(self):
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(current.data)
            current = current.next
        print(nodes)

    def traverse(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.next


def addTwoNumbers(l1: LinkedList, l2: LinkedList):
    # dummy = cur = Node(0)
    carry = 0
    l3 = LinkedList()
    while l1.head or l2.head:
        if l1:
            currentNode = l1.head
            carry += currentNode.data
            l1.head=currentNode.next

        if l2:
            currentNode = l2.head
            carry += currentNode.data
            l2.head = currentNode.next
    l3.append(carry)
    return l3.display()


def printList(head):

	ptr = head
	while ptr:
		print(ptr.data, end=' —> ')
		ptr = ptr.next
	print('None')


def reverse(head):

	out = None
	current = head

	while current:
		next = current.next
		current.next = out
		out = current
		current = next

	return out


def append(X, Y):

	head = None
	prev = None
	carry = 0

	while X or Y:

		total = 0
		if X:
			total += X.data
		if Y:
			total += Y.data

		total += carry
		carry = total // 10
		total = total % 10

		node = Node(total)

		if head is None:
			prev = node
			head = node
		else:
			prev.next = node
			prev = node

		X = X.next if X else X
		Y = Y.next if Y else Y

	if carry:
		prev.next = Node(carry, prev.next)

	return head


def addLists(X, Y):

	# reverse `X` and `Y` to access elements from the end
	X = reverse(X)
	Y = reverse(Y)

	return reverse(append(X, Y))