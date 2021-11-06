import sys, getopt


def main(args):
    opts, args = getopt.getopt(args,"Ddr")
    #return print(opts)

    for opt, args in opts:
        if opt in ['-D']:
            print('directory mode')

        if opt in ['-d']:
            print('dev mode')

        if opt in ['-r']:
            print('report mode')


if __name__ == "__main__":
   main(sys.argv[1:])


  
