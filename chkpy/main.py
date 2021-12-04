'''
Author(s): Anthony, Nick, Dylan
Created date: 10/27/21
Description: This is the main class for ChkPy, this is what the users will
interact with when the file is run.
last edit: 11/20/21
'''
import getopt
import os
import sys
import modes
import directory


def main(args):
    '''
    date: 11/20/21
    author: Anthony, Nick, Dylan
    description: This is the main for ChkPy, when this function is called
    it requires the folowing: A file/directory name plus any options.

    chkpy has 3 options:

    - the default or " " which runs reporting tools before and
      after attempting to fix styling/syntax (Before and after mode)

    - the "-r" option which only runs reporting tools against,
      the given file/directory (reporting mode)

    - the "-d" option which runs reporting tools AFTER,
      attempting to fix styling/syntax (developer mode)
    '''
    opts, args = getopt.getopt(args, "dr")
    file = args[0]
    dir_mode_steps = ['directorymode']
    default_steps = ['pylint', 'pycode', 'auto8', 'pylint', 'pycode']
    dev_mode_steps = ['auto8', 'pylint', 'pycode']
    report_mode_steps = ['pylint', 'pycode']

    seperator = "\n=====================================================================\n"
    if os.path.isdir(file):
        print('Running from a directory!')
        directory.directory(dir_mode_steps, args)
        sys.exit()

    if len(args) == 1:
        default_mode = modes.Modemaker(file, default_steps)
        print(*default_mode.run(), sep=seperator)
    for arg in args:
        if arg in ['-d']:
            dev_mode = modes.Modemaker(file, dev_mode_steps)
            print(*dev_mode.run(), sep=seperator)

        elif arg in ['-r']:
            report_mode = modes.Modemaker(file, report_mode_steps)
            print(*report_mode.run(), sep=seperator)
