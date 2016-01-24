# encoding: utf-8
'''
stealthco.main -- Technical Test

stealthco.main is a command line interface application that renders vectors as
ascii characters.

It defines classes_and_methods

Created on 24 Jan 2016

@author:     Matthew Green

@copyright:  2016 New Edge Engineering Ltd. All rights reserved.

@license:    MIT
'''

import sys, re

from models import Graph, Coordinate

program_usage = """USAGE:
main.py ["(x,y) - (x,y), (x,y) - (x,y),..."]
Where:
 (x,y) are coordinates within a 20 by 10 grid
Format of coordinates but be '(x,y) - (x,y), '. Without ', ' on the last coordinate.
"""


def main(argv=None): # IGNORE:C0111
    """Command line interface application
%s
""" % program_usage

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    graph = Graph(20,10)
    if(len(sys.argv) > 1):
        pattern = re.compile("\(([0-9]+),([0-9]+)\) - \(([0-9]+),([0-9]+)\)")
        vectors = sys.argv[1].split(', ')
        for coordinates in vectors:
            result = pattern.match(coordinates)
            if result:
                start = Coordinate(int(result.group(1)), int(result.group(2)))
                end = Coordinate(int(result.group(3)), int(result.group(4)))
                graph.plot(start, end)

    print(graph.render())


if __name__ == '__main__':
    sys.exit(main())
