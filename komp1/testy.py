import unittest
from komp2.kalkulator import *

# def add(a):
#     return(1)

def my_function ( my_list ):
    if len ( my_list ) == 0:
        raise ValueError

class TestMyMethods (unittest.TestCase):
    def test1(self):
        v = add("1")
        self.assertEqual(v,1)

    def test0(self):
        v = add("")
        self.assertEqual(v,0)

    def test1_2(self):
        v = add("1,2")
        x = add("2,1")
        self.assertEqual(v,3)
        self.assertNotEqual(v,12)
        self.assertIs(x,v)

    def test12(self):
        v = add("12")
        self.assertEqual(v,12)
        

    def test_wielu(self):
        v = add("1,2,3,4,55")
        self.assertEqual(v,65)


   
        
unittest.main()

