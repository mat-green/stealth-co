'''
Created on 24 Jan 2016

@author:     Matthew Green

@copyright:  2016 New Edge Engineering Ltd. All rights reserved.

@license:    MIT
'''

class Graph(object):
    '''
    classdocs
    '''

    def __init__(self, width, height):
        '''
        Constructor.

        :param width: Width of the graph as a Integer.
        :param height: Height of the graph as a Integer.
        '''
        grid = []
        a = 0
        while a < height:
            b = 0
            row = []
            while b < width:
                row.append(" ")
                b += 1
            grid.append(row)
            a += 1
        self.grid = grid


    def render(self):
        result = [ ''.join(line) for line in self.grid ]
        return '\n'.join(result)
