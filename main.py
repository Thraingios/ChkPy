'''
Authonr(s): Anthony, Nick, Dylan
Created date: 10/27/21
Description: This is the main class for checkpy, this is what the users will interact with whn the file is run.
last edit: 10/27/21
PLEASE UPDATE LAST EDIT WHEN YOU UPDATE THIS FILE
'''


'''
date: 10/27/21
author: Anthony
description: This is the main class of the file.
'''




import modes
import art
class main:
    art.openart()

    myfile = input("ENTER A FILENAME HERE -> ")

    mypylint = modes.Tools.pylint(myfile)
    print(mypylint[0])

    # currently using input for testing only, changed this to use input at myfile so i didnt have to repeat myself - Nick
    modes.Tools.auto8(myfile)


if __name__ == "__main__":
    main()
