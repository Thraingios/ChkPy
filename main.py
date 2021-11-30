'''
Author(s): Anthony, Nick, Dylan
Created date: 10/27/21
Description: This is the main class for ChkPy, this is what the users will 
interact with when the file is run.
last edit: 11/20/21
'''

import modes, getopt, os, directory

def main(args):
    '''
    date: 11/20/21
    author: Anthony, Nick, Dylan 
    description: This is the main for ChkPy, when this function is called 
    it requires the folowing: A file/directory name plus any options.

    chkpy has 3 options:

    - the default or " " which runs reporting tools before and after attempting to fix styling/syntax (Before and after mode)

    - the "-r" option which only runs reporting tools against the given file/directory (reporting mode)

    - the "-d" option which runs reporting tools AFTER attempting to fix styling/syntax (developer mode)
    '''
    opts, args = getopt.getopt(args,"dr")
    file = args[0]
    Dir_mode_steps = ['directorymode']
    Default_steps =['pylint','pycode', 'auto8', 'pylint', 'pycode']
    Dev_mode_steps = ['auto8', 'pylint', 'pycode']
    Report_mode_steps = ['pylint', 'pycode']
    
    seperator = "\n=====================================================================\n"
    if os.path.isdir(file):
        print('Running from a directory!')
        directory.Directory(Dir_mode_steps,args)
        exit()

    if len(args) == 1:
        Default_mode = modes.Modemaker(file, Default_steps)
        print(*Default_mode.run(), sep = seperator)
    for arg in args:
        if arg in ['-d']:
            Dev_mode = modes.Modemaker(file, Dev_mode_steps)
            print(*Dev_mode.run(), sep = seperator)

        elif arg in ['-r']:
            Report_mode = modes.Modemaker(file, Report_mode_steps)
            print(*Report_mode.run(), sep = seperator)