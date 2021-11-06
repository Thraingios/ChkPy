'''
Authonr(s): Anthony, Nick, Dylan
Created date: 10/27/21
Description: This is the main class for checkpy, this is what the users will interact with whn the file is run.
last edit: 11/02/21
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

    for opt, args in opts:
        if opt in ['-D']:
            print('directory mode')

        if opt in ['-d']:
            print('dev mode ' + file)

        if opt in ['-r']:
            print('report mode ' + file)

    
    '''
    #mypylint = modes.Tools.pylint(file)
    #print(mypylint[0])

    #mypycodestyle = modes.Tools.pycode(file)
    #print(mypycodestyle)

    #modes.Tools.auto8(file)
    '''


if __name__ == "__main__":
   main(sys.argv[:1], sys.argv[2:])