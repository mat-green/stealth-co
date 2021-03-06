'''
Created on 24 Jan 2016

@author:     Matthew Green

@copyright:  2016 New Edge Engineering Ltd. All rights reserved.

@license:    MIT
'''

class Graph(object):
    '''
    Object that plots vectors as lines and render to ascii characters.
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


    def plot(self, start, end):
        '''
        Updated the graph with a plotted line
        
        :param start: The start coordinate as a Coordinate
        :param end: The end coordinate as a Coordinate
        '''
        # determine direction
        rise = end.y - start.y
        run = end.x - start.x
        if(rise != 0 and run != 0):
            slope = float(abs(rise)) / float(abs(run))
        else :
            slope = 0
        # insert X into grid
        x = start.x
        y = start.y
        if(rise >= 0):
            while x <= (end.x) and y <= (end.y):
                self.grid[y][x] = "X"
                if(slope > 0):
                    if(slope < 1):
                        x += int(round(slope, 0))
                    else:
                        x += int(slope)
                    y += 1
                else: # use rise and run to determine direction.
                    if(rise > 0):
                        y += 1
                    else:
                        x += 1
        elif(rise <= 0):
            while x <= (end.x) and y >= (end.y):
                self.grid[y][x] = "X"
                if(slope > 0):
                    if(slope < 1):
                        x += int(round(slope, 0))
                    else:
                        x += int(slope)
                    y -= 1
                else: # use rise and run to determine direction.
                    if(rise < 0):
                        y -= 1
                    else:
                        x += 1


    def render(self):
        '''
        Basic render of data.
        
        :return: Ascii string of characters
        '''
        result = [ ''.join(line) for line in self.grid ]
        return '\n'.join(result)



class Coordinate(object):
    '''
    Holds coordinates
    '''

    def __init__(self, x, y):
        '''
        Constructor.

        :param x: X position as a Integer.
        :param y: Y position as a Integer.
        '''
        self.x = x
        self.y = y
