import unittest

# * Section 1 (Lists)

# * dd: NumList Data Definition

# a NumList is one of the following
# - "empty", or
# - Pair(first, rest)

class Pair:
    def __init__(self, first, rest):
        self.first = first # a number
        self.rest = rest # a NumList

    def __eq__(self, other):
        return (type(other) == Pair
                and self.first == other.first
                and self.rest == other.rest)
    def __repr__(self):
        return ("%r, %r" % (self.first, self.rest))

# * 1:

# NumList -> int
# Returns the number of values in the given list

def length(numList):
    if numList == "mt":
        return 0
    return 1 + length(numList.rest)

# * 2:

# NumList -> int
# Returns of the sum of the values in the given list

def sum(numList):
    if numList == "mt": 
        return 0
    return numList.first + sum(numList.rest)

# * 3:

# NumList int -> int
# Returns number of values in given list above given threshold value

def count_greater_than(numList, threshold):
    if numList == "mt":
        return 0
    if numList.first <= threshold:
        return count_greater_than(numList.rest, threshold)
    if numList.first > threshold:
        return 1 + count_greater_than(numList.rest, threshold)

# * 4:

# NumList int -> int
# Returns position of value in given list

def find(numList, val, position=None):
    if numList == "mt":
        return None
    if position == None:
        position = 0
    if numList.first == val:
        return position
    return find(numList.rest, val, position + 1)

# * 5:

# NumList -> NumList
# Returns a new linked list where each number in given list is smaller by one

def sub_one_map(numList):
    if numList == "mt":
        return "mt"
    return Pair(numList.first - 1, sub_one_map(numList.rest))

# * 6:

# NumList int -> NumList
# Returns a new list where given number is inserted into proper position in
# given sorted list

def insert(numList, num):
    if numList == "mt":
        return Pair(num, "mt")
    if num > numList.first:
        return Pair(numList.first, insert(numList.rest, num))
    if num <= numList.first:
        return Pair(num, numList)

# * Tests : the test case class for the list functions

class TestCase(unittest.TestCase):

    # repr tests
    def test_repr(self):
        numList = Pair(8, Pair(2, Pair(3, Pair(12, "mt"))))
        self.assertEqual(repr(numList), "8, 2, 3, 12, 'mt'")

    # length tests
    def test_length(self):
        numListEmpty = "mt"
        numList = Pair(8, Pair(2, Pair(3, Pair(12, "mt"))))
        sortedNumList = Pair(3, Pair(6, Pair(9, Pair(12, "mt"))))

        self.assertEqual(length(numListEmpty), 0)
        self.assertEqual(length(numList), 4) 
        self.assertEqual(length(sortedNumList), 4) 

    # sum tests
    def test_sum(self):
        numList = Pair(8, Pair(2, Pair(3, Pair(12, "mt"))))
        sortedNumList = Pair(3, Pair(6, Pair(9, Pair(12, "mt"))))

        self.assertEqual(sum(numList), 25)
        self.assertEqual(sum(sortedNumList), 30)

    # count_greater_than tests
    def test_count_greater_than(self):
        numList = Pair(8, Pair(2, Pair(3, Pair(12, "mt"))))
        sortedNumList = Pair(3, Pair(6, Pair(9, Pair(12, "mt"))))

        self.assertEqual(count_greater_than(numList, 5), 2)
        self.assertEqual(count_greater_than(sortedNumList, 5), 3)

    # find tests
    def test_find(self):
        numList = Pair(8, Pair(2, Pair(3, Pair(12, "mt"))))
        sortedNumList = Pair(3, Pair(6, Pair(9, Pair(12, "mt"))))

        self.assertEqual(find(numList, 4), None)
        self.assertEqual(find(numList, 8), 0)
        self.assertEqual(find(numList, 12), 3)

    # sub_one_map tests
    def test_sub_one_map(self):
        numList = Pair(8, Pair(2, Pair(3, Pair(12, "mt"))))
        sortedNumList = Pair(3, Pair(6, Pair(9, Pair(12, "mt"))))
        decrementedNumList = Pair(7, Pair(1, Pair(2, Pair(11, "mt"))))
        decrementedSortedList = Pair(2, Pair(5, Pair(8, Pair(11, "mt"))))

        self.assertEqual(sub_one_map(numList), decrementedNumList)
        self.assertEqual(sub_one_map(sortedNumList), decrementedSortedList)

    # insert tests
    def test_insert(self):
        emptyNumList = "mt"
        insertEmpty = Pair(3, "mt")
        sortedNumList = Pair(3, Pair(6, Pair(9, Pair(12, "mt"))))
        insertSortedList = Pair(3, Pair(5, Pair(6, Pair(9, Pair(12, "mt")))))

        self.assertEqual(insert(sortedNumList, 5), insertSortedList)
        self.assertEqual(insert(emptyNumList, 3), insertEmpty)

if (__name__ == '__main__'):
    unittest.main()
