import sys, getopt


def main(file,args):
    opts, args = getopt.getopt(args,"Ddr")
    file = file[0]

    for opt, args in opts:
        if opt in ['-D']:
            print('directory mode')

        if opt in ['-d']:
            print('dev mode ' + file)

        if opt in ['-r']:
            print('report mode ' + file)


if __name__ == "__main__":
   main(sys.argv[:1], sys.argv[2:])


  
