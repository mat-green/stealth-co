'''
Created on 24 Jan 2016

@author:     Matthew Green

@copyright:  2016 New Edge Engineering Ltd. All rights reserved.

@license:    MIT
'''
import unittest

from models import Graph, Coordinate

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
        self.assertEqual(actual, "                    \n" \
                                 "                    \n" \
                                 "                    \n" \
                                 "                    \n" \
                                 "                    \n" \
                                 "                    \n" \
                                 "                    \n" \
                                 "                    \n" \
                                 "                    \n" \
                                 "                    ")


    def testDot(self):
        # test set up
        component = Graph(20,10)
        start = Coordinate(1,1)
        end = Coordinate(1,1)
        # test execution
        component.plot(start, end)
        actual = component.render()
        # test verification
        self.assertEqual(actual, "                    \n" \
                                 " X                  \n" \
                                 "                    \n" \
                                 "                    \n" \
                                 "                    \n" \
                                 "                    \n" \
                                 "                    \n" \
                                 "                    \n" \
                                 "                    \n" \
                                 "                    ")


    def testHorizontal(self):
        # test set up
        component = Graph(20,10)
        start = Coordinate(0,4)
        end = Coordinate(19,4)
        # test execution
        component.plot(start, end)
        actual = component.render()
        # test verification
        self.assertEqual(actual, "                    \n" \
                                 "                    \n" \
                                 "                    \n" \
                                 "                    \n" \
                                 "XXXXXXXXXXXXXXXXXXXX\n" \
                                 "                    \n" \
                                 "                    \n" \
                                 "                    \n" \
                                 "                    \n" \
                                 "                    ")


    def testVertical(self):
        # test set up
        component = Graph(20,10)
        start = Coordinate(1,1)
        end = Coordinate(1, 8)
        # test execution
        component.plot(start, end)
        actual = component.render()
        # test verification
        self.assertEqual(actual, "                    \n" \
                                 " X                  \n" \
                                 " X                  \n" \
                                 " X                  \n" \
                                 " X                  \n" \
                                 " X                  \n" \
                                 " X                  \n" \
                                 " X                  \n" \
                                 " X                  \n" \
                                 "                    ")


    def testDiagonal(self):
        # test set up
        component = Graph(20,10)
        start = Coordinate(1,1)
        end = Coordinate(8, 8)
        # test execution
        component.plot(start, end)
        actual = component.render()
        # test verification
        self.assertEqual(actual, "                    \n" \
                                 " X                  \n" \
                                 "  X                 \n" \
                                 "   X                \n" \
                                 "    X               \n" \
                                 "     X              \n" \
                                 "      X             \n" \
                                 "       X            \n" \
                                 "        X           \n" \
                                 "                    ")


    def testBackDiagonal(self):
        # test set up
        component = Graph(20,10)
        start = Coordinate(4,9)
        end = Coordinate(14, 0)
        # test execution
        component.plot(start, end)
        actual = component.render()
        # test verification
        self.assertEqual(actual, "             X      \n" \
                                 "            X       \n" \
                                 "           X        \n" \
                                 "          X         \n" \
                                 "         X          \n" \
                                 "        X           \n" \
                                 "       X            \n" \
                                 "      X             \n" \
                                 "     X              \n" \
                                 "    X               ")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testBlank']
    unittest.main()