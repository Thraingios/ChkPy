'''
Author(s): Anthony, Nick, Dylan, MRegirouard
Created date: 10/27/21
Description: This file contains both the functions class (
tools class) and the modes class
The functions class contains functions to call autopep8, pycodestyle & pylint
The modes class contains various function calls to create the program modes
last edit: 02/13/22
PLEASE UPDATE LAST EDIT WHEN YOU UPDATE THIS FILE
'''
import os
from os import walk
from pylint import epylint


class Tools:
    '''
    date: 10/27/21
    author: Anthony
    description: This class contains the
    functions that call the 3 tools ChkPy will use
    '''

    def auto8(filename):  # F1
        '''
        date: 10/27/21
        author: Anthony, MRegirouard
        description: This function calls autopep8 from the system and runs
        it against an input file
        '''
        os.system(
            "autopep8 --in-place --aggressive --aggressive --aggressive " +
            "\"" + filename + "\"")
        return "\nRUNNING AUTOPEP8 WITH AGRESSIVENESS LVL 3\n"

    def pylint(filename):  # F2
        '''
        date: 11/01/21
        edited: 02/13/22
        author: Nick, MRegirouard
        description: This function calls pylint and
        runs it against an input file and returns the
        output in a tuple, first part of the tuple should be
        what we need most of the time however
        im returning both just in case
        '''

        (pylint_stdout, pylint_stderr) = epylint.py_run("\"" + filename + "\"",
        return_std=True)
        return "\n OUTPUT FROM PYLINT! \n\n" + pylint_stdout.getvalue() + "\n"

    def pycode(filename):  # F3
        '''
        date: 10/27/21
        edited: 02/13/22
        author: Dylan, MRegirouard
        description: This function calls pycodestyle
        from the system and runs it
        against an input file
        '''

        pycodestyle = os.popen("pycodestyle " + "\"" + filename + "\"").read()
        return "\n OUTPUT FROM PYCODESTYLE! \n" + pycodestyle + "\n"

    def directorymode(mydirectory):
        '''
        date: 11/20/21
        author: Nick & Dylan
        description: This function takes in a directory from main and runs,
        each of the tools in this program against each,
        file in the directory tree. This includes all sub-folders
        '''

        dirlist = []
        for (root, dirs, files) in walk(mydirectory):
            for name in files:
                if '.py' in name[-3:]:
                    dirlist.append(os.path.join(root, name))
        return dirlist


class Modemaker():
    '''
    date: 11/09/21
    author: Nick
    description: This class takes in a filename as well as a variable,
    amount of other variables (which would be the names of tools)
    to help build the object
    '''

    # note *args is a variable argument meaning that it can take any amount of
    # arguments
    def __init__(self, filename, optargs):
        '''
        date: 11/09/21
        author: Nick
        description: initialization of the variables for Modemaker
        '''
        self.filename = filename
        self.optargs = optargs

    def run(self):
        '''
        date: 11/09/21
        author: Nick
        description:
        has two blank lists, one being the command list.
        This is where we take the arguments
        passed when making the object and
        turns them into usable commands.
        we then iterate through this command list using eval
        to actually run the command
        (note i know its techinally bad practice but the user wont be
        supplying any of the arguments for it and is just used internally)
        from there we take the output (if any) from each command and append it
        to command out which is then returned to the user
        '''
        command_list = []
        command_out = []

        for arg in self.optargs:
            command_list.append("Tools." + arg + "('" + self.filename + "')")

        for command in command_list:
            command_out.append(eval(command))
        return command_out
