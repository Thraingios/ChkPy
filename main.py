'''
Author(s): Anthony, Nick, Dylan
Created date: 10/27/21
Description: This is the main class for checkpy, this is what the users will interact with whn the file is run.
last edit: 11/15/21
PLEASE UPDATE LAST EDIT WHEN YOU UPDATE THIS FILE
'''

import modes, getopt, os, directory

def main(file,args):
    '''
    date: 11/20/21
    author: Anthony, Nick, Dylan 
    description: This is the main for chkpy, when this fucntion is called it requirs the folowing: A file/directory name plus any options.

    chkpy has 3 optons:

    - the default or " " whitch runs reporting tools before and after attempting to fix styling/syntax (Before and after mode)

    - the "-r" option whitch ownly runs reporting tools agenst the given file/directory (reporting mode)

    - the "-d" option whitch runs reporting tools AFTER attempting to fix styling/syntax (devleoping mode)

    chkpy will allow you to run BOTH modes silmutaniously although this is not reccomended for any serious user
    '''
    tempargs = args
    opts, args = getopt.getopt(args,"dr")
    file = file[0]
    Dir_mode_steps = ['directorymode']
    Default_steps =['pylint','pycode', 'auto8', 'pylint', 'pycode']
    Dev_mode_steps = ['auto8', 'pylint', 'pycode']
    Report_mode_steps = ['pylint', 'pycode']
    
    seperator = "\n=====================================================================\n"
    if os.path.isdir(file):
        print('Running from a directory!')
        directory.Directory(file,Dir_mode_steps,tempargs)
        exit()
        

    if not opts:
        Default_mode = modes.Modemaker(file, Default_steps)
        print(*Default_mode.run(), sep = seperator)
    for opt, args in opts:
        if opt in ['-d']:
            Dev_mode = modes.Modemaker(file, Dev_mode_steps)
            print(*Dev_mode.run(), sep = seperator)

        elif opt in ['-r']:
            Report_mode = modes.Modemaker(file, Report_mode_steps)
            print(*Report_mode.run(), sep = seperator)