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
    modes.Tools.auto8(input("ENTER A FILENAME HERE -> ")) #currently useing input for testing ownly
    pass


if __name__ == "__main__":
    main()