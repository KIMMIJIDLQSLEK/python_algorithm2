#[3]->[4]
#Node에는 data, next가 있어야한다.
class Node:
    def __init__(self,data): #constructer(생성자)
        self.data=data
        self.next=None

#1. node의 데이터값 보기
#print(node.data)

#2. 다음 node의 데이터값 보기
# node=Node(3)
# first_node=Node(4)
# node.next=first_node #연결
# print(node.next.data)

# #3. 쉽게 LinkedList만들기
# class LinkedList:
#     def __init__(self,data):
#         self.head=Node(data)  #Node로 이동

# linked_list=LinkedList(3)  #LnkedList로 이동
# print(linked_list.head.data)  #3출력
# print(linked_list.head.next)  #None출력

#4. append로 node붙히기  [3]->[4]->[5]->[6]->[new] 맨뒤에 노드를 새로 붙히고 싶음
class LinkedList:
    def __init__(self,data):
        self.head=Node(data)  #Node로 이동

    def append(self,data): #cur을 이용해 맨끝의 노드까지 이동할것(다음 노드가 None일 때까지)
        # case 1. head에 data가 없을경우 -> 생성
        if self.head is None:
            self.head = Node(data)
            return

        # self.head.next=Node(data)
        # case 2. head에 data가 있을경우
        cur=self.head #현재 head [3]의 위치에 있음

        while cur.next is not None:
            cur=cur.next
        cur.next=Node(data)
#5. linked_list 모든 data 출력
    def print_all(self):
        cur=self.head
        while cur is not None:
            print(cur.data)
            cur=cur.next




linked_list=LinkedList(3)  #LnkedList로 이동
linked_list.append(4)
linked_list.append(5)

linked_list.print_all() #5