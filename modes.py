'''
Authonr(s): Anthony, Nick, Dylan
Created date: 10/27/21
Description: This file contains both the functions class (tools class) and the modes class
The functions class contians functions to call autopep8, pycodestyle & pylint
The modes class contains various function calls to create the program modes
last edit: 11/01/21
PLEASE UPDATE LAST EDIT WHEN YOU UPDATE THIS FILE
'''
import os
from pylint import epylint

'''
date: 10/27/21
author: Anthony
description: This class contains the functions that call the 3 tools Chkpy will use
'''
class Tools:

    '''
    date: 10/27/21
    author: Anthony
    description: This function calls autopep8 from the system and runs it against an input file
    '''
    def auto8(filename): # F1
        os.system("autopep8 --in-place --aggressive --aggressive --aggressive " + filename)

    '''
    date: 11/01/21
    author: Nick
    description: This function calls pylint and runs it against an input file and returns the
    output in a tuple, first part of the tuple should be what we need most of the time however
    im returning both just in case
    '''
    def pylint(filename): #F2
        (pylint_stdout, pylint_stderr) = epylint.py_run(filename, return_std=True)
        return pylint_stdout.getvalue(), pylint_stderr.getvalue()


    '''
    date: 10/27/21
    author: Dylan
    description: This function calls pycodestyle from the system and runs it against an input file
    Think about running with either --count or --statistics if needed
    '''
    def pycode(filename): #F3
        pycodestyle = os.popen("pycodestyle " + filename).read()
        return pycodestyle



class Modes:
    def Before_and_after_mode():
        pass
    def Dev_Mode():
        pass
    def Report_mode():
        pass
    pass
