# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:06:21 2018

@author: fahads99
"""
import unittest 
from inc import inc

class MyTest(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(inc(0), 1)
        self.assertEqual(inc(100), 101)
        self.assertEqual(inc(1), 2)
        self.assertEqual(inc(-1), 0)
        self.assertGreater(inc(4), 4)
        
        
if __name__ == '__main__':
    unittest.main()   
