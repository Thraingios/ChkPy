'''
Author(s): Nick, Dylan
Created date: 11/14/21
Description: This is the file for our directory mode, which goes through
a directory and gives a list back of specifically python filenames
last edit: 11/15/21
PLEASE UPDATE LAST EDIT WHEN YOU UPDATE THIS FILE
'''
import modes
import main


def directory(steps, args):
    '''
    Author(s): Nick, Dylan
    Created date: 11/14/21
    Description: This is the function for our directory mode,
    which goes through a directory (dir) and then goes through the directory,
    mode which gives a list back of specifically python filenames back to main
    runs main for every file in the list
    last edit: 11/15/21
    PLEASE UPDATE LAST EDIT WHEN YOU UPDATE THIS FILE
    '''
    directory_mode = modes.Modemaker(args[0], steps)
    test = directory_mode.run()
    for file in test[0]:
        temparglist = [file]
        if len(args) > 1:
            temparglist.append(args[1])
        print(
            "\n|#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|\n|",
            "                                                          |\n" +
            '\033[1m' +
            '              Currently Testing\n' +
            '              ' +
            file +
            '\033[0m' +
            "\n|                               ",
            "                          ",
            "|\n|#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|\n")
        main.main(temparglist)
