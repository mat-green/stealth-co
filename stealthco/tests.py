'''
Created on 24 Jan 2016

@author:     Matthew Green

@copyright:  2016 New Edge Engineering Ltd. All rights reserved.

@license:    MIT
'''
import unittest

from models import Graph

class TestGrid(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testBlank(self):
        # test set up
        component = Graph(20,10)
        # test execution
        actual = component.render()
        # test verification
        self.assertEqual("                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    ", actual)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testBlank']
    unittest.main()