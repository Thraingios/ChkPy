''' 
Authonr(s): Anthony, Nick, Dylan
Created date: 10/27/21
Description: This file contains both the functions class (tools class) and the modes class
The functions class contians functions to call autopep8, pycodestyle & pylint
The modes class contains various function calls to create the program modes
last edit: 10/27/21
PLEASE UPDATE LAST EDIT WHEN YOU UPDATE THIS FILE
'''
import os

''' 
date: 10/27/21
author: Anthony
description: This class contians the fucntions that call the 3 tools Chkpy will use
'''
class Tools:

    ''' 
    date: 10/27/21
    author: Anthony
    description: This fucntion calls autopep8 from the system and runs it agenst a input file
    '''
    def auto8(filename): # F1
        os.system("autopep8 filename")

    ''' 
    date: 10/27/21
    author: Anthony
    description: This fucntion calls pylint and runs it agenst a input file
    '''
    def pylint(): #F2
        pass

    ''' 
    date: 10/27/21
    author: Anthony
    description: This fucntion calls pycodestyle from the system and runs it agenst a input file
    '''
    def pycode(): #F3
        pass



class Modes:
    pass