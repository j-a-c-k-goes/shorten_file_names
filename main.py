'''
    Program:   main.py

    Objective: automate shortening of program files exceeding 8 characters.

    Design:    a] walk filesystem for program files
               b] evaluate length
               c] prompt to change to shorter name
'''
import sys
import os
from msg import *
from usage import *
from cargs import *
from seek import *
if __name__ == '__main__':
    arg = CheckArgs()
    try:
        if arg.get('status') == True:
            path_to_walk    = arg.get('path')
            mode            = arg.get('mode')
            ext             = arg.get('ext')
            Msg('update', 'Proceeding.')
            Seek(path_to_walk, mode, ext)
        else:
            exit(-1)
    except Exception as exception:
        Msg('exception', exception)