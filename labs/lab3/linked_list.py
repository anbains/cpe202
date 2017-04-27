# Section 1: LinkedList

# AnyList Data Definition

# an AnyList is one of the following
# - None, or
# - Pair(first, rest)

class Pair:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest
    
    def __eq__(self, other):
        return (type(other) == Pair
                and self.first == other.first
                and self.rest == other.rest)

    def __repr__(self):
        return ("%r, %r" % (self.first, self.rest))

# Functions

# No arguments
# Returns an empty list

def empty_list():
    return None 

# AnyList int [any type] -> AnyList
# Returns a new list with the given value inserted at the given index

def add(list, index, value):
    if (list == None and index == 0):
        return Pair(value, None)
    if (list == None):
        raise IndexError("Index is out of bounds")
    if (index == 0):
        return Pair(value, list)
    if (list.rest == None and index > 1):
        raise IndexError("Index is out of bounds")
    return Pair(list.first, add(list.rest, index - 1, value))

# AnyList -> int
# Returns number of elements in list

def length(list):
    if (list == None):
        return 0;
    return 1 + length(list.rest)

# AnyList int -> int
# Returns value at given index

def get(list, index):
    if (list == None):
        raise IndexError("Index is out of bounds")
    if (list.rest == None and index > 0):
        raise IndexError("Index is out of bounds")
    if (index == 0):
        return list.first
    return get(list.rest, index - 1)

# AnyList int [any type] -> AnyList
# Returns list with element replaced with given value at given index

def set(list, index, value):
    if (list == None):
        raise IndexError("Index is out of bounds")
    if (list.rest == None and index > 0):
        raise IndexError("Index is out of bounds")
    if (index == 0):
        return Pair(value, list.rest) 
    return Pair(list.first, set(list.rest, index - 1, value))

# AnyList int -> Tuple
# Returns 2-tuple of removed element and resulting list

def remove(list, index):
    if (list == None):
        raise IndexError("Index is out of bounds")
    if (list.rest == None and index > 0):
        raise IndexError("Index is out of bounds")
    return remove_element(list, index), remove_list(list, index) 

# AnyList int -> AnyList
# Returns list with removed element at given index

def remove_list(list, index):
    if (list == None):
       raise IndexError("Index is out of bounds")
    if (list.rest == None and index > 0):
       raise IndexError("Index is out of bounds")
    if (index == 0):
       return list.rest
    return Pair(list.first, remove_list(list.rest, index - 1))

# AnyList int -> [any value]
# Returns removed element at given index

def remove_element(list, index):
    if (list == None):
       raise IndexError("Index is out of bounds")
    if (list.rest == None and index > 0):
       raise IndexError("Index is out of bounds")
    if (index == 0):
       return list.first
    return remove_element(list.rest, index - 1)

