# Section 2: ArrayList

# ArrayList Data Definition

# an ArrayList is one of the following
# - None, or
# - List(array, length, capacity)

class List:
    def __init__(self):
        self.array = [None] * 10
        self.length = 0 
        self.capacity = 10
    
    def __eq__(self, other):
        return (type(other) == List
                and self.array == other.array
                and self.length == other.length
                and self.capacity == other.capacity)

    def __repr__(self):
        return ("%r, %r, %r" % (self.array, self.length, self.capacity))

# Functions

# No arguments
# Returns an empty list

def empty_list():
    return List() 

# ArrayList int [any type] -> ArrayList
# Returns a new list with the given value inserted at the given index

def add(list, index, value):
    if (index > list.length or index < 0):
        raise IndexError("Index out of bounds")
    else:
        if (list.length == list.capacity):
            list.array += [None]
            list.capacity += 1
        for i in range(list.length - index):
            list.array[list.length - i] = list.array[list.length - i - 1]
        list.array[index] = value
        list.length += 1
        return list

# ArrayList -> int
# Returns number of elements in list

def length(list):
    return list.length

# ArrayList int -> int
# Returns value at given index

def get(list, index):
    if (index >= list.length or index < 0):
        raise IndexError("Index out of bounds")
    else:
        return list.array[index]

# ArrayList int [any type] -> ArrayList
# Returns list with element replaced with given value at given index

def set(list, index, value):
    if (index >= list.length or index < 0):
        raise IndexError("Index out of bounds")
    else:
        list.array[index] = value
        return list

# ArrayList int -> Tuple
# Returns 2-tuple of removed element and resulting list

def remove(list, index):
    if (index >= list.length or index < 0):
        raise IndexError("Index out of bounds")
    else:
        removedElement = list.array[index]
        for i in range(index, list.length):
            list.array[index] = list.array[index + 1]
            index += 1
        list.length -= 1
        return removedElement, list

