class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

#linked_list에 저장된값을 하나의 수로 만들어서 더하기 => 678+354=1032
def get_linked_list_sum(linked_list_1, linked_list_2):
    # head_1 = linked_list_1.head
    # head_2 = linked_list_2.head
    #
    # sum1=0
    # while head_1 is not None:
    #     sum1=sum1*10+head_1.data
    #     head_1=head_1.next
    #
    # sum2 = 0
    # while head_2 is not None:
    #     sum2 = sum2 * 10 + head_2.data
    #     head_2 = head_2.next
    #
    # return sum1+sum2

#중복 줄이기위해
    sum1=_get_linked_list_sum(linked_list_1)
    sum2=_get_linked_list_sum(linked_list_2)

    return sum1+sum2

def _get_linked_list_sum(linked_list):
    head=linked_list.head
    linked_list_sum = 0
    while head is not None:
        linked_list_sum = linked_list_sum * 10 + head.data
        head = head.next

    return linked_list_sum


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))