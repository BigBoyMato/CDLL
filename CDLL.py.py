# Globals given
NEXT = 1
PREV = 2
VALUE = 0


print('')
print('7 Variation by Kholodilin_1909, CDLL with head only')
print('List created and used in most functions: [10,20,30,40]' '\n')


print('1: add_to_the_back_7' '\n')


def add_to_the_back_7(value, head):
    item = [value, None, None]
    if head is None:
        head = item
    else:
        tail = head[PREV]
        tail[NEXT] = item
        item[PREV] = tail
    head[PREV] = item
    item[NEXT] = head
    return head


head = None
head = add_to_the_back_7(10, head)
head = add_to_the_back_7(20, head)
head = add_to_the_back_7(30, head)
head = add_to_the_back_7(40, head)
print(head, '\n')


print('2: add_to_the_front_7' '\n')


def add_to_the_front_7(value, head):
    item = [value, None, None]
    if head is None:
        head = item
    else:
        tail = head[NEXT]
        tail[PREV] = item
        item[NEXT] = tail
    head[NEXT] = item
    item[PREV] = head
    return head


head = None
head = add_to_the_front_7(10, head)
head = add_to_the_front_7(20, head)
head = add_to_the_front_7(30, head)
head = add_to_the_front_7(40, head)
print(head, '\n')


# Only head needed
# Not all of the CDLL properties is needed
print('3: print_elements_7' '\n')


def print_elements_7(head):
    if head is None:
        return None
    else:
        print(head[VALUE])
        present_node = head[NEXT]
        while present_node is not head:
            print(present_node[VALUE])
            present_node = present_node[NEXT]
            head[PREV] = present_node


head = None
head = add_to_the_back_7(10, head)
head = add_to_the_back_7(20, head)
head = add_to_the_back_7(30, head)
head = add_to_the_back_7(40, head)
print_elements_7(head)
# no print() needed, function itself is printing elements
print('\n')


print('4: get_at_index_7', '\n')


def get_at_index_7(index, head):
    print('Index given: ', index)
    if head is None:
        return None
    i = 0
    if i == index:
        return head[VALUE]
    present_node = head[NEXT]
    i += 1
    while present_node is not head:
        if i == index:
            return present_node[VALUE]
        i += 1
        present_node = present_node[NEXT]
    print("Index out of range")


head = None
head = add_to_the_back_7(10, head)
head = add_to_the_back_7(20, head)
head = add_to_the_back_7(30, head)
head = add_to_the_back_7(40, head)
head = get_at_index_7(0, head)
print(head, 'is the value of given index', '\n')


print('5: search_value_7', '\n')


def search_value_7(value, head):
    print('search for: ', value)
    present_node = head[NEXT]
    if value == head[VALUE]:
        print(head[VALUE], 'is included in the list:', 'True')
    else:
        while present_node is not head:
            if present_node[VALUE] == value:
                print(present_node[VALUE], 'is included in the list:', 'True')
                break
            present_node = present_node[NEXT]
            head[PREV] = present_node
            if present_node is head:
                print(value, 'is not included in the list:', 'False')


head = None
head = add_to_the_back_7(10, head)
head = add_to_the_back_7(20, head)
head = add_to_the_back_7(30, head)
head = add_to_the_back_7(40, head)
search_value_7(10, head)
search_value_7(30, head)
search_value_7(50, head)
# no print() needed, function itself is printing elements which are found
# in the DCLL or not found
print('')


print('6: remove_from_the_end_7', '\n')


def remove_from_the_end_7(value, head):
    if head is None:
        return None
    else:
        present_node = head[NEXT]
        while present_node is not head[PREV]:
            present_node = present_node[NEXT]
            head[PREV] = present_node
        present_node[NEXT] = head
        head[PREV] = present_node
    return head


head = None
head = add_to_the_back_7(10, head)
head = add_to_the_back_7(20, head)
head = add_to_the_back_7(30, head)
head = add_to_the_back_7(40, head)
head = remove_from_the_end_7(40, head)
print(head)
print('element from the end removed', '\n')


print('7: remove_from_the_front_7', '\n')


def remove_from_the_front_7(value, head):
    if head is None:
        return None
    else:
        tail = head[PREV]
        head = head[NEXT]
        present_node = head[NEXT]
        while present_node is not tail:
            present_node = present_node[NEXT]
            head[PREV] = present_node
        present_node[NEXT] = head
        head[PREV] = present_node
    return head


head = None
head = add_to_the_back_7(10, head)
head = add_to_the_back_7(20, head)
head = add_to_the_back_7(30, head)
head = add_to_the_back_7(40, head)
head = remove_from_the_front_7(10, head)
print(head)
print('element from the front  removed', '\n')
print('')
print('Thanks for watching!')
