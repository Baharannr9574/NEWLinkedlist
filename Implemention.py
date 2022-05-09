from main import Node,LinkedList,addTwoNumbers,addLists,printList,reverse,append

list1 = LinkedList()
list2 = LinkedList()
list3 = LinkedList()

list1.append(2)
list1.append(4)
list1.append(3)

list2.append(5)
list2.append(6)
list2.append(4)

list1.display()
list2.display()

#addTwoNumbers(list1, list2)

printList(addLists(list1.head, list2.head))
#reverse(list1.head)
#append(list1.head,list2.head)
