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

import sys


program_usage = """USAGE:
main.py [(x,y) - (x,y), (x,y) - (x,y),...]
Where:
 (x,y) are coordinates within a 20 by 10 grid
"""


def main(argv=None): # IGNORE:C0111
    """Command line interface application
%s
""" % program_usage

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)



if __name__ == '__main__':
    sys.exit(main())
