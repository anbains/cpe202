import unittest
from linked_list import *

class TestList(unittest.TestCase):

    #  Testing class and function definitions
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)

    # Testing __repr__
    def test_repr(self):
        emptyList = empty_list()
        self.assertEqual(repr(emptyList), "None")

        list = Pair("memes", Pair(3, Pair("meme", None)))
        self.assertEqual(repr(list), "'memes', 3, 'meme', None")

    # Testing empty_list
    def test_empty_list(self):
        emptyList = empty_list()
        self.assertEqual(repr(emptyList), "None")

    # Testing add
    def test_add(self):
        emptyList = empty_list()
        emptyAdd = Pair("meme", None)
        self.assertEqual(add(emptyList, 0, "meme"), emptyAdd)
        self.assertRaises(IndexError, add, emptyList, 2, "meme")
        self.assertRaises(IndexError, add, emptyList, -2, "meme")

        list = Pair("memes", Pair(3, Pair("meme", None)))
        addList = Pair("memes", Pair(4, Pair(3, Pair("meme", None))))
        self.assertEqual(add(list, 1, 4), addList)
        self.assertRaises(IndexError, add, list, 6, "meme")

    # Testing length
    def test_length(self):
        emptyList = empty_list()
        self.assertEqual(length(emptyList), 0)

        list = Pair("memes", Pair(3, Pair("meme", None)))
        self.assertEqual(length(list), 3)

    # Testing get
    def test_get(self):
        emptyList = empty_list()
        self.assertRaises(IndexError, get, emptyList, 0)

        list = Pair("memes", Pair(3, Pair("meme", None)))
        self.assertEqual(get(list, 1), 3)
        self.assertEqual(get(list, 2), "meme")
        self.assertRaises(IndexError, get, list, 6)

    # Testing set
    def test_set(self):
        emptyList = empty_list()
        self.assertRaises(IndexError, set, emptyList, 0, "meme")

        list = Pair("memes", Pair(3, Pair("meme", None)))
        setList1 = Pair("memez", Pair(3, Pair("meme", None)))
        setList2 = Pair("memez", Pair(3, Pair("memes", None)))
        self.assertEqual(set(list, 0, "memez"), setList1)
        self.assertEqual(set(setList1, 2, "memes"), setList2)
        self.assertRaises(IndexError, set, list, 6, "blank")

    # Testing remove
    def test_remove(self):
        emptyList = empty_list()
        self.assertRaises(IndexError, remove, emptyList, 0)

        list = Pair("memes", Pair(3, Pair("meme", None)))
        rmList1 = Pair("memes", Pair("meme", None))
        rmTuple = (3, rmList1)
        self.assertRaises(IndexError, remove, list, 7)
        self.assertEqual(remove(list, 1), rmTuple)

        listNone = Pair("memes", None)
        self.assertRaises(IndexError, remove, listNone, 7)

    # Testing remove_list
    def test_remove_list(self):
        emptyList = empty_list()
        self.assertRaises(IndexError, remove_list, emptyList, 0)

        list = Pair("memes", Pair(3, Pair("meme", None)))
        self.assertRaises(IndexError, remove, list, 7)

        listNone = Pair("memes", None)
        self.assertRaises(IndexError, remove_list, listNone, 7)

    # Testing remove_element
    def test_remove_element(self):
        emptyList = empty_list()
        self.assertRaises(IndexError, remove_element, emptyList, 0)

        list = Pair("memes", Pair(3, Pair("meme", None)))
        self.assertRaises(IndexError, remove_element, list, 7)

if __name__ == '__main__':
    unittest.main()
