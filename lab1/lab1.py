import unittest

#* Section 1 (Git)

# persnickety

#* Section 2 (Data Definitions)

#* 1)

# Fahrenheit is a double that represents temperature in degrees Fahrenheit
# Celsius is a double that repesents temperature in degrees Celsius

class Fahrenheit:
    def __init__(self, celsius, fahrenheit):
        self.celsius = celsius
        self.fahrenheit = fahrenheit * (9/5) + 32

    def __repr__(celsius, fahrenheit):
        return "Celsius: %r, Fahrenheit: %r" % (self.celsius, self.fahrenheit)

    def __eq__(self, other):
        return (type(other) == Fahrenheit 
                and self.celsius == other.celsius 
                and self.fahrenheit == other.fahrenheit)

#* 2)

# a Price is a int that represents the price of an item in cents

class Price:
    def __init__(self, price):
        self.price = price

    def __repr__(price):
        return "Price: %r" % (self.price)

    def __eq__(self, other):
        return type(other) == Price and self.price == other.price

#* 3)

# a PriceRecord is an object that includes both the price and name of the item
# the Price is an integer that represents the price of an item in cents
# the Name is a string that represents the name of the item

class PriceRecord:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(name, price):
        return "Name: %r, Price: %r" % (self.name, self.price)

    def __eq__(self, other):
        return type(other) == PriceRecord and self.name == other.name and self.price == other.price

#* 4)

# an OpenTab is an object that includes the URL being visited and the date
# on which it was loaded 
# a URL is a string that is the website of the OpenTab
# a Date is a string that represents the date on which the OpenTab was visited

class OpenTab:
    def __init__(self, url, date):
        self.url = url
        self.date = date

    def __repr__(url, date):
        return "URL: %r, Date: %r" % (self.url, self.date)

    def __eq__(self, other):
        return (type(other) == OpenTab 
                and self.url == other.url 
                and self.date == self.date)

#* Section 3 (Signature, Purpose Statements, Headers)

#* 1)

# int double -> double
# adds sales tax to the given price

def addSalesTax(price):
    pass

#* 2)

# string -> Price
# finds price for named item in a store's price database

def findItem(name):
    pass

#* 3)

# Region, db -> int
# computes median income in a given geographic region

def medianIncome(region, db):
    pass

#* 4)

# Region, DB -> List
# determines cities that overlap in the region using a given geographic region
# and a database

def citiesOverlap(region, db):
    pass

#* Section 4 (Test Cases)

#* 1)

# int, int, int -> int
# determines second largest number from a set of 3 given numbers

def secondLargest(int1, int2, int3):
    pass

def testSecondLargest():
    int1, int2, int3 = 5, 7, 8
    self.assertEqual(secondLargest(int1, int2, int3), 7)
    int3 = 6
    self.assertEqual(secondLargest(int1, int2, int3), 6)

#* 2)

# String -> Boolean
# determines if a string has capital letters

def capitals(str):
    pass

def testCapitals():
    str1 = "meme"
    str2 = "mEme"
    str3 = "MEME"
    self.assertEqual(capitals(str1), True)
    self.assertEqual(capitals(str2), False)
    self.assertEqual(capitals(str3), False)

#* 3)

# String, String -> String
# determines the northernmost state, given two

def northernmost(state1, state2):
    pass

def testNorthernmost():
    state1 = "California"
    state2 = "Oregon"
    state3 = "Washington"
    self.assertEqual(northernmost(state1, state2), "Oregon")
    self.assertEqual(northernmost(state1, state3), "Washington")
    self.assertEqual(northernmost(state1, state2), "Washington")

#* Section 5 (Whole Functions)

#* 1)

# a Length is a double represented as a number of feet 
# double -> double
# converts a given number of feet to meters

def f2m(feet):
   return feet * 0.3048 

#* 2)

# a MusicalNote is a pitch represented through a frequency and a duration
# a Frequency is represented in hertz
# a Duration is represented as a length in seconds

class MusicalNote: 
    def __init__(self, pitch, duration):
        self.pitch = pitch
        self.duration = duration

    def __repr__(self, pitch, duration):
        return ("Pitch: %r, Duration: %r" % (self.pitch, self.duration))

    def __eq__(self, other):
        return (type(other) == MusicalNote
                and self.pitch == other.pitch
                and self.duration == other.duration)
#* 3)

# a MusicalNote is a pitch reprsented through a frequency and a duration
# MusicalNote -> MusicalNote
# returns the given musical note one octave higher, by doubling the frequency

def up_one_octave(musicalNote):
    return MusicalNote(musicalNote.pitch * 2, musicalNote.duration)

#* 4)

# a MusicalNote is a pitch reprsented through a frequency and a duration
# MusicalNote -> MusicalNote
# returns the given musical note one octave higher, by doubling the frequency

def up_one_octave_m(musicalNote):
    musicalNote.pitch = musicalNote.pitch * 2
    return None

class TestCase(unittest.TestCase):

    # f2m tests
    def testF2m():
        numFeet = 1.0
        self.assertEqual(f2m(numFeet), 0.3048)

    # Musical Note tests
    def testMusicalNote():
        note = MusicalNote(4, 5)
        self.assertEqual(note.pitch, 4)
        self.assertEqual(note.duration, 6)
    
    # up_one_octave tests
    
    def testUpOneOctave():
        musicalNote1 = MusicalNote(3, 4)
        musicalNote2 = MusicalNote(6, 4)
        self.assertEqual(up_one_octave(musicalNote1), musicalNote2)

    # up_one_octave_m tests
    
    def testUpOneOctaveM():
        musicalNote1 = MusicalNote(3, 4)
        musicalNote2 = MusicalNote(6, 4)
        self.assertEqual(up_one_octave_m(musicalNote1), None)
        up_one_octave_m(musicalNote1)
        self.assertEqual(musicalNote1.pitch, musicalNote2.pitch)

if (__name__ == '__main__'):
    unittest.main()
