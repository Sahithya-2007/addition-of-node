class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
def iterate(head):
    temp=head
    while temp!=None:
        print(temp.val,end=" ")
        temp=temp.next
        
def insert (idx,newnode,head):
    temp=head
    cnt=1 
    while cnt<idx:
        temp=temp.next
        cnt+=1 
    temp1=temp.next
    temp.next=newnode
    newnode.next=temp1
    
head=Node(5)
head.next=Node(10)
head.next.next=Node(4)
insert(2,Node(15),head)
iterate(head)