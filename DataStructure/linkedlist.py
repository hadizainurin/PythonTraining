class Node:
    def __init__(self, head=None):
        #Create two list that has head and tail
        #This is similar to concept of pointer introduced in C++
        self.head = head  #struct node *next
        self.tail = None  #data

class SlinkedList:
    def __init__(self):
        self.head = None