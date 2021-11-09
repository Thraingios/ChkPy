#!/usr/bin/python

'''
Authonr(s): Anthony, Nick, Dylan
Created date: 10/27/21
Description: This is the main class for checkpy, this is what the users will interact with whn the file is run.
last edit: 11/09/21
PLEASE UPDATE LAST EDIT WHEN YOU UPDATE THIS FILE
'''


'''
date: 10/27/21
author: Anthony
description: This is the main class of the file.
'''




import modes, art, sys, getopt

def main(file,args):
    art.openart()
    opts, args = getopt.getopt(args,"Ddr")
    file = file[0]
    Dir_mode_steps = ['pylint','pycode','pylint'] # note this is an example just to run the steps we can fill them in later
    Dev_mode_steps = []
    Report_mode_steps = []

    print(file)

    for opt, args in opts:
        if opt in ['-D']:
            Directory_mode = modes.Modemaker(file, Dir_mode_steps)
            print(*Directory_mode.run(), sep = "\n") #the run function returns a list, so adding a * in front of it should iterate over the list and then seperates each list value by a newline

        if opt in ['-d']:
            Dev_mode = modes.Modemaker(file, Dev_mode_steps)
            print(*Dev_mode.run(), sep = "\n")

        if opt in ['-r']:
            Report_mode = modes.Modemaker(file, Report_mode_steps)
            print(*Report_mode.run(), sep = "\n")

    
    '''
    #mypylint = modes.Tools.pylint(file)
    #print(mypylint[0])

    #mypycodestyle = modes.Tools.pycode(file)
    #print(mypycodestyle)

    #modes.Tools.auto8(file)
    '''


if __name__ == "__main__":
    # print(sys.argv)
    main(sys.argv[1:], sys.argv[2:])