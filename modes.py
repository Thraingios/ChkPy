'''
Authonr(s): Anthony, Nick, Dylan
Created date: 10/27/21
Description: This file contains both the functions class (tools class) and the modes class
The functions class contians functions to call autopep8, pycodestyle & pylint
The modes class contains various function calls to create the program modes
last edit: 11/02/21
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
        return("\nRUNNING AUTOPEP8 WITH AGRESSIVENESS LVL 3\n")

    '''
    date: 11/01/21
    edited 11/09/21
    author: Nick
    description: This function calls pylint and runs it against an input file and returns the
    output in a tuple, first part of the tuple should be what we need most of the time however
    im returning both just in case
    '''
    def pylint(filename): #F2
        (pylint_stdout, pylint_stderr) = epylint.py_run(filename, return_std=True)
        #return pylint_stdout.getvalue()
        return "\n OUTPUT FROM PYLINT! \n\n" + pylint_stdout.getvalue() + "\n"

    '''
    date: 10/27/21
    author: Dylan
    description: This function calls pycodestyle from the system and runs it against an input file
    Think about running with either --count or --statistics if needed
    '''
    def pycode(filename): #F3
        pycodestyle = os.popen("pycodestyle " + filename).read()
        return "\n OUTPUT FROM PYCODESTYLE! \n" + pycodestyle + "\n"


        


class Modemaker(object):
    '''
    date: 11/09/21
    author: Nick
    description: This class takes in a filename as well as a variable amount of other variables (which would be the names of tools) to help build the object
    '''
    def __init__(self, filename, optargs): #note *args is a variable argument meaning that it can take any amount of arguments
        self.filename = filename
        self.optargs = optargs
    
    def run(self):
        '''
        date: 11/09/21
        author: Nick
        description:
        has two blank lists, one being the command list. this is where we take the arguments passed when making the object and turns them into usable commands.
        we then iterate through this command list using eval to actually run the command (note i know its techinally bad practice but the user wont be supplying any of the
        arguments for it and is just used internally) from there we take the output (if any) from each command and append it to command out which is then returned to the user
        '''
        command_list = []
        command_out = []
        for arg in self.optargs:
            command_list.append("Tools." + arg +"('" + self.filename +"')")
        for command in command_list:
            command_out.append(eval(command))
        return command_out
        
        

            
            

