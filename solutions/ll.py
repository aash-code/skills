
from models.CustomLinkedList import LinkedList
from utils.render import linked_list_from_array


def remove_dupes_from_linked_list(ip):
    '''Implement an algo to remove nodes with duplicate values from a linked list.'''
    if ip is None or len(ip) < 1:
        return ip
    
    # The snippet here creates a linkedlist from input array.
    ll = linked_list_from_array(ip)

    # Actual Solution starts here.    
    found = set()
    prev = None
    curr = ll.head
    
    while curr:
        if curr.value in found:
            prev.next = curr.next
        else:
            found.add(curr.value)
            prev = curr
        curr = prev.next
        
    return ll.as_list()

def find_kth_element_from_last_node_in_linked_list(ip):
    '''Implement an algo to find value of kth element prior to the last node of the linked list.'''
    if ip is None or len(ip) < 2 or len(ip[0]) == 0 or type(ip[1]) is not int:
        return []
    
    # The snippet here creates a linkedlist from input array.
    ll = linked_list_from_array(ip[0])
    k = ip[1]
    
    # Actual Solution starts here.
    slow = ll.head
    fast = ll.head

    for i in range(k):
        if fast.next:
            fast = fast.next
        else:
            return []
    
    while fast.next:
        fast = fast.next
        slow = slow.next
        
    return slow.value


def delete_node_from_linked_list(ip):
    '''Implement an algo where given a node, delete it from the linked list it resides in. do not delete last node'''
    if ip is None or len(ip) < 2 or len(ip[0]) == 0 or type(ip[1]) is not int or ip[1]<1:
        return ip[0]
    
    # The snippet here extracts a node from an input array at given position.
    ll = linked_list_from_array(ip[0])
    
    node = ll.head
    
    for i in range(ip[1]-1):
        if node is None or node.next is None:
            return ip[0]
        else:
            node = node.next

    # Actual Solution starts here.
    if node.next is None:
        return ip[0]
    
    next = node.next
    
    node.value = next.value
    node.next = next.next
        
    return ll.as_list()

def partition_linked_list_at_value(ip):
    '''Implement an algo where given a linkedlist and a value n, partition the linked list such that all nodes with values less than n are on the left and rest on the right side'''
    if ip is None or len(ip) < 2 or len(ip[0]) == 0 or type(ip[1]) is not int:
        return ip[0]
    
    # The snippet here extracts a node from an input array at given position.
    ll = linked_list_from_array(ip[0])
    node = ll.head
    x = ip[1]
    
    # actual solution starts here
    left = None
    left_ptr = None
    right = None
    right_ptr = None
    
    ctr = 0
    
    while node is not None:
        if(node.value < x):
            if(left is None):
                left = node
                left_ptr = left
            else:
                left_ptr.next = node
                left_ptr = node
        else:
            if(right is None):
                right = node
                right_ptr = right
            else:
                right_ptr.next = node
                right_ptr = node
        node = node.next

    if(left is None):
        ll.head = right
    else:
        ll.head = left
        left_ptr.next = right
    if(right_ptr is not None):
        right_ptr.next = None

    return ll.as_list()
