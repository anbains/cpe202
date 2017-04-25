import unittest

# a StrList is one of the following
# - "empty", or
# - a Pair(string, StrList)

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

# a ClassShape has two things:
# - a String to represent a name
# - a StrList of field names

class ClassShape:
    def __init__(self, name, strList):
        self.name = name
        self.strList = strList
    def __eq__(self, other):
        return (type(other) == ClassShape
                and self.name == other.name
                and self.strList == other.strList)
    def __repr__(self):
        return ("%r, %r" % (self.name, self.strList))

# StrList -> String
# joins lines of code into a single string

def join_lines(strList):
    if strList == "mt":
        return ""
    return strList.first + "\n" + join_lines(strList.rest)

# StrList -> StrList
# Returns a StrList of assignments from given field names

def fields_to_assignments(strList):
    if strList == "mt":
        return "mt"
    fieldAssign = "        self." + strList.first + " = " + strList.first
    return Pair(fieldAssign, fields_to_assignments(strList.rest))

# StrList -> String
# Returns a string where elements are joined by commas

def commasep(strList):
    if strList == "mt":
        return ""
    return ", " + strList.first + commasep(strList.rest)

# StrList -> StrList
# Returns a StrList representing lines of __init__

def init_method(strList):
    startingLine = "    def __init__(self" + commasep(strList) + "):"
    if strList == "mt":
        return Pair(startingLine, Pair("        pass", "mt"))
    return Pair(startingLine, fields_to_assignments(strList))

# ClassShape -> StrList
# Returns a StrList representing lines of __eq__

def eq_method(classShape):
    startingLine = "    def __eq__(self, other):" 
    returnLn1 = "        return (type(other) == " + classShape.name
    return Pair(startingLine, Pair(returnLn1,
        eq_return_lines(classShape.strList)))
        # Pair(eq_return_lines(classShape.strList), "mt")))

# StrList -> String
# Returns the formatted {!r} portion of the repr method

def repr_format_r(strList):
    if strList == "mt":
        return ""
    if strList.rest == "mt":
        return "{!r}"
    return "{!r}, " + repr_format_r(strList.rest)


# ClassShape -> StrList
# Returns a StrList representing lines of __repr__

def repr_method(classShape):
    startingLine = "    def __repr__(self):" 
    returnLn1 = ("        return \"" + classShape.name + "(" 
            + repr_format_r(classShape.strList) + ")\".format(" 
            + repr_format_string(classShape.strList) + ")")
    return Pair(startingLine, Pair(returnLn1, "mt"))

# ClassShape -> String
# Returns a single string containing the entire class definition

def render_class(classShape):
    classDef = "class " + classShape.name + ":"
    init = join_lines(init_method(classShape.strList))
    eq = join_lines(eq_method(classShape))
    rep = join_lines(repr_method(classShape))

    return classDef + "\n" + init + "\n" + eq + "\n" + rep

# Helper methods

# StrList -> StrList
# Returns a StrList containing 'and self.<field> == other.<field>'

def eq_return_lines(strList):
    if strList == "mt":
        return Pair("                )", "mt")
    return Pair(("                and self." + strList.first + " == other." 
            + strList.first), eq_return_lines(strList.rest))

# StrList -> String
# Returns string portion inside .format()

def repr_format_string(strList):
    if strList == "mt":
        return ""
    if strList.rest == "mt":
        return "self." + strList.first 
    return "self." + strList.first + ", " + repr_format_string(strList.rest)

# Test Cases

class TestCase(unittest.TestCase):
    
    # Test repr 
    def test_repr(self):
        strList = Pair("meme", Pair("memes", "mt"))
        reprStrList = "'meme', 'memes', 'mt'"
        self.assertEqual(repr(strList), reprStrList)

        classShape = ClassShape("Meme", strList) 
        reprClassShape = "'Meme', " + reprStrList 
        self.assertEqual(repr(classShape), reprClassShape)

    # Test eq
    def test_eq(self):
        strList = Pair("meme", Pair("memes", "mt"))
        strList2 = Pair("meme", Pair("memes", "mt"))
        classShape = ClassShape("Meme", strList)
        classShape2 = ClassShape("Meme", strList2)
        self.assertTrue(classShape == classShape2)

    # Testing join_lines
    def test_join_lines(self):
        strList = Pair("i", Pair("like", Pair("memes", "mt")))
        joinLinesStr = "i\nlike\nmemes\n"
        self.assertEqual(join_lines(strList), joinLinesStr)

    # Test fields_to_assignments
    def test_fields_to_assignments(self):
        strList = Pair("memeOne", Pair("memeTwo", "mt"))
        assignments = Pair("        self.memeOne = memeOne", 
                Pair("        self.memeTwo = memeTwo", "mt"))
        self.assertEqual(fields_to_assignments(strList), assignments)

    # Test commasep
    def test_commasep(self):
        strList = Pair("memeOne", Pair("memeTwo", "mt"))
        commasepStr = ", memeOne, memeTwo"
        self.assertEqual(commasep(strList), commasepStr)

    # Test init_method
    def test_init_method(self):
        strList = Pair("memeOne", Pair("memeTwo", "mt"))
        strListInitMethod = Pair("    def __init__(self, memeOne, memeTwo):", 
                Pair("        self.memeOne = memeOne", Pair("        self.memeTwo = memeTwo",
                "mt")))
        self.assertEqual(init_method(strList), strListInitMethod)

        strListEmpty = "mt"
        strListInitEmpty = Pair("    def __init__(self):",
                Pair("        pass", "mt"))
        self.assertEqual(init_method(strListEmpty), strListInitEmpty)

    # Test eq_method
    def test_eq_method(self):
        strList = Pair("memeOne", Pair("memeTwo", "mt"))
        classShape = ClassShape("Meme", strList)
        strListEqMethod = Pair("    def __eq__(self, other):",
                Pair("        return (type(other) == Meme", 
                Pair("                and self.memeOne == other.memeOne",
                Pair("                and self.memeTwo == other.memeTwo",
                Pair("                )", "mt")))))
        self.assertEqual(eq_method(classShape), strListEqMethod)

        strListEmpty = "mt"
        classShapeEmpty = ClassShape("Meme", strListEmpty)
        strListEqEmpty = Pair("    def __eq__(self, other):",
                Pair("        return (type(other) == Meme", 
                Pair("                )", "mt")))
        self.assertEqual(eq_method(classShapeEmpty), strListEqEmpty)

    # Test repr_method
    def test_repr_method(self):
        strList = Pair("memeOne", Pair("memeTwo", "mt"))
        classShape = ClassShape("Meme", strList)
        strListReprMethod = Pair("    def __repr__(self):", 
                Pair("        return \"Meme({!r}, {!r})\".format(self.memeOne, self.memeTwo)", 
                    "mt"))
        self.assertEqual(repr_method(classShape), strListReprMethod)

        strListEmpty = "mt"
        classShapeEmpty = ClassShape("Meme", strListEmpty)
        strListReprMethod = Pair("    def __repr__(self):", 
                Pair("        return \"Meme()\".format()", 
                    "mt"))
        self.assertEqual(repr_method(classShapeEmpty), strListReprMethod)

    # Test render_class
    def test_render_class(self):
        strList = Pair("memeOne", Pair("memeTwo", "mt"))
        classShape = ClassShape("Meme", strList)
        
        strListRender = "class Meme:\n    def __init__(self, memeOne, memeTwo):" 
        strListRender += "\n        self.memeOne = memeOne\n        self.memeTwo = memeTwo\n\n    " 
        strListRender += "def __eq__(self, other):\n        return (type(other) == Meme" 
        strListRender += "\n                and self.memeOne == other.memeOne\n                and "
        strListRender += "self.memeTwo == other.memeTwo\n                )\n\n    def __repr__(self):" 
        strListRender += "\n        return \"Meme({!r}, {!r})\".format(self.memeOne, self.memeTwo)\n"

        self.assertEqual(render_class(classShape), strListRender)

if (__name__ == '__main__'):
    unittest.main()
