import unittest
from array_list import *

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)

    # Testing __repr__
    def test_repr(self):
        list = List()
        list.array = [0, 1, 2]
        list.length = 3

        self.assertEqual(repr(list), "[0, 1, 2], 3, 10")

    # Testing empty_list
    def test_empty_list(self):
        list = List()
        self.assertEqual(list, List())

    # Testing add
    def test_add(self):
        list = List()

        addList1 = List()
        addList1.array = [1, None, None, None, None, None, None,
                None, None, None]
        addList1.length = 1

        self.assertRaises(IndexError, add, list, 1, 1)
        self.assertEqual(add(list, 0, 1), addList1)

        addList2 = List()
        addList2.array = [1, 2, 3, 4, None, None, None, None, None, None]
        addList2.length = 4
        
        list.array = [1, 2, 4, None, None, None, None, None, None, None]
        list.length = 3

        self.assertEqual(add(list, 2, 3), addList2)

        addList3 = List()
        addList3.array = [1, 2, 3, 4, None, None, None, None, None, None]
        addList3.length = 4
        
        list.array = [1, 2, 3, None, None, None, None, None, None, None]
        list.length = 3

        self.assertEqual(add(list, 3, 4), addList3)

        list.array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list.length = 10

        addList4 = List()
        addList4.array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        addList4.length = 11
        addList4.capacity = 11

        self.assertEqual(add(list, 10, 11), addList4)


    # Testing length
    def test_length(self):
        list = List()
        self.assertEqual(length(list), 0)

        list.array = [1, 2, None, None, None, None, None, None, None,
                None]
        list.length = 2
        self.assertEqual(length(list), 2)

    # Testing get
    def test_get(self):
        list = List()
        self.assertRaises(IndexError, get, list, 0)
        self.assertRaises(IndexError, get, list, 1)

        list.array = [1, 2, 3, None, None, None, None, None, None,
                None]
        list.length = 3
        self.assertEqual(get(list, 1), 2)
        add(list, 3, 4)
        self.assertEqual(get(list, 0), 1)
        self.assertEqual(get(list, 2), 3)
        self.assertRaises(IndexError, get, list, 7)
        self.assertRaises(IndexError, get, list, -1)

    # Testing set
    def test_set(self):
        list = List()
        self.assertRaises(IndexError, set, list, 0, 1)
        self.assertRaises(IndexError, set, list, 1, 1)

        list.array = [1, 2, 3, None, None, None, None, None, None,
                None]
        list.length = 3
        setList = List()
        setList.array = [1, 1, 3, None, None, None, None, None, None,
                None]
        setList.length = 3
        self.assertEqual(set(list, 1, 1), setList)
        self.assertRaises(IndexError, set, list, 7, 1)
        self.assertRaises(IndexError, set, list, -1, 1)

    # Testing remove
    def test_remove(self):
        list = List()
        self.assertRaises(IndexError, remove, list, 1) 

        list.array = [1, 2, 3, 3.5, 4, None, None, None, None,
                None]
        list.length = 5

        rmList = List()
        rmList.array = [1, 2, 3, 4, None, None, None, None, None, None]
        rmList.length = 4

        self.assertRaises(IndexError, remove, list, 8)
        self.assertRaises(IndexError, remove, list, -8)
        self.assertEqual(remove(list, 3), (3.5, rmList))

if __name__ == '__main__':
    unittest.main()
