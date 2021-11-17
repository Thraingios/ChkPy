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


def Directory(dir,steps,args):
    Directory_mode = modes.Modemaker(dir,steps)
    test = Directory_mode.run()
    for file in test[0]:
        tempfilelist = [file,args]
        print("\n|#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|\n|                                                           |\n"+'\033[1m'+'              Currently Testing\n'+'              '+file+'\033[0m' +"\n|                                                           |\n|#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#|\n")
        main.main(tempfilelist,args)



